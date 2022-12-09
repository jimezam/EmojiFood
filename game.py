# v1
import pygame
import pygame.camera
from pygame.locals import *
from src.Food import Food
from src.Bug import Bug
from src.Player import Player

# v2
import cv2
import numpy as np

##############################################################

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

size = (WINDOW_WIDTH, WINDOW_HEIGHT)

FOOD_COUNT = 3
BUG_COUNT = 4

faceDetection = False

##############################################################

pygame.init()
pygame.camera.init()

display = pygame.display.set_mode(size)

# ,pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE

clist = pygame.camera.list_cameras()

if not clist:
    raise ValueError("Sorry, no cameras detected.")

cam = pygame.camera.Camera(clist[0], size)

cam.start()

clock = pygame.time.Clock()

##############################################################

sounds = { 
    "food_wasted": pygame.mixer.Sound("assets/sounds/food_wasted.mp3"), 
    "food_eaten": pygame.mixer.Sound("assets/sounds/food_eaten.mp3"), 
    "bug_eaten": pygame.mixer.Sound("assets/sounds/bug_eaten.mp3") 
}

##############################################################

allSprites = pygame.sprite.Group()
foods = pygame.sprite.Group()	 
bugs = pygame.sprite.Group() 

# Create the foods
for i in range(FOOD_COUNT):
    food = Food(WINDOW_WIDTH, WINDOW_HEIGHT)
    allSprites.add(food)
    foods.add(food)				

# Create the bugs
for i in range(BUG_COUNT):
    bug = Bug(WINDOW_WIDTH, WINDOW_HEIGHT)
    allSprites.add(bug)
    bugs.add(bug)				

# Create the player
player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
allSprites.add(player)

##############################################################

# v2

classificator = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

##############################################################

# create a surface to capture to.  for performance purposes
# bit depth is the same as that of the display surface.

snapshot = pygame.surface.Surface(size, 0, display)

running = True

while running:
    ##############################################################

    snapshot = cam.get_image()

    snapshot = pygame.transform.flip(snapshot, True, False)

    display.blit(snapshot, (0,0))

    ##############################################################

    # v2

    if(faceDetection):
        frame = pygame.surfarray.array3d(snapshot)
        frame = frame.swapaxes(0,1)

        # frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = classificator.detectMultiScale(gray, 1.1, 5)

        for (x,y,w,h) in faces:
            player.moveTo(x+w/2, y+h/2)
            break

    ##############################################################

    # Set the game's FPS
    clock.tick(60)

    # Update all the sprites in the game
    allSprites.update()

    allSprites.draw(display)

    pygame.display.flip()

    ##############################################################

    for sprite in allSprites:
        if int(sprite.rect.left) < 0:
            if(isinstance(sprite, Food)):
                sounds['food_wasted'].play()
            sprite.reset()
            
    ##############################################################

    hits = pygame.sprite.spritecollide(player, foods, False)
    for hit in hits:
        sounds['food_eaten'].play()
        hit.reset()

    hits = pygame.sprite.spritecollide(player, bugs, False)
    for hit in hits:
        sounds['bug_eaten'].play()
        hit.reset()

    ##############################################################

    events = pygame.event.get()

    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            running = False
        if e.type == KEYDOWN and e.key == K_f:
            faceDetection = not faceDetection
            print(f"Face detection is: {faceDetection}")

    keys = pygame.key.get_pressed()

    if(keys[K_LEFT] or keys[K_RIGHT] or
       keys[K_UP] or keys[K_DOWN]):
        player.move(keys)

##############################################################

cam.stop()
pygame.camera.quit()
pygame.quit()

##############################################################