import copy
import random

class Hat:
    def __init__(self, **kwargs):

        _contents = [[f'{key}' for _ in range(value)]\
                    for key, value in kwargs.items()]

        self.contents = sum(_contents, [])
    
    def draw(self, n_draws):
        choices = []
        if n_draws > len(self.contents):
            choices += self.contents
            self.contents.clear()
            return choices

        choices = random.sample(self.contents, n_draws)
        for choice in choices:
            self.contents.remove(choice)
        return choices


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    list_experiments = [copy.deepcopy(hat).draw(num_balls_drawn) \
                        for _ in range(num_experiments) ]
 

    sucess_list = [ all([True if value <= contents.count(key) else False \
                    for key, value in expected_balls.items() ] ) \
                    for contents in list_experiments]


    probability = sum(sucess_list)/num_experiments
    return probability

hat = Hat(red = 3, blue = 3)
