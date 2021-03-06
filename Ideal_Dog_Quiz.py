"""
FINDING YOUR IDEAL DOG
An interactive quiz for finding your ideal dog!

Authors: Cynthia Yong and Sabrina Pereira
"""
import pygame
import inquirer

#Initialize the pygame window:
pygame.init()
win = pygame.display.set_mode((600,600))
win.fill((43, 226, 229))

#Initialize lists of dog attributes/answers, and questions as inquirer List objects
size_list = ['Small', 'Medium', 'Large']
furlength_list = ['Short', 'Medium', 'Long']
personality_list = ['Friendly', 'Laid-back', 'Active']
qlist = [inquirer.List('size', message = 'Ideal Size?', choices = size_list),inquirer.List('furlength', message = 'Ideal Fur Length?', choices = furlength_list),inquirer.List('personality', message = 'Ideal Personality?', choices = personality_list)]

#Varibles for Quiz stages
Beginning = True
Middle = False
End = False


class Characteristics:
    """
    Contains information about size, fur length, and personality.
    Takes size, furlength, and personality as strings.
    """
    def __init__(self, size, furlength, personality):
        self.size = size
        self.furlength = furlength
        self.personality = personality

    def __str__(self):
        return self.size + ' ' + self.furlength + ' ' + self.personality

class Dog:
    """
    Represents a type of dog. Each dog object has a breed, characteristics object, and an associated photo.
    """
    def __init__(self, breed, characteristics, photofile= None):
        self.breed = breed
        self.characteristics = characteristics
        self.photofile = photofile

    def __repr__(self):
        return self.breed + ' ' + self.characteristics.size + ' ' + self.characteristics.furlength + ' ' + self.characteristics.personality


def filter_doglist(user_input, doglist, characteristic):
    """
    Takes in a user's prefrence, a list of dogs to narrow down, and the characteristic currently being looked at.
    Returns a list of dogs that match the user's preference.

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
    """
    Creates an object that contains information about a desired button's color, size and text.
    Color to be inputed as a triple indicating a decimal code; the x, y, width and height values should be integers.
    Contains methods that allow the button to be drawn on the screen and check if it has been clicked.
    """
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
            #Set font and size of button text, display centered
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


def buttongenerator(i=0):
    """
    Generates and displays buttons with a question and its corresponding answer choices.
    Takes in the index for the desired question from the question list qlist.
    Returns a list of the generated button objects for the answer choices.
    """
    win.fill((43, 226, 229))

    question = qlist[i].message
    questionbutton = button((184, 231, 242),225,150,150, 75, question)
    questionbutton.draw(win, (0,0,0))

    buttonlist = []
    incrementx = 0
    for choice in qlist[i].choices:
        b = button((184, 231, 242), 100 + incrementx, 300, 100, 75, choice)
        buttonlist.append(b)
        b.draw(win, (0,0,0))
        incrementx += 150
    return buttonlist


def display_photos(doglist):
    """
    Takes in a list containing 1, 2, or 3 dogs and then displays their associated photos.
    """
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



#Creating Dog objects and adding them to a list as possibilities for quiz results

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




if __name__ == '__main__':

    #Intializes screen and index for question in qlist
    win.fill((201, 177, 237))
    i = 0

    #Shows beginning screen
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

    #Shows the question sequence
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

            #Advances to next question if the user clicks on an answer choice, proceeds to end sequence if finished of if no dogs are applicable
            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttonlist:
                    if b.isOver(pos):
                        user_input = b.text
                        filter_doglist(user_input, Dog_list, qlist[i].name)
                        if i < len(qlist):
                            i += 1
                            if i == len(qlist):
                                Middle = False
                                if Dog_list == []:
                                    SadEnd = True
                                else:
                                    End = True

    win.fill((201, 177, 237))
    #Shows the end results
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

    #Ends sequence if no dogs match the user's criteria
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
