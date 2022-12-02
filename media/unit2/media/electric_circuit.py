#!/usr/bin/env python3

import schemdraw
import schemdraw.elements as elm
from schemdraw.types import Point
from util import get_path

path = get_path('svg')
with schemdraw.Drawing(show=False, file=path, metadata={'Date': None}) as d:
    R1 = elm.Resistor().label('$R_1$')
    R2 = elm.Resistor().label('$R_2$')
    R3 = elm.Resistor().label('$R_3$', loc='bot', ofst=(0.7, 0.1))
    R4 = elm.Resistor().label('$R_4$')
    R5 = elm.Resistor().label('$R_5$')
    R6 = elm.Resistor().label('$R_6$')
    V1 = elm.SourceV().label('$V_1$')
    V2 = elm.SourceV().label('$V_2$', loc='bot')
    L65 = elm.Line()
    L46 = elm.Line()
    d += L65.up(length=3)
    d += R5.left()
    d += elm.Dot()
    d += R4.left()
    d += L46.down()
    d += R6.endpoints(L46.end, L65.start)
    d += R3.at(R5.end).up()
    d += V1.at(R4.end).up()
    d += V2.at(R5.start).up()
    d += R1.endpoints(V1.end, R3.end)
    d += elm.Dot()
    d += R2.endpoints(V2.end, R3.end)
    d += elm.LoopArrow().at(R4.center, dy=1.6).label('$I_1$').color('C1')
    d += elm.LoopArrow(direction='ccw', theta1=-145,
                       theta2=-215).at(R5.center,
                                       dy=1.6).label('$I_2$').color('C2')
    d += elm.LoopArrow(direction='ccw', theta1=-145,
                       theta2=-215).at(R6.center,
                                       dy=1.6).label('$I_3$').color('C3')
print(path)
