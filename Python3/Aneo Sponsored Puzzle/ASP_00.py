import sys
import math
import numpy
import decimal

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class light:

    def __init__(self, distance, duration):
        self.distance = int(distance)
        self.duration = int(duration)

    def isGreenAtArrival(self, arrivalTime:decimal.Decimal):
        noOfHalfPeriods= arrivalTime//self.duration
        return True if noOfHalfPeriods%2 == 0 else False  

    def arrivalTime(self, startTime, startDistance, speed_kmh):
        speed_ms = speed_kmh/decimal.Decimal(3.6)
        travelDistance = self.distance - startDistance
        return startTime + decimal.Decimal(travelDistance/speed_ms)
        

def doesNotGoThrough(lights, speed_kmh):

    timePassed = 0
    currentDistanceFromStart = 0

    for currentLight in lights: #type: light
        arrivalAtGreenLight = currentLight.arrivalTime(timePassed, currentDistanceFromStart, speed_kmh)

        if currentLight.isGreenAtArrival(arrivalAtGreenLight):
            timePassed = arrivalAtGreenLight
            currentDistanceFromStart = currentLight.distance
        else: #ran a red light
            return True 

    #it came through!
    return False


speed_kmh = int(input()) 
light_count = int(input())

lights = numpy.empty(light_count, light)

for i in range(light_count):
    distance, duration = [j for j in input().split()]
    lights[i] = light(distance, duration)

while doesNotGoThrough(lights, speed_kmh):
    speed_kmh -= 1

print(speed_kmh)
