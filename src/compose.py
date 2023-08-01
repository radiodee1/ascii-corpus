# import the pygame module, so you can use it
import pygame
import sys

import random
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    square_size = 30 
    size_x = 340 
    size_y = 280 
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((size_x,size_y))
    screen.fill('white') 
    # define a variable to control the main loop
    running = True
    
    objects = []

    tot = int(sys.argv[1].split(".")[-2])
    
    spot = 0 
    if len(sys.argv) > 2:
        print(sys.argv[2], tot)
        while len(objects) < tot and spot < 2000:
            x = random.randint(0 + square_size , size_x - square_size )
            y = random.randint(0 + square_size , size_y - square_size )
            if len(objects) == 0:
                objects.append((x,y))
            #box = (x,y)
            keep = True
            for prev in objects:
                p_x = prev[0]
                p_y = prev[1]
                square_size_plus = square_size * 2

                span_x = [ i for i in range(p_x - square_size_plus , p_x + square_size_plus ) ]
                span_y = [ i for i in range(p_y - square_size_plus , p_y + square_size_plus ) ]
                #print(span_x)
                if x in span_x and y in span_y:
                    keep = False
                    #objects.append((x,y))
            if keep:
                objects.append((x,y))
            spot += 1 
        pass 

    # main loop
    while running:
        #screen.fill("white")
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                down1, down2 = pygame.mouse.get_pos()
                print(down1, down2)
                objects.append((down1, down2))
                #down3 = down1 + 5
                #down4 = down2 + 5
                #pygame.draw.rect(screen, 'red',  [down1, down2, down3, down4], 2 )
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            for i in objects:
                down1, down2 = i 
                down1 -= square_size / 2 
                down2 -= square_size / 2
                down3 = square_size
                down4 = square_size
                pygame.draw.rect(screen, 'black',  [down1, down2, down3, down4] )
                #print(i, 'red')

        pygame.display.set_caption(sys.argv[1].split('/')[-1])
        pygame.display.flip()
        if len(sys.argv) > 2:
            running = False
    
    print(sys.argv)
    num = sys.argv[1].split(".")[-2]

    if len(objects) > 0 or num.startswith('0'):
        print(num)
        name = '../../test.png'
        if len(sys.argv) >= 2:
            name = sys.argv[1]
            print(name)
        pygame.image.save(screen, name)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
