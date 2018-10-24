

import pygame
import inquirer

pygame.init()
win = pygame.display.set_mode((600,600))
win.fill((43, 226, 229))

#LISTS:
size_list = ['Small', 'Medium', 'Large']
furlength_list = ['Short', 'Medium', 'Long']
personality_list = ['Friendly', 'Laid-back', 'Active']
dog_attributes = [size_list,furlength_list,personality_list]
qlist = [inquirer.List('size', message = 'Ideal Size?', choices = size_list),inquirer.List('furlength', message = 'Ideal Fur Length?', choices = furlength_list),inquirer.List('personality', message = 'Ideal Personality?', choices = personality_list)]

Beginning = True
Middle = False
End = False

class Characteristics(object):
    def __init__(self, size, furlength, personality):
        self.size = size
        self.furlength = furlength
        self.personality = personality

    def __str__(self):
        return self.size + ' ' + self.furlength + ' ' + self.personality

class Dog(object):
    """  """
    def __init__(self, breed, characteristics, photofile= None):
        self.breed = breed
        self.characteristics = characteristics
        self.photofile = photofile

    def __repr__(self):
        return self.breed + ' ' + self.characteristics.size + ' ' + self.characteristics.furlength + ' ' + self.characteristics.personality

Lab = Dog('Lab', Characteristics('Large', 'Short', 'Friendly'), 'Lab.jpeg')
Yorkie = Dog('Yorkie', Characteristics('Small', 'Long', 'Friendly'), 'Yorkie.jpeg')
Golden_Retriever = Dog('Golden Retriever', Characteristics('Large', 'Long', 'Friendly'), 'Golden_Retriever.jpeg')
Pug = Dog('Pug', Characteristics('Small', 'Short', 'Laid-back'), 'Pug.jpeg')
Pomeranian = Dog('Pomeranian', Characteristics('Small', 'Long', 'Active'), 'Pomeranian.jpeg')
Poodle = Dog('Poodle', Characteristics('Large', 'Medium', 'Friendly'), 'Poodle.jpeg')
Bulldog = Dog('Bulldog', Characteristics('Medium', 'Short', 'Laid-back'), 'Bulldog.jpeg')
Pitbull = Dog('Pitbull', Characteristics('Large', 'Short', 'Active'), 'Pitbull.jpeg')
Corgi = Dog('Corgi', Characteristics('Medium', 'Long', 'Friendly'), 'Corgi.jpeg')
Cocker_Spaniel = Dog('Cocker-Spaniel', Characteristics('Medium', 'Long', 'Laid-back'), 'Cocker_Spaniel.jpeg')
Border_Collie = Dog('Border Collie', Characteristics('Large', 'Long', 'Active'), 'Border_Collie.jpeg')
Chihuahua = Dog('Chihuahua', Characteristics('Small', 'Short', 'Active'), 'Chihuahua.jpeg')
German_Shepard = Dog('German Shepard', Characteristics('Large', 'Short', 'Active'), 'German_Shepard.jpeg')
Boxer = Dog('Boxer', Characteristics('Large', 'Short', 'Active'), 'Boxer.jpeg')
Maltese = Dog('Maltese', Characteristics('Small', 'Long', 'Laid-back'), 'Maltese.jpeg')
Husky = Dog('Husky', Characteristics('Large', 'Medium', 'Active'), 'Husky.jpeg')
Terrier = Dog('Terrier', Characteristics('Small', 'Medium', 'Active'), 'Terrier.jpeg')
Sheepdog = Dog('Sheepdog', Characteristics('Large', 'Medium','Active'),'Sheepdog.jpeg')

Dog_list = [Lab, Yorkie, Golden_Retriever, Pug, Pomeranian, Poodle, Bulldog, Pitbull, Corgi, Cocker_Spaniel, Border_Collie, Chihuahua, German_Shepard, Boxer, Maltese, Husky, Terrier, Sheepdog]

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

def display_photos(doglist):
    i = 0
    if len(doglist) == 1:
        win.blit(pygame.image.load(doglist[0].photofile),(225,330))
        pygame.display.flip()

    if len(doglist) == 2:
        for dog in doglist:
            win.blit(pygame.image.load(dog.photofile),(125+i,330))
            pygame.display.flip()
            i += 200

    if len(doglist) == 3:
        for dog in doglist:
            win.blit(pygame.image.load(dog.photofile),(25+i,330))
            pygame.display.flip()
            i += 200

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

            font = pygame.font.SysFont('comicsans', 21)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def __repr__(self):
        return self.text


run = True

def buttongenerator(i=0):
    win.fill((43, 226, 229))

    question = qlist[i].message

    questionbutton = button((184, 231, 242),225,150,150, 75, question)
    questionbutton.draw(win, (0,0,0))
    incrementx = 0

    buttonlist2 = []
    for choice in qlist[i].choices:
        b = button((184, 231, 242), 100 + incrementx, 300, 100, 75, choice)
        buttonlist2.append(b)
        b.draw(win, (0,0,0))
        incrementx += 150
    return buttonlist2


if __name__ == '__main__':

    print (Dog_list)
    i = 0
    win.fill((201, 177, 237))
    while Beginning:
        pygame.display.update()

        Page1 = button((184, 231, 242), 25, 200, 555, 75, text='READY TO DISCOVER YOUR IDEAL DOG? Just answer the following questions!')
        Start = button((184, 231, 242), 250, 330, 100, 50, text='LETS DO IT !')
        Page1.draw(win, (0,0,0))
        Start.draw(win, (0,0,0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Start.isOver(pos):
                    Beginning = False
                    Middle = True
    while Middle:
        buttonlist = buttongenerator(i)
        pygame.display.update()

        if Dog_list == []:
            Middle = False
            SadEnd = True

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(buttonlist)
                for b in buttonlist:
                    if b.isOver(pos):
                        user_input = b.text
                        print (filter_doglist(user_input, Dog_list, qlist[i].name))
                        if i < 3:
                            i += 1
                            if i == 3:
                                Middle = False
                                if Dog_list == []:
                                    SadEnd = True
                                else:
                                    End = True

    win.fill((201, 177, 237))

    while End:
        pygame.display.update()

        PageEnd = button((184, 231, 242), 30, 100, 550, 75, 'YOUR IDEAL DOG/DOGS:')

        dogs = ''
        for dog in Dog_list:
            dogs = dogs + dog.breed + '! '

        End = button((184, 231, 242), 175, 230, 250, 50, dogs)
        PageEnd.draw(win, (0,0,0))
        End.draw(win, (0,0,0))
        display_photos(Dog_list)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
    while SadEnd:
        pygame.display.update()

        PageEnd = button((184, 231, 242), 30, 150, 550, 75, text='No dogs match. You can check out cats! ;)')
        PageEnd.draw(win, (0,0,0))
        win.blit(pygame.image.load('SadDog.jpg'),(225,275))
        pygame.display.flip()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
