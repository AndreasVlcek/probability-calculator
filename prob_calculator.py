import random
import copy
from collections import Counter


class Hat:

  def __init__(self, **kwargs):
    self.kwargs = kwargs
    self.contents = []
    for key, value in self.kwargs.items():
      #print(key, '->', value)
      for i in range(0, value):
        self.contents.append(key)

  def draw(self, number_of_balls):
    drawn_balls = []

    if number_of_balls > len(self.contents):
      drawn_balls = self.contents
      self.contents = []
    else:
      i = 0
      while i < number_of_balls:
        ball = random.choice(self.contents)
        self.contents.remove(ball)

        drawn_balls.append(ball)
        i += 1

    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  match = 0

  n = 0
  while n < num_experiments:

    # always make a copy of the orginal hat
    test_hat = copy.deepcopy(hat)

    # draw balls and turn list into a dictionary
    drawn_balls = test_hat.draw(num_balls_drawn)
    drawn_balls_dict = dict(Counter(drawn_balls))

    found = 0
    for k, v in expected_balls.items():
      if k in drawn_balls_dict:
        # at least!
        if (drawn_balls_dict.get(k) >= v):
          found += 1
      else:
        break

    if found == len(expected_balls):
      match += 1

    n += 1

  return match / num_experiments
