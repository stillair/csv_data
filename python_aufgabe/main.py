import pygame, math
import pandas as pd
from pygame.locals import *
from datetime import datetime
pygame.init()

x_max = 400
y_man = 400

screen = pygame.display.set_mode([x_max, y_man])
screen.fill([255,255,255])
clock = pygame.time.Clock()

class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.time = datetime.now()

class CSVData:
    def __init__(self, pointA, pointB):
        self.pointA_coords = [pointA.x_coord, pointA.y_coord]
        self.pointA_time = pointA.time
        self.pointB_coords = [pointB.x_coord, pointB.y_coord]
        self.pointB_time = pointB.time


def calcVelocity(a: Point, b: Point):
    distance = math.hypot(a.x_coord - b.x_coord, a.y_coord-b.y_coord) # distance between the clicks
    time_difference = (b.time - a.time).total_seconds() # seconds between the clicks
    velocity = distance / time_difference # velocity in pixel per second
    return velocity


def main():
   clicks = 0
   df1 = pd.DataFrame(pd.read_csv('data.csv'))
   #print(df1)
   while True:     
      for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               return
            elif event.type == MOUSEBUTTONDOWN:
               clicks += 1 # add click
               print(clicks)
               pos = pygame.mouse.get_pos()
               if (clicks % 2) == 0: # check if click is even
                    pointB = Point(pos[0], pos[1])
                    velocity = calcVelocity(pointA, pointB)
                    print(calcVelocity(pointA, pointB))
                    startpoint = f'X: {pointA.x_coord} Y: {pointA.y_coord}'
                    endpoint = f'X: {pointB.x_coord} Y: {pointB.y_coord}'
                    print(startpoint)
                    data = {
                        'Startpunkt': [startpoint],
                        'Startzeit': [pointA.time.strftime("%m/%d/%Y, %H:%M:%S:%f")],
                        'Endpunkt': [endpoint],
                        'Endzeit': [pointB.time.strftime("%m/%d/%Y, %H:%M:%S:%f")]
                    }
                    
                    df2 = pd.DataFrame(data)
                    df1 = df1.append(df2, ignore_index=True, sort=False)
                    df1.to_csv('data.csv')
                    print(df1)
                    print('add even point')
               else:
                    pointA = Point(pos[0], pos[1])
                    print('add odd point')
      clock.tick(30)

# Execute game:
main()
