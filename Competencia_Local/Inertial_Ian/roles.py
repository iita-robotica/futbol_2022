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

        default = Point(equipo * 0.4, equipo * 0.4)
        

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


        range_a = 0.3

        default = Point(0, equipo * 0.55)
        
        left_corner = Point(equipo * 0.3, equipo * 0.55)
        right_corner = Point(equipo * (-0.3), equipo * 0.55)


        if snapshot.ball != None:
            ball = snapshot.ball.position

            target = Point(ball.x, equipo * 0.55)

            left_target = Point(equipo * 0.3, ball.y)
            right_target = Point(equipo * (-0.3), ball.y)


            if ball.y < 0 and ball.y < range_a:
                #print("caso 1: pelota lejos de mi arco")
                if ball.x <= 0.35 and ball.x >= -0.35:
                    #print("caso 1,1: pelota en el margen del área")
                    if robot.getPosition().dist(target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(target)
                
                elif equipo * ball.x > 0.35:
                    #print("caso 1,2: pelota a la izquierda del margen del área")
                    if robot.getPosition().dist(left_corner) < 0.01:
                        robot.lookAtPoint(ball)
                    else:
                        robot.moveToPoint(left_corner)
                
                else:
                    #print("caso 1,3: pelota a la derecha del margen del área")
                    if robot.getPosition().dist(right_corner) < 0.01:
                        robot.lookAtPoint(ball)
                    else:
                        robot.moveToPoint(right_corner)
                
            
            else:
                #print("caso 2: pelota cerca de mi arco")
                if ball.x <= 0.35 and ball.x >= -0.35:
                    #print("caso 2,1: pelota en el margen del área")
                    if robot.getPosition().dist(ball) < 0.01:
                        robot.moveToBall()
                    else:
                        robot.moveToPoint(target)

                elif equipo * ball.x > 0.35:
                    #print("caso 2,2: pelota a la izquierda del margen del área")
                    if robot.getPosition().dist(left_target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(left_target)

                else:
                    #print("caso 2,3: pelota a la derecha del margen del área")
                    if robot.getPosition().dist(right_target) < 0.01:
                        robot.lookAtAngle(degrees(90))
                    else:
                        robot.moveToPoint(right_target)


        else:
            robot.moveToPoint(default)

