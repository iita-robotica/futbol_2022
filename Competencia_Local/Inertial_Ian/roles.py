# -*- coding: utf-8 -*-
from math_utils.point import Point
from math_utils.angle import degrees

class Forwarder:
    def applyOn(self, robot, snapshot):
         
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1

        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN
        
        
        range_b = 0.0

        target = Point(ball.x + 0.5, equipo * -0.35)
        default = Point(-0.25, equipo * (-0.25))

        goal = Point(0.0, equipo * (-0.8))

        x = ball.x
        y = ball.y

        distance_x = robot.getPosition().x - x
        distance_y = robot.getPosition().y - y


        if (equipo * y) > range_b:
            if robot.getPosition().dist(target) < 0.01:
                robot.lookAtAngle(degrees(90))
            else:
                robot.moveToPoint(target)

        elif (equipo * y) <= range_b:
            if snapshot.ball != None:
                if 0 < distance_y <= 0.15 and abs(distance_x) <= 0.1:
                    robot.moveToPoint(goal)
                    if snapshot.ball != None:
                        robot.moveToPoint(default)
                else:
                    robot.moveToBall()
            else:
                robot.moveToPoint(default)

        else:
            if snapshot.ball != None:
                robot.moveToBall()
            else:
                robot.moveToPoint(default)


class Midfielder:
    def applyOn(self, robot, snapshot):
        
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1

        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN
        
        
        range_b = 0.0

        target = Point(ball.x, 0.0)

        goal = Point(0.0, equipo * (-0.8))

        x = ball.x
        y = ball.y

        distance_x = robot.getPosition().x - x
        distance_y = robot.getPosition().y - y


        if (equipo * y) > range_b:
            if snapshot.ball != None:
                if 0 < distance_y <= 0.15 and abs(distance_x) <= 0.1:
                    robot.moveToPoint(target)
                else:
                    robot.moveToBall()
            else:
                robot.moveToPoint(Point.ORIGIN)

        elif (equipo * y) <= range_b:
            if snapshot.ball != None:
                if 0 < distance_y <= 0.15 and abs(distance_x) <= 0.1:
                    robot.moveToPoint(goal)
                    if snapshot.ball != None:
                        robot.moveToPoint(Point.ORIGIN)
                else:
                    robot.moveToBall()
            else:
                robot.moveToPoint(Point.ORIGIN)

        else:
            if snapshot.ball != None:
                robot.moveToBall()
            else:
                robot.moveToPoint(Point.ORIGIN)
            
            
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


        range_a = 0.3

        target = Point(ball.x, equipo * 0.55)

        left_target = Point(equipo * 0.3, ball.y)
        right_target = Point(equipo * (-0.3), ball.y)

        left_corner = Point(equipo * 0.3, equipo * 0.55)
        right_corner = Point(equipo * (-0.3), equipo * 0.55)

        x = ball.x
        y = ball.y


        if y < 0 and abs(y) < range_a:
            if x <= 0.35 and x >= -0.35:
                if robot.getPosition().dist(target) < 0.01:
                    robot.lookAtAngle(degrees(90))
                else:
                    robot.moveToPoint(target)
            
            elif equipo * x > 0.35:
                robot.moveToPoint(left_corner)
                robot.lookAtPoint(ball)
            
            elif equipo * x < -0.35:
                robot.moveToPoint(right_corner)
                robot.lookAtPoint(ball)
            
            else:
                robot.lookAtPoint(ball)
        
        elif y < 0 and abs(y) >= range_a:
            if x <= 0.35 and x >= -0.35:
                if snapshot.ball != None:
                    robot.moveToBall()
                else:
                    robot.moveToPoint(target)

            elif equipo * x > 0.35:
                if robot.getPosition().dist(left_target) < 0.01:
                    robot.lookAtAngle(degrees(90))
                else:
                    robot.moveToPoint(left_target)

            elif equipo * x < -0.35:
                if robot.getPosition().dist(right_target) < 0.01:
                    robot.lookAtAngle(degrees(90))
                else:
                    robot.moveToPoint(right_target)

        else:
            robot.moveToPoint(target)
   