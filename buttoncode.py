

import pygame
import inquirer
import dog_program

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

# def redrawWindow():
#     win.fill((225,255,255))
#     greenButton1.draw(win, (0,0,0))
#     greenButton2.draw(win, (0,0,0))
#     greenButton3.draw(win, (0,0,0))
#     questionbutton.draw(win, (0,0,0))

run = True

def buttongenerator(i=0):
    win.fill((225,255,255))
    size_list = ['small', 'medium', 'large']
    furlength_list = ['short', 'medium', 'long']
    personality_list = ['friendly', 'protective']

    qlist = [inquirer.List('furlength', message = 'Ideal Fur Length?', choices = furlength_list)]
    question = qlist[i].message


    questionbutton = button((0,255,0),275,50,100, 75, question)
    questionbutton.draw(win, (0,0,0))
    incrementx = 0
    buttonlist = []
    for choice in qlist[i].choices:
        b = button((0,255,0), 100 + incrementx, 225, 100, 75, choice)
        buttonlist.append(b)
        b.draw(win, (0,0,0))
        incrementx += 150
    return buttonlist

while run:
    buttonlist = buttongenerator()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()b
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttonlist:
                if b.isOver(pos):
                    user_input = b.text
                    print (user_input)
                    print (filter_doglist(user_input, Dog_list, 'furlength'))


        # if event.type == pygame.MOUSEMOTION :
        #     if greenButton1.isOver(pos):
        #         greenButton1.color = (225,0,0)
        #     else:
        #         greenButton1.color = (0,225,0)


if __name__ == '__main__':
