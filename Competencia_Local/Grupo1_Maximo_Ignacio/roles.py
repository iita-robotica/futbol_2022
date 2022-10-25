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
                if ball.y < 0.33* -(equipo):
                    offset = Point(-0.01, 0.0 )
                    robot.moveToBall(offset)
                    print("giro")
            else:
                offset = Point(-0.05, 0.0 )
                robot.moveToBall(offset)
                if ball.y < 0.33* -(equipo):
                    offset = Point(0.01, 0.0 )
                    robot.moveToBall(offset)
        else:
            ball = Point.ORIGIN
            masadelanteA=Point(0.35, 0.20 * -(equipo))
            if masadelanteA == robot.getPosition():
                robot.lookAtBall()
                print("lookAtBallDELANTERO")
            else:
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
            ball = snapshot.ball.position
            if ball.x < 0:
                offset = Point(0.05, 0.0 )
                robot.moveToBall(offset)
            #robot.moveToBall()
                if ball.y < 0.33* -(equipo):
                    offset = Point(-0.01, 0.0 )
                    robot.moveToBall(offset)  
                    print("girodefensor")
            else:
                offset = Point(-0.05, 0.0 )
                robot.moveToBall(offset)
                if ball.y < 0.33* -(equipo):
                    offset = Point(0.01, 0.0 )
                    robot.moveToBall(offset)
            
            #robot.moveToBall()
        else:
            ball = Point.ORIGIN
            masadelanteB=Point(-0.35, 0.20 * -(equipo))
            if masadelanteB == robot.getPosition():
                robot.lookAtBall()
                print("lookAtBallDEFENSOR")
            else:
                robot.moveToPoint(masadelanteB)
            #robot.moveToPoint(Point.ORIGIN)