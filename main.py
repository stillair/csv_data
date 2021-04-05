import pygame, math
import pandas as pd
from pygame.locals import *
from datetime import datetime
pygame.init()

x_max = 400
y_man = 400

screen = pygame.display.set_mode((x_max, y_man))
screen.fill((0,0,0))
clock = pygame.time.Clock()
lineColor = pygame.Color(0, 255, 0)

class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.time = datetime.now()

def calcVelocity(a: Point, b: Point):
    distance = math.hypot(a.x_coord - b.x_coord, a.y_coord-b.y_coord) # distance between the clicks
    time_difference = (b.time - a.time).total_seconds() # seconds between the clicks
    velocity = distance / time_difference # velocity in pixel per second
    return velocity


def main():
   clicks = 0
   df1 = pd.DataFrame(pd.read_csv('data.csv')) # load data
   
   while True:     
      for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               return
            elif event.type == MOUSEBUTTONDOWN:
               clicks += 1 # add click
               pos = pygame.mouse.get_pos()

               if (clicks % 2) == 0: # second clicks
                    pointB = Point(pos[0], pos[1])

                    startpoint = f'X: {pointA.x_coord} Y: {pointA.y_coord}'
                    endpoint = f'X: {pointB.x_coord} Y: {pointB.y_coord}'
                    velocity = calcVelocity(pointA, pointB)

                    # write variables in data object
                    data = {
                        'Startpunkt': [startpoint],
                        'Startzeit': [pointA.time.strftime("%m/%d/%Y, %H:%M:%S:%f")],
                        'Endpunkt': [endpoint],
                        'Endzeit': [pointB.time.strftime("%m/%d/%Y, %H:%M:%S:%f")],
                        'Geschwindigkeit': [velocity]
                    }

                    pygame.draw.line(screen, lineColor, (pointA.x_coord, pointA.y_coord), (pointB.x_coord, pointB.y_coord), width=1) # draw line
                    
                    df2 = pd.DataFrame(data) # create new dataframe 
                    df1 = df1.append(df2, ignore_index=True, sort=False) # merge dataframes
                    df1.to_csv('data.csv', index=False) # save data
               else: # first clicks
                    pointA = Point(pos[0], pos[1])
      pygame.display.flip()
      clock.tick(30)

# Execute game:
main()
