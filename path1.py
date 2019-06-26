import math, sys, pygame, random
from math import *
from pygame import *

class Node(object):
    def __init__(self, point, parent):
        super(Node, self).__init__()
        self.point = point
        self.parent = parent

XDIM = 800
YDIM = 800
windowSize = [XDIM, YDIM]
delta = 10.0
GAME_LEVEL = 1
GOAL_RADIUS = 10
MIN_DISTANCE_TO_ADD = 1.0
NUMNODES = 5000
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode(windowSize)
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 255, 0
green = 0, 0, 255
cyan = 0,180,105

count = 0
rectObs = []

def dist(p1,p2):    #distance between two points
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def point_circle_collision(p1, p2, radius):
    distance = dist(p1,p2)
    if (distance <= radius):
        return True
    return False

def step_from_to(p1,p2):
    if dist(p1,p2) < delta:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + delta*cos(theta), p1[1] + delta*sin(theta)

def collides(p):    #check if point collides with the obstacle
    for rect in rectObs:
        if rect.collidepoint(p) == True:
            return True
    return False




def get_random_clear():
    while True:
        p = random.random()*XDIM, random.random()*YDIM
        noCollision = collides(p)
        if noCollision == False:
            return p


def init_obstacles(configNum):  #initialized the obstacle
    global rectObs
    rectObs = []
    print("config "+ str(configNum))
    rectObs.append(pygame.Rect((250,250),(100,100)))
    rectObs.append(pygame.Rect((390,390),(120,120)))
    pygame.draw.circle(screen, black, (300,300), 50)
    pygame.draw.circle(screen, black, (450,450), 60)
    


def reset():
    global count
    screen.fill(white)
    init_obstacles(GAME_LEVEL)
    count = 0

def main():
    global count
    
    initPoseSet = False
    initialPoint = Node(None, None)
    goal1PoseSet = False
    goal1Point = Node(None, None)
    goal2PoseSet = False
    goal2Point = Node(None, None)
    currentState = 'init'

    nodes1 = []
    nodes2 = []
    reset()

    while True:
        if currentState == 'init':
            print('goal point not yet set')
            pygame.display.set_caption('Select Starting Point and then Goal Point')
            initialPoint = Node((0,0), None)
            fpsClock.tick(10)
            nodes1.append(initialPoint) # Start in the center
            initPoseSet = True
            pygame.draw.circle(screen, red, initialPoint.point, GOAL_RADIUS)
            goal1Point = Node((700,400),None)
            goal1PoseSet = True
            pygame.draw.circle(screen, green, goal1Point.point, GOAL_RADIUS)
            currentState = 'buildTree1'
        elif currentState == 'goal1Found':
            currNode = goal1Node.parent
            pygame.display.set_caption('Goal1 Reached')
            print("Goal1 Reached")
            while currNode.parent != None:
                pygame.draw.line(screen,red,currNode.point,currNode.parent.point)
                currNode = currNode.parent
            optimizePhase = True
            currentState = 'setgoal2'
            
        elif currentState == 'optimize':
            fpsClock.tick(0.5)
            pass
        elif currentState == 'buildTree1':
            count = count+1
            pygame.display.set_caption('Performing RRT')
            if count < NUMNODES:
                foundNext = False
                while foundNext == False:
                    rand = get_random_clear()
                    parentNode = nodes1[0]
                    for p in nodes1:
                        if dist(p.point,rand) <= dist(parentNode.point,rand):
                            newPoint = step_from_to(p.point,rand)
                            if collides(newPoint) == False:
                                parentNode = p
                                foundNext = True

                newnode = step_from_to(parentNode.point,rand)
                nodes1.append(Node(newnode, parentNode))
                pygame.draw.line(screen,cyan,parentNode.point,newnode)

                if point_circle_collision(newnode, goal1Point.point, GOAL_RADIUS):
                    currentState = 'goal1Found'
                    goal1Node = nodes1[len(nodes1)-1]

                
            else:
                print("Ran out of nodes... :(")
                return;
        elif currentState == 'setgoal2':
            print('goal point2 not yet set')
            pygame.display.set_caption('Select Starting Point and then Goal Point')
            initialPoint = Node((0,0), None)
            fpsClock.tick(10)
            nodes2.append(initialPoint) # Start in the center
            initPoseSet = True
            pygame.draw.circle(screen, red, initialPoint.point, GOAL_RADIUS)
            goal2Point = Node((700,700),None)
            goal2PoseSet = True
            pygame.draw.circle(screen, green, goal2Point.point, GOAL_RADIUS)
            currentState = 'buildTree2'
        elif currentState == 'buildTree2':
            count = count+1
            pygame.display.set_caption('Performing RRT')
            if count < NUMNODES:
                foundNext = False
                while foundNext == False:
                    rand = get_random_clear()
                    parentNode = nodes2[0]
                    for p in nodes1:
                        if dist(p.point,rand) <= dist(parentNode.point,rand):
                            newPoint = step_from_to(p.point,rand)
                            if collides(newPoint) == False:
                                parentNode = p
                                foundNext = True

                newnode = step_from_to(parentNode.point,rand)
                nodes2.append(Node(newnode, parentNode))
                pygame.draw.line(screen,cyan,parentNode.point,newnode)

                if point_circle_collision(newnode, goal2Point.point, GOAL_RADIUS):
                    currentState = 'goal2Found'
                    goal2Node = nodes2[len(nodes2)-1]

        

        

        pygame.display.update()
        fpsClock.tick(10000)

        



if __name__ == '__main__':
    main()
