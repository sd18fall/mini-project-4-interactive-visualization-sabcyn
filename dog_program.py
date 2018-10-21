
import pygame
import inquirer


#LISTS:
size_list = ['small', 'medium', 'large']
furlength_list = ['short', 'medium', 'long']
personality_list = ['friendly', 'protective']
dog_attributes = [size_list,furlength_list,personality_list]

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
        return self.breed

        # + ' ' + self.characteristics.size + ' ' + self.characteristics.furlength + ' ' + self.characteristics.personality

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


if __name__ == '__main__':

    print (Dog_list)

    question1 = [inquirer.List('size', message = 'Ideal Size?', choices = size_list)]
    answer1 = inquirer.prompt(question1)
    print (filter_doglist(answer1['size'], Dog_list, 'size'))

    question2 = [inquirer.List('furlength', message = 'Ideal Fur Length?', choices = furlength_list)]
    answer2 = inquirer.prompt(question2)
    print (filter_doglist(answer2['furlength'], Dog_list, 'furlength'))

    question3 = [inquirer.List('personality', message = 'Ideal Personality?', choices = personality_list)]
    answer3 = inquirer.prompt(question3)
    print (filter_doglist(answer3['personality'], Dog_list, 'personality'))



    # import doctest
    # doctest.run_docstring_examples(modify_list, globals(), verbose=True)
