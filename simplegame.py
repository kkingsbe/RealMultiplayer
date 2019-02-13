import json
import pygame
import socket

pygame.init() #Initializes the modules needed for PyGame
screen = pygame.display.set_mode((400, 300)) #Creates a window of the desired size
done = False
is_blue = True
y = 30
x = 30
clock = pygame.time.Clock()

TCP_IP = '54.172.15.213'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)
    return d

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    screen.fill((0,0,0)) #Clears the screen
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #Draws a rectangle (screen object, RGB, x & y coords of upper left corner, width, and height

    data = json.dumps({"x" : x, "y" : y}).encode("utf8")
    s.send(bytes(data))

    data = json.loads(s.recv(BUFFER_SIZE))

    print("X2 : " + str(data["x"]))
    pygame.draw.rect(screen, color, pygame.Rect(data["x"], data["y"], 60, 60))
    pygame.display.flip()  # Swaps buffers to make the game screen become visible
    clock.tick(60) #Waits 1/60th of a second, allowing the game to run at 60fps
s.close()