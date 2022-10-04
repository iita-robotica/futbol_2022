# -*- coding: utf-8 -*-
from re import A
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

        goal = Point(0.0, equipo * (-0.8))

        distance_y = robot.getPosition().y - ball.y


        if snapshot.ball != None:

            if (equipo * ball.y) > range_b:
                if distance_y <= 0.15:
                    robot.lookAtPoint(goal)
                    robot.moveToBall()
                else:
                    robot.moveToBall()
            elif (equipo * ball.y) <= range_b:
                if distance_y <= 0.15:
                    robot.moveToBall()
                elif distance_y > 0.15:
                    robot.moveToPoint(Point.ORIGIN)
                    robot.lookAtPoint(ball)
        
        else:
            robot.moveToPoint(Point.ORIGIN)



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
        
        target = Point(ball.x, equipo * 0.4)

        default = Point(ball.x, 0.0)

        distance_y = robot.getPosition().y - ball.y


        if snapshot.ball != None:

            if (equipo * ball.y) > 0:
                target = Point(ball.x - 0.2, equipo * 0.4)
            elif (equipo * ball.y) < 0:
                target = Point(ball.x + 0.2, equipo * 0.4)

            if (equipo * ball.y) > range_b:
                if robot.getPosition().dist(target) < 0.01:
                    robot.lookAtAngle(degrees(90))
                else:
                    robot.moveToPoint(target)
            elif (equipo * ball.y) <= range_b:
                if distance_y <= 0.3:
                    robot.moveToBall()
                elif distance_y > 0.3:
                    if robot.getPosition().dist(target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(target)
            else:
                robot.moveToPoint(default)
        
        else:
            robot.moveToPoint(default)
            


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

        x,y = 0,0
        if robot.teamMessages:
            x,y = max(robot.teamMessages)


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
        
        elif abs(y) >= range_a:
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
   