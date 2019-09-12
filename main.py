import pygame as pg
import maze
import thorpy

pg.init()
pg.mixer.init()

WIDTH = 400
HEIGHT = 500
FPS = 120
WHITE = (255,255,255)
GREY = (100,100,100)


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("A* algorithm by TUAHIVAA Guillaume")

clock = pg.time.Clock()





def myFunction():
    print("button try")




screen.fill(WHITE)
done = False
myRect = maze.Maze(screen)
# print(myRect.group_of_cells)
counter = 0
while not done:
    clock.tick(FPS)

    for event in pg.event.get():

        if event.type == pg.QUIT:
            done = True

        #if left click is pressed then execute
        if pg.mouse.get_pressed()[0]:
            mouseX, mouseY = pg.mouse.get_pos()
            print( int(mouseX/100), int(mouseY/100) )
            custom_cell = myRect.group_of_cells[int(mouseX/100)][int(mouseY/100)]
            print("unique ID is: " + str(custom_cell.unique_ID) )

            custom_cell.change_color(screen, (0,0,0), ((int(mouseX/100))*100),((int(mouseY/100))*100) )
            custom_cell.build_wall()
            custom_cell.cancel()

        if pg.mouse.get_pressed()[2]:
            mouseX, mouseY = pg.mouse.get_pos()
            print( int(mouseX/100), int(mouseY/100) )
            custom_cell = myRect.group_of_cells[int(mouseX/100)][int(mouseY/100)]
            print("unique ID is: " + str(custom_cell.unique_ID) )

            custom_cell.change_color(screen, (255,255,255), ((int(mouseX/100))*100),((int(mouseY/100))*100) )
            custom_cell.destroy_wall()
            custom_cell.cancel()



        if pg.mouse.get_pressed()[1]:

            # STARTER!
            if counter == 0:
                mouseX, mouseY = pg.mouse.get_pos()
                print(int(mouseX / 100), int(mouseY / 100))
                custom_cell = myRect.group_of_cells[int(mouseX / 100)][int(mouseY / 100)]
                print("unique ID is: " + str(custom_cell.unique_ID))

                custom_cell.change_color(screen, (0, 125, 0), ((int(mouseX / 100)) * 100),
                                         ((int(mouseY / 100)) * 100))
                custom_cell.destroy_wall()
                custom_cell.Source()


                counter += 1


            #TARGET!
            elif counter == 1:
                mouseX, mouseY = pg.mouse.get_pos()
                print(int(mouseX / 100), int(mouseY / 100))
                custom_cell = myRect.group_of_cells[int(mouseX / 100)][int(mouseY / 100)]
                print("unique ID is: " + str(custom_cell.unique_ID))

                custom_cell.change_color(screen, (255, 255, 0), ((int(mouseX / 100)) * 100),((int(mouseY / 100)) * 100))
                custom_cell.destroy_wall()
                custom_cell.Target()
                counter += 1
                # counter = 0

    pg.display.update()
    thorpy.make_button("test", myFunction)





pg.quit()
