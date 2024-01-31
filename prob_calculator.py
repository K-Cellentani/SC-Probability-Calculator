import random
from copy import deepcopy
from collections import Counter

class Hat:
  def __init__(self, **input):
    self.contents = []
    for i in input.items():
      color = i[0]
      freq = i[1]
      for _ in range(freq):
        self.contents.append(color)
    self.hat_num_balls = len(self.contents) + 1

  def draw(self, num_balls_drawn):
    if num_balls_drawn > self.hat_num_balls:
      return 'all the balls'
    elif num_balls_drawn == self.hat_num_balls:
      drawn_balls = self.contents
      return drawn_balls
    else: 
      drawn_balls = random.sample(self.contents, num_balls_drawn)
      for ball in drawn_balls:
          self.contents.remove(ball)
      return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  correct = 0
  expected_ball_contents = []
  for i in expected_balls.items():
    color = i[0]
    freq = i[1]
    for i in range(freq):
      expected_ball_contents.append(color)
  
  def contains(l1, l2):
    return not (Counter(l2) - Counter(l1))
  
  for _ in range(num_experiments):
    hat_copy = deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    if contains(drawn, expected_ball_contents):
      correct += 1

  probability = correct / num_experiments
  return probability 
