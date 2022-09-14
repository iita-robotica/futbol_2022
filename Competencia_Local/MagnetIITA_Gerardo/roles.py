# -*- coding: utf-8 -*-
import random
from math_utils.point import Point
from math_utils.angle import degrees

class BallFollower:
    def applyOn(self, robot, snapshot):
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1

        if snapshot.ball != None:
            robot.moveToBall()
        else:
            puntoAleatorio = Point(0, 0.1 * -(equipo))
            robot.moveToPoint(puntoAleatorio)

class Goalkeeper:
    def applyOn(self, robot, snapshot):
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1

        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN

        target = Point(ball.x, equipo * 0.55)
        if robot.getPosition().dist(target) < equipo * 0.01: #Si el balón se encuentra dentro del rango del área no continuar hasta la colisión con pared - si es mayor al absoluto de 0.35 
            robot.lookAtAngle(degrees(90))
        else:
            robot.moveToPoint(target)

class Defender:
    def applyOn(self, robot, snapshot):
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1
