# -*- coding: utf-8 -*-
from math_utils.point import Point
from math_utils.angle import degrees

TIMEOUT_GOAL_ZONE = 60*1 # 15 segundos
# El rol "BallFollower" sigue ciegamente a la pelota.
# ¡Ojo que podemos meter goles en contra!
class BallFollower:
    def applyOn(self, robot, snapshot):
        # Si sabemos dónde está la pelota, nos movemos hacia ella.
        # Caso contrario, nos movemos al centro de la cancha
        if snapshot.ball != None:
            robot.moveToBall()
        else:
            robot.moveToPoint(Point.ORIGIN)

# El rol "Goalkeeper" implementa un arquero básico
class Goalkeeper:
    timeout = TIMEOUT_GOAL_ZONE
    goaly = 0.55

    def applyOn(self, robot, snapshot):
        # Definimos un punto objetivo en el cual queremos ubicar el robot.
        # Este punto está dado por la coordenada X de la pelota y un valor
        # de Y fijo (este valor está definido de forma que esté cerca del
        # arco pero fuera del área)
        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN

        # Si el robot está lo suficientemente cerca del punto objetivo,
        # entonces giramos para mirar a los laterales. Sino, nos movemos
        # hacia el punto objetivo
        target = Point(0.0, - 0.65)
        robot.moveToPoint(target)

        # Queda pendiente validar que el robot este dentro del area respecto a x
        # Por ahora solo valido que esta dentro del area en el eje y
        if abs(robot.getPosition().y) - self.goaly > 0 :
            self.timeout-=1
            print("Inside of timeout zone")
            if self.timeout < 0:
                print("TIEMPO DENTRO DEL ARCO  EXCEDIDO")
                # Reinicio el contador
                self.timeout=TIMEOUT_GOAL_ZONE
        else:
            self.timeout=TIMEOUT_GOAL_ZONE


# Tercer rol
class Defender:
    def applyOn(self, robot, snapshot):
        # Definimos un punto objetivo en el cual queremos ubicar el robot.
        # Este punto está dado por la coordenada X de la pelota y un valor
        # de Y fijo (este valor está definido de forma que esté cerca del
        # arco pero fuera del área)
        if snapshot.ball != None:
            ball = snapshot.ball.position
        else:
            ball = Point.ORIGIN

        # Si el robot está lo suficientemente cerca del punto objetivo,
        # entonces giramos para mirar a los laterales. Sino, nos movemos
        # hacia el punto objetivo
        target = Point(ball.x, - 0.25)
        if robot.getPosition().dist(target) < 0.01:
            robot.lookAtAngle(degrees(90))
        else:
            robot.moveToPoint(target)
