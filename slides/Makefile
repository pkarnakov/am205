ZIPDIR = am205_2022_slides
ZIP = zip

default:

zip: $(ZIPDIR).zip

$(ZIPDIR).zip: export_files
	mkdir "$(ZIPDIR)"
	rsync -L --files-from 'export_files' --exclude 'export_files' . "$(ZIPDIR)"
	rsync -va index.html dist plugin "$(ZIPDIR)"
	$(ZIP) -0 -r "$@" "$(ZIPDIR)"
	rm -vrf "$(ZIPDIR)"

.PHONY: default zip
