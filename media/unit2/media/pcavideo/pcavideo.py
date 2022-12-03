#!/usr/bin/env python3

from PIL import Image
from glob import glob
import numpy as np
import os
import matplotlib.pyplot as plt
import pickle


def load(dirname):
    files = glob(os.path.join(dirname, "a_*.png"))
    files = sorted(files)
    images = []
    for i, fpath in enumerate(files):
        if i % 10 == 0:
            print(fpath)
        img = Image.open(fpath)
        img = np.array(img)[:, :, :3].astype(np.float32) / 255.
        images.append(img)
    return np.array(images)


def pca(images, cachename=None):
    mean = np.mean(images, axis=0)
    images = np.array(images)
    images -= mean[None, ...]
    imsize = images[0].shape
    nimg = len(images)
    images = np.reshape(images, (nimg, -1))
    (u, s, v) = np.linalg.svd(images, full_matrices=0)
    u = u.astype(np.float32)
    s = s.astype(np.float32)
    v = v.astype(np.float32)
    return u, s, v, imsize, mean

def load_pca(dirname):
    cachename = dirname
    if cachename:
        cachepath = 'cache_{}.pickle'.format(cachename)
        if os.path.isfile(cachepath):
            print("Loading cache '{}'".format(cachepath))
            with open(cachepath, 'rb') as f:
                return pickle.load(f)
    images = load(dirname)
    print("PCA " + dirname)
    res = pca(images)
    if cachename:
        print("Saving cache '{}'".format(cachepath))
        with open(cachepath, 'wb') as f:
            pickle.dump(res, f)
    return res

def save(dirname, images, imsize):
    os.makedirs(dirname, exist_ok=True)
    for i in range(images.shape[0]):
        path = os.path.join(dirname, "a_{:05d}.png".format(i))
        if os.path.isfile(path) and 0:
            if i % 10 == 0:
                print("skip existing '{}'".format(path))
            continue
        img = np.clip(mean + images[i].reshape(imsize), 0, 1)
        img = (img * 255).astype(np.uint8)
        img = Image.fromarray(img)
        if i % 10 == 0:
            print(path)
        img.save(path)


if __name__ == "__main__":
    for dirname in [
            'paris',
            'vietnam',
            'sunrise',
    ]:
        u, s, v, imsize, mean = load_pca(dirname)
        save(dirname + '_first3', u @ np.diag(np.hstack(
            (s[:3], s[3:] * 0))) @ v, imsize)
        save(dirname + '_zero3', u @ np.diag(np.hstack(
            (s[:3] * 0, s[3:]))) @ v, imsize)
