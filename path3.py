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
    rectObs.append(pygame.Rect((180,180),(40,40)))
    rectObs.append(pygame.Rect((520,520),(60,60)))
    rectObs.append(pygame.Rect((160,540),(80,80)))
    rectObs.append(pygame.Rect((230,530),(40,40)))
    pygame.draw.circle(screen, black, (200,200), 20)
    pygame.draw.circle(screen, black, (550,550), 30)
    pygame.draw.circle(screen, black, (200,600), 40)
    pygame.draw.circle(screen, black, (250,550), 20)
    


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
    goal3PoseSet = False
    goal3Point = Node(None, None)
    goal4PoseSet = False
    goal4Point = Node(None, None)
    currentState = 'init'

    nodes1 = []
    nodes2 = []
    nodes3 = []
    nodes4 = []
    reset()

    while True:
        if currentState == 'init':
            print('goal point not yet set')
            pygame.display.set_caption('Select Starting Point and then Goal Point')
            initialPoint = Node((400,400), None)
            fpsClock.tick(10)
            nodes1.append(initialPoint) # Start in the center
            initPoseSet = True
            pygame.draw.circle(screen, red, initialPoint.point, GOAL_RADIUS)
            goal1Point = Node((100,100),None)
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
            initialPoint = Node((400,400), None)
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
                    print('goal2Found')
        elif currentState == 'goal2Found':
            currNode = goal2Node.parent
            pygame.display.set_caption('Goal2 Reached')
            print("Goal2 Reached")
            while currNode.parent != None:
                pygame.draw.line(screen,red,currNode.point,currNode.parent.point)
                currNode = currNode.parent
            optimizePhase = True
            currentState = 'setgoal3'
            print("goal3")
        elif currentState == 'setgoal3':
            print('goal point not yet set')
            pygame.display.set_caption('Select Starting Point and then Goal Point')
            initialPoint = Node((400,400), None)
            fpsClock.tick(10)
            nodes1.append(initialPoint) # Start in the center
            initPoseSet = True
            pygame.draw.circle(screen, red, initialPoint.point, GOAL_RADIUS)
            goal3Point = Node((700,100),None)
            goal3PoseSet = True
            pygame.draw.circle(screen, green, goal1Point.point, GOAL_RADIUS)
            currentState = 'buildTree3'
        elif currentState == 'buildTree3':
            count = count+1
            pygame.display.set_caption('Performing RRT')
            if count < NUMNODES:
                foundNext = False
                while foundNext == False:
                    rand = get_random_clear()
                    parentNode = nodes3[0]
                    for p in nodes1:
                        if dist(p.point,rand) <= dist(parentNode.point,rand):
                            newPoint = step_from_to(p.point,rand)
                            if collides(newPoint) == False:
                                parentNode = p
                                foundNext = True

                newnode = step_from_to(parentNode.point,rand)
                nodes3.append(Node(newnode, parentNode))
                pygame.draw.line(screen,cyan,parentNode.point,newnode)

                if point_circle_collision(newnode, goal3Point.point, GOAL_RADIUS):
                    currentState = 'goal3Found'
                    goal3Node = nodes3[len(nodes3)-1]
                    print('goal3Found')
        elif currentState == 'goal3Found':
            currNode = goal3Node.parent
            pygame.display.set_caption('Goal3 Reached')
            print("Goal3 Reached")
            while currNode.parent != None:
                pygame.draw.line(screen,red,currNode.point,currNode.parent.point)
                currNode = currNode.parent
            optimizePhase = True
            currentState = 'setgoal4'
            print("goal4")
        elif currentState == 'setgoal4':
            print('goal point not yet set')
            pygame.display.set_caption('Select Starting Point and then Goal Point')
            initialPoint = Node((400,400), None)
            fpsClock.tick(10)
            nodes1.append(initialPoint) # Start in the center
            initPoseSet = True
            pygame.draw.circle(screen, red, initialPoint.point, GOAL_RADIUS)
            goal4Point = Node((50,700),None)
            goal4PoseSet = True
            pygame.draw.circle(screen, green, goal1Point.point, GOAL_RADIUS)
            currentState = 'buildTree4'
        elif currentState == 'buildTree4':
            count = count+1
            pygame.display.set_caption('Performing RRT')
            if count < NUMNODES:
                foundNext = False
                while foundNext == False:
                    rand = get_random_clear()
                    parentNode = nodes4[0]
                    for p in nodes1:
                        if dist(p.point,rand) <= dist(parentNode.point,rand):
                            newPoint = step_from_to(p.point,rand)
                            if collides(newPoint) == False:
                                parentNode = p
                                foundNext = True

                newnode = step_from_to(parentNode.point,rand)
                nodes4.append(Node(newnode, parentNode))
                pygame.draw.line(screen,cyan,parentNode.point,newnode)

                if point_circle_collision(newnode, goal3Point.point, GOAL_RADIUS):
                    currentState = 'goal4Found'
                    goal4Node = nodes4[len(nodes3)-1]
                    print('goal4Found')
        elif currentState == 'goal4Found':
            currNode = goal4Node.parent
            pygame.display.set_caption('Goal4 Reached')
            print("Goal4 Reached")
            while currNode.parent != None:
                pygame.draw.line(screen,red,currNode.point,currNode.parent.point)
                currNode = currNode.parent
            optimizePhase = True
            currentState = 'setgoal4'
            print("goal4")
                    
            
                    

        

        

        pygame.display.update()
        fpsClock.tick(10000)

        



if __name__ == '__main__':
    main()
