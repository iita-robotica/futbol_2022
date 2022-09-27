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
            ball = snapshot.ball.position
            robot.moveToBall()
        else:
            puntoDefinido = Point(0, 0.1 * -(equipo))
            robot.moveToPoint(puntoDefinido)

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
            if robot.getPosition().dist(Point(ball.x, ball.y)) < equipo * 0.065:
                if abs(ball.x) >= 0.55:
                    if ball.x > 0:
                        robot.moveToPoint(Point(ball.x - 0.20, equipo*0.55))
                    elif ball.x < 0:
                        robot.moveToPoint(Point(ball.x + 0.20, equipo*0.55))
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

        targetDefensor = Point(0.0, 0.0)
        target = Point(ball.x, equipo * 0.25)
        if abs(ball.y) >= 0.25 and abs(ball.y) < 0.8:
            robot.lookAtAngle(degrees(90), 8.9)
            offset = Point((-equipo) * 0.12, 0.0)
            robot.moveToBall(offset)
        else:
            robot.moveToPoint(target)
            if robot.getPosition().dist(target) <= 0.01:
                robot.lookAtAngle(degrees(90))
                if abs(ball.x) >= 0.35:
                    robot.moveToPoint(targetDefensor)
                    if (ball.y < -0.6 or ball.y > -0.6) and (ball.y >= equipo * 0.25):
                        robot.lookAtAngle(degrees(equipo*45))
                        robot.lookAtAngle(degrees(equipo * -45))
