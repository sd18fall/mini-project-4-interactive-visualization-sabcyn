#Authors: Sabrina Pereira, Cynthia Yong

#Interactive

import pygame

class Dog(object):
    """  """
    size_list = ['small', 'medium', 'large']
    furlength_list = ['short', 'medium', 'long']
    personality_list = ['friendly', 'protective']
    dog_attributes = [size_list,furlength_list,personality_list]

    def __init__(self,breed, size, furlength, personality):
        self.breed = breed
        self.size = size
        self.furlength = furlength
        self.personality = personality

    # def __str__(self):
    #     return "Brick height=%f, width=%f, x=%f, y=%f" % (self.height,
    #                                                       self.width,
    #                                                       self.x,
    #                                                      self.y)

class Question(object):
    """  """
    question_list = ['Ideal size?', 'Ideal fur length?', 'Ideal personality?']

    def __init__(self, height, width, x, y):
        """  """
        self.curr_question = questionlist[0]
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def update(self):
        """ update the question """
        self.curr_question = self.questionlist[self.curr_question.index()+1]

    def __str__(self):
        return self.current_question

class Answer(object):
    def __int__(self, choice, height, width, x, y):
        self.choice = choice
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class DogModel(object):
    def __init__(self, size):
        self.answer = []
        self.question = 0
        self.width = size[0]
        self.height = size[1]
        self.question_width = 100
        self.question_height = 20
        self.answernumbers = 3
        self.answer_space = 10
        self.answer_width = (self.width- (2*self.answer_space))/self.answernumbers)
        self.answer_height = 20
        self.answery = 400

        for x in range(self.answer_space,
                       self.width - self.answer_space - self.answer_width,
                       self.answer_width)
                self.answer.append(Answer(self.answer.height,
                                         self.answer.width,
                                         x,
                                         self.answery))
        self.question = Question(20, 100, 200, 200)

    def update(self):
        """ """
        self.question.update()

class AnswerController(object):
    """ A controller that uses the mouse to move the paddle """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Handle the mouse event so the paddle tracks the mouse position """
        if event.type == pygame.locals.MOUSEMOTION:
            self.model.paddle.x = event.pos[0] - self.model.paddle.width/2.0

class FormViewer(object):






    # def __str__(self):
    #     output_lines = []
    #     # convert each brick to a string for outputting
    #     for brick in self.bricks:
    #         output_lines.append(str(brick))
    #     output_lines.append(str(self.paddle))
    #     # print one item per line
    #     return "\n".join(output_lines)
