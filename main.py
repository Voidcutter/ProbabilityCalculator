import copy
import random
# Consider using the modules imported above.

class Hat:
    # get different amounts of balls of different colours
    def __init__(self, **kwargs):
        # the 'hat'
        self.contents = []
        self.contents_clone = []
        for ball, num in kwargs.items():
            # multiplying the ball color by the amount
            # output of (white=1, black=2, blue=0) will be ['white', 'black', 'black']
            self.contents += [ball] * num
            # create the same list for a refill
            self.contents_clone += [ball] * num
       
    def draw(self, num):
        # num = number of balls picked
        if num > len(self.contents_clone):
            return self.contents
        elif len(self.contents) >= num:
            picked = random.sample(self.contents, num)
            for i in picked:
                self.contents.remove(i)
            return picked
        else: 
            self.contents = copy.deepcopy(self.contents_clone)
            return self.draw(num)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    def check(exp_balls, act_balls):
        for ball in exp_balls:
            if act_balls.count(ball) >= exp_balls.count(ball):
                continue
            else:
                return False
        return True

    exp_balls = []
    # expected balls preparation
    for ball, num in expected_balls.items():
            # multiplying the ball color by the amount
            exp_balls += [ball] * num

    m = 0 # number of matches

    for _ in range(num_experiments):

        act_balls = hat.draw(num_balls_drawn)

        if check(exp_balls, act_balls):
            m += 1             

    return m / num_experiments