# import the pygame module, so you can use it
import pygame
import sys
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))
    screen.fill('white') 
    # define a variable to control the main loop
    running = True
    
    objects = []

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
                down1 -= 15
                down2 -= 15
                down3 = 30
                down4 = 30
                pygame.draw.rect(screen, 'red',  [down1, down2, down3, down4] )
                #print(i, 'red')

        pygame.display.flip() 
    
    print(sys.argv)
    if len(objects) > 0:
        name = '../../test.png'
        if len(sys.argv) == 2:
            name = sys.argv[-1]
            print(name)
        pygame.image.save(screen, name)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
