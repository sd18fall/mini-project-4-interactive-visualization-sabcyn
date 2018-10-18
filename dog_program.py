
# import pygame

#LISTS:
size_list = ['small', 'medium', 'large']
furlength_list = ['short', 'medium', 'long']
personality_list = ['friendly', 'protective']
dog_attributes = [size_list,furlength_list,personality_list]

class Characteristics():
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

    # def __str__(self):
    #     return self.breed

    def __repr__(self):
        return self.breed

Dog_list = []
for size in size_list:
    for fur in furlength_list:
        for personality in personality_list:
            Dog_list.append(Dog('Lab', Characteristics(size, fur, personality)))

def modify_list(user_input, doglist, characteristic):
    """
    >>> modify_list('small', [Dog('Yorkie',Characteristics('small','long','friendly'))], 'size')
    [Yorkie]
    >>> modify_list('large', [Dog('Yorkie',Characteristics('small','long','friendly'))], 'size')
    []
    """
    for dog in doglist:
        if getattr(dog.characteristics,characteristic) != user_input:
            doglist.remove(dog)
    return doglist

if __name__ == '__main__':
    # Yorkie = Dog('Yorkie',Characteristics('small','medium','friendly'))
    # Doglist = [Yorkie]
    # print (modify_list('large', Doglist, 'size'))

    import doctest
    doctest.run_docstring_examples(modify_list, globals(), verbose=True)
