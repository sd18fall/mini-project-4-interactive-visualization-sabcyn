

import pygame
import inquirer

pygame.init()
win = pygame.display.set_mode((600,600))
win.fill((255,255,255))

#LISTS:
size_list = ['small', 'medium', 'large']
furlength_list = ['short', 'medium', 'long']
personality_list = ['friendly', 'protective']
dog_attributes = [size_list,furlength_list,personality_list]
qlist = [inquirer.List('size', message = 'Ideal Size?', choices = size_list),inquirer.List('furlength', message = 'Ideal Fur Length?', choices = furlength_list),inquirer.List('personality', message = 'Ideal Personality?', choices = personality_list)]

class Characteristics(object):
    def __init__(self, size, furlength, personality):
        self.size = size
        self.furlength = furlength
        self.personality = personality

    def __str__(self):
        return self.size + ' ' + self.furlength + ' ' + self.personality

class Dog(object):
    """  """
    def __init__(self, breed, characteristics):
        self.breed = breed
        self.characteristics = characteristics

    def __repr__(self):
        return self.breed + ' ' + self.characteristics.size + ' ' + self.characteristics.furlength + ' ' + self.characteristics.personality

Dog_list = []
Name_list = ['Lab', 'Yorkie', 'Golden', 'Pug', 'Pomeranian', 'Poodle', 'Bulldog', 'Pitbull', 'Corgi', 'CockerSpaniel', 'BorderCollie', 'Chihuahua', 'German', 'Boxer', 'Maltese', 'Husky', 'Terrier', 'Sheepdog']
i = 0
for size in size_list:
    for fur in furlength_list:
        for personality in personality_list:
                Dog_list.append(Dog(Name_list[i], Characteristics(size, fur, personality)))
                i += 1

def filter_doglist(user_input, doglist, characteristic):
    """ aslkdjfaskldjfaskldfjasdf types of input, what we would return
    >>> filter_doglist('small', [Dog('Yorkie',Characteristics('small','long','friendly'))], 'size')
    [Yorkie]
    >>> filter_doglist('large', [Dog('Yorkie',Characteristics('small','long','friendly'))], 'size')
    []
    """
    for i in range(len(doglist)-1,-1,-1):
        if getattr(doglist[i].characteristics,characteristic) != user_input:
            Dog_list.remove(doglist[i])
    return doglist

#BUTTON CLASS
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

run = True

def buttongenerator(i=0):
    win.fill((225,255,255))
    size_list = ['small', 'medium', 'large']
    furlength_list = ['short', 'medium', 'long']
    personality_list = ['friendly', 'protective']

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


if __name__ == '__main__':

    print (Dog_list)
    i = 0
    while run:
        buttonlist = buttongenerator(i)
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttonlist:
                    if b.isOver(pos):
                        user_input = b.text
                        print (filter_doglist(user_input, Dog_list, qlist[i].name))
                        if i < 3:
                            i += 1
