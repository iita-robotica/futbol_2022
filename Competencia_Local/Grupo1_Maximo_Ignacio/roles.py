# -*- coding: utf-8 -*-
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
            if ball.x < 0:
                offset = Point(0.05, 0.0 )
                robot.moveToBall(offset)
            #robot.moveToBall()
            else:
                offset = Point(-0.05, 0.0 )
                robot.moveToBall(offset)
        else:
            ball = Point.ORIGIN
            masadelanteA=Point(0.35, 0.20 * -(equipo))
            robot.moveToPoint(masadelanteA)
   
        
        """if snapshot.ball != None:
            offset = Point(0.05, 0.0 )
            robot.moveToBall(offset)
            #robot.moveToBall()
        elif snapshot.ball != x2:
            offset = Point(-0.05, 0.0 )
            robot.moveToBall(offset)"""


            #robot.moveToBall()
        #else:
            #masadelanteA=Point(0.35, 0.20 * -(equipo))
            #robot.moveToPoint(masadelanteA)
            
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

# Tercer rol 
class Defender:
    def applyOn(self, robot, snapshot):
        if snapshot.color == "B":
            equipo = 1
        else:
            equipo = -1
        if snapshot.ball != None:
            offset = Point(0.05, 0.0 )
            robot.moveToBall(offset)
            #robot.moveToBall()
        else:
            masadelanteB=Point(-0.35, 0.20 * -(equipo))
            robot.moveToPoint(masadelanteB)
            #robot.moveToPoint(Point.ORIGIN)
            

            