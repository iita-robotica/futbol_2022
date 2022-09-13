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
        if robot.getPosition().dist(target) < equipo * 0.01:
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
        print(f'{abs(ball.y)} >= 0.25 and {abs(ball.y)} < 0.8')
        if abs(ball.y) >= 0.25 and abs(ball.y) < 0.8:
            robot.lookAtAngle(degrees(90), 8.9)
            robot.moveToBall()
        else:
            robot.moveToPoint(target)
            if robot.getPosition().dist(target) <= 0.01:
                robot.lookAtAngle(degrees(90))
                if (ball.y < -0.6 or ball.y > -0.6) and (ball.y >= equipo * 0.25):
                    robot.lookAtAngle(degrees(equipo*45))
                    robot.lookAtAngle(degrees(equipo * -45))
