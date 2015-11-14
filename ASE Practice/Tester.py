from StateMachine import *
from MapEntities import *
from MapState import *
import pygame,time

(width,height) = (1000,1000)
screen = pygame.display.set_mode((width, height))
pygame.init()
screenInf = ScreenInfo(screen,width,height)

## Every GeneralState must have
## A Screen

## Every Option State must have:
## A Screen
## List of Labels
## List of next states
## Screen Size info

## Every Map State must have:
## A Screen
## A Player
## List of Tiles
## Bounds (can be taken from Map)

## General Notes
## Maps should be loaded in the beginning

player = Player(screenInf,0,0,None)
mp = Map(screenInf,'AtoBatMapTest.png',1000,1000)
ms = MapState(screenInf,player,mp.loadMap(),mp.minX,mp.maxX,mp.minY,mp.maxY)

lis = ['QUIT','QUIT2',"Map"]
Quit = QuitState(screenInf)
states = [Quit,Quit,ms]
state = OptionState(screenInf,lis,states,False,10,10,100,100)

SM = AtoBatMachine(state)
SM.run()
