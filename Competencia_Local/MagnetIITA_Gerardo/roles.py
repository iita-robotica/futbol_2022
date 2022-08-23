# -*- coding: utf-8 -*-
import random
from math_utils.point import Point
from math_utils.angle import degrees

class BallFollower:
    def applyOn(self, robot, snapshot):
        if snapshot.ball != None:
            robot.moveToBall()
        else:
            posAleatoriaX = random.uniform(0, 1)
            posAleatoriay = random.uniform(0, 1)
            puntoAleatorio = Point(posAleatoriaX, posAleatoriay)
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
        if robot.getPosition().dist(target) < 0.01:
            robot.lookAtAngle(degrees(90))
        else:
            robot.moveToPoint(target)

class Defender:
    def applyOn(self, robot, snapshot):
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1

        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN

        target = Point(ball.x, equipo * 0.25)

        if ball.y >= (-equipo) * 0.25 and ball.y < (-equipo) * 0.8:
            robot.lookAtAngle(degrees(90), 7.5)
            robot.moveToBall()
            print(ball.y)
        else:
            robot.moveToPoint(target)
            if robot.getPosition().dist(target) < 0:
                robot.lookAtAngle(degrees(90))

            