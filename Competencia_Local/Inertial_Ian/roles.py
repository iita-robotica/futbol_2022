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
                if (distance_y < range_b) and (abs(distance_y) <= 0.25) and (abs(distance_x) <= 0.1):
                    print("yendo al gol")
                    robot.moveToPoint(goal)
                else:
                    print("acercandome a la pelota")
                    robot.moveToBall()
            
            else:
                if (equipo * ball.y < equipo * 0.3) and (equipo * distance_y <= 0.25) and (equipo * distance_x <= 0.1):
                    print("asegurando la pelota")
                    robot.moveToBall()
                else:
                    print("esperando")
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

        default = Point(equipo * 0.4, equipo * 0.3)
        

        if snapshot.ball != None:
            ball = snapshot.ball.position

            target = Point(ball.x, equipo * 0.3)

            distance_y = robot.getPosition().y - ball.y
            distance_x = robot.getPosition().x - ball.x


            if (equipo * ball.y) <= range_b:
                target = Point(ball.x - 0.2, equipo * 0.3)

                if robot.getPosition().dist(target) < 0.01:
                    robot.lookAtAngle(degrees(90))
                else:
                    robot.moveToPoint(target)
            
            else:
                target = Point(ball.x + 0.2, equipo * 0.3)

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


        range_a = equipo * 0.3

        default = Point(0, equipo * 0.55)
        
        left_corner = Point(equipo * 0.3, equipo * 0.55)
        right_corner = Point(equipo * (-0.3), equipo * 0.55)


        if snapshot.ball != None:
            ball = snapshot.ball.position

            target = Point(ball.x, equipo * 0.55)

            left_target = Point(equipo * 0.3, ball.y)
            right_target = Point(equipo * (-0.3), ball.y)


            if (equipo == 1 and ball.y < range_a) or (equipo == -1 and ball.y > range_a):
              
                if (equipo * ball.y) < 0:
                    if robot.getPosition().dist(target) < 0.01:
                            robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(target)

                else:

                    if ball.x <= 0.35 and ball.x >= -0.35:
                        if robot.getPosition().dist(target) < 0.01:
                            robot.lookAtAngle(degrees(90))
                        else:
                            robot.moveToPoint(target)
                    
                    elif equipo * ball.x > 0.35:
                        if robot.getPosition().dist(left_corner) < 0.01:
                            robot.lookAtPoint(ball)
                        else:
                            robot.moveToPoint(left_corner)
                    
                    else:
                        if robot.getPosition().dist(right_corner) < 0.01:
                            robot.lookAtPoint(ball)
                        else:
                            robot.moveToPoint(right_corner)
                
            
            else:

                if ball.x <= 0.35 and ball.x >= -0.35:
                    if ((equipo * robot.getPosition().y) <= (equipo * 0.5)) and (robot.getPosition().dist(ball) < 0.02):
                        robot.moveToBall()
                    else:
                        robot.moveToPoint(target)

                elif equipo * ball.x > 0.35:
                    if robot.getPosition().dist(left_target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(left_target)

                else:
                    if robot.getPosition().dist(right_target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(right_target)


        else:
            robot.moveToPoint(default)

