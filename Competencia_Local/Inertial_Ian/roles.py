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


        range_b = 0.0

        goal = Point(0.0, equipo * (-0.8))

    
        if snapshot.ball != None:
            ball = snapshot.ball.position

            distance_y = robot.getPosition().y - ball.y
            distance_x = robot.getPosition().x - ball.x

            if (equipo * ball.y) <= range_b:
                if equipo * distance_y <= 0.1 and equipo * distance_x <= 0.1:
                    robot.moveToPoint(goal)
                else:
                    robot.moveToBall()
            
            else:
                if equipo * distance_y <= 0.1 and equipo * distance_x <= 0.1:
                    robot.moveToBall()
                else:
                    if robot.getPosition() == Point.ORIGIN:
                        robot.lookAtPoint(ball)
                    else:
                        robot.moveToPoint(Point.ORIGIN)

        else:
            robot.moveToPoint(Point.ORIGIN)
        


class Midfielder:
    def applyOn(self, robot, snapshot):
        
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1


        range_b = 0.0

        default = Point(equipo * 1, equipo * 1)
        

        if snapshot.ball != None:
            ball = snapshot.ball.position

            target = Point(ball.x, equipo * 1)

            distance_y = robot.getPosition().y - ball.y
            distance_x = robot.getPosition().x - ball.x


            if (equipo * ball.y) <= range_b:
                target = Point(ball.x - 0.2, equipo * 1)

                if robot.getPosition().dist(target) < 0.01:
                    robot.lookAtAngle(degrees(90))
                else:
                    robot.moveToPoint(target)
            
            else:
                target = Point(ball.x + 0.2, equipo * 1)

                if equipo * distance_y <= 0.3 and equipo * distance_x <= 0.3:
                    robot.moveToBall()
                else:
                    if robot.getPosition().dist(target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(target)
        
        else:
            robot.moveToPoint(default)


            
class Goalkeeper:
    def applyOn(self, robot, snapshot):
        
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1


        range_a = 0.3

        default = Point(equipo * 1, equipo * 1)
        
        target = Point(ball.x, equipo * 0.55)

        left_target = Point(equipo * 0.3, ball.y)
        right_target = Point(equipo * (-0.3), ball.y)

        left_corner = Point(equipo * 0.3, equipo * 0.55)
        right_corner = Point(equipo * (-0.3), equipo * 0.55)


        if snapshot.ball != None:
            ball = snapshot.ball.position

            if ball.y < 0 and abs(ball.y) < range_a:
                if ball.x <= 0.35 and ball.x >= -0.35:
                    if robot.getPosition().dist(target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(target)
                
                elif equipo * ball.x > 0.35:
                    robot.moveToPoint(left_corner)
                    robot.lookAtPoint(ball)
                
                elif equipo * ball.x < -0.35:
                    robot.moveToPoint(right_corner)
                    robot.lookAtPoint(ball)
                
            
            elif abs(ball.y) >= range_a:
                if ball.x <= 0.35 and ball.x >= -0.35:
                    if snapshot.ball != None:
                        robot.moveToBall()
                    else:
                        robot.moveToPoint(target)

                elif equipo * ball.x > 0.35:
                    if robot.getPosition().dist(left_target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(left_target)

                elif equipo * ball.x < -0.35:
                    if robot.getPosition().dist(right_target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(right_target)


            else:
                robot.moveToPoint(default)

        else:
            robot.moveToPoint(default)

