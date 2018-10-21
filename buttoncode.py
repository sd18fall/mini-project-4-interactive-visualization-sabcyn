

import pygame

pygame.init()
win = pygame.display.set_mode((600,600))
win.fill((255,255,255))

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 15)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def redrawWindow():
    win.fill((225,255,255))
    greenButton1.draw(win, (0,0,0))
    greenButton2.draw(win, (0,0,0))
    greenButton3.draw(win, (0,0,0))
    questionbutton.draw(win, (0,0,0))

run = True

greenButton1 = button((0,255,0), 100,225,100, 75, 'Ideal Size? :)')
greenButton2 = button((0,255,0), 250,225,100, 75, 'Ideal Furlength? :D')
greenButton3 = button((0,255,0), 400,225,100, 75, 'Ideal Personality? :]')
questionbutton = button((0,255,0), 200,100,100, 50, 'Question 1')

while run:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if greenButton1.isOver(pos):
        #         print ('clicked')

        if event.type == pygame.MOUSEMOTION :
            if greenButton1.isOver(pos):
                greenButton1.color = (225,0,0)
            else:
                greenButton1.color = (0,225,0)






# counter = 0
# def counter_label(label):
#   counter = 0
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
#
# def print2():
#     print ('helloooooo')
#
# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="dark green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=print2)
# button.pack()
# root.mainloop()


# def button():
#
#     intro = True
#
#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         gameDisplay.fill(white)
#         largeText = pygame.font.Font('freesansbold.ttf',115)
#
#         pygame.draw.rect(gameDisplay, green,(150,450,100,50))
#         pygame.draw.rect(gameDisplay, red,(550,450,100,50))
#
#         mouse = pygame.mouse.get_pos()
#
#         if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
#             pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
#         else:
#             pygame.draw.rect(gameDisplay, green,(150,450,100,50))
#
#         smallText = pygame.font.Font("freesansbold.ttf",20)
#         textSurf, textRect = text_objects("SMALL", smallText)
#         textRect.center = ( (150+(100/2)), (450+(50/2)) )
#         gameDisplay.blit(textSurf, textRect)
#
#
#         pygame.draw.rect(gameDisplay, red,(550,450,100,50))
#
#         pygame.display.update()
#         clock.tick(15)
#
#
#
#         # if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
#         #     pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
#         # print ("CHANE")
#         # else:
#         #     pygame.draw.rect(gameDisplay, green,(150,450,100,50))
#         # pygame.draw.rect(gameDisplay, red,(550,450,100,50))
#         # pygame.display.update()
#
#
#
#
#
#
#
#
#
#
#         # #print(mouse)
#         #     # This block is executed once for each MOUSEBUTTONDOWN event.
#         # if event.type == pygame.MOUSEBUTTONDOWN:
#         #     # 1 is the left mouse button, 2 is middle, 3 is right.
#         #     if event.button == 1:
#         #         # `event.pos` is the mouse position.
#         #         if button.collidepoint(event.pos):
#         #             # Increment the number.
#         #             number += 1
#         # pygame.display.update()
#         # if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
#         #     pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
#         # else:
#         #     pygame.draw.rect(gameDisplay, green,(150,450,100,50))
#         # pygame.draw.rect(gameDisplay, green,(550,450,100,50))
#         # pygame.display.update()
#
# # def loop():
# #     # clock = pygame.time.Clock()
# #     number = 0
# #     # The button is just a rect.
# #     button = pygame.Rect(0, 100, 200, 200)
# #     done = False
# #     while not done:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 done = True
# #             # This block is executed once for each MOUSEBUTTONDOWN event.
# #             elif event.type == pygame.MOUSEBUTTONDOWN:
# #                 # 1 is the left mouse button, 2 is middle, 3 is right.
# #                 if event.button == 1:
# #                     # `event.pos` is the mouse position.
# #                     if button.collidepoint(event.pos):
# #                         # Increment the number.
# #                         number += 1
#
#         # screen.fill(WHITE)
#         # pygame.draw.rect(screen, GRAY, button)
#         # text_surf = FONT.render(str(number), True, BLACK)
#         # You can pass the center directly to the `get_rect` method.
#         # text_rect = text_surf.get_rect(center=(width/2, 30))
#         # screen.blit(text_surf, text_rect)
#         # pygame.display.update()
#
#
#
# pygame.init()
#
# display_width = 800
# display_height = 600
#
# white = (255,255,255)
# red = (200,0,0)
# green = (0,200,0)
#
# bright_red = (255,0,0)
# bright_green = (0,255,0)
#
# gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('YOUR IDEAL DOG TEST')
# button()
