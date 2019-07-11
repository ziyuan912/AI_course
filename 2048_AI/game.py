import numpy as np
from merge_game import MERGE_FUNCTIONS
from logic1 import game_state, cal_score, add_block, printgrid
from direct1 import random_direction, expectimax_direction
import matplotlib.pyplot as plt


# preparation
int2dir = ['up', 'down', 'left', 'right']

score = 0
lose = False
score = []
step = []
maxnum = []
for i in range(100):
    s = 0
    # init
    matrix = [[0 for i in range(4)] for j in range(4)]
    add_block(matrix)
    add_block(matrix)
    while True:
        #printgrid(matrix)
        if game_state(matrix) == 'lose':
            # print ('lose')
            # print ('score: ', cal_score(matrix))
            break
        direction = expectimax_direction(matrix)
        #print(direction)
        new_matrix = MERGE_FUNCTIONS[direction](matrix)
        if (matrix == new_matrix):
            continue
        matrix = new_matrix
        add_block(matrix)
        s += 1
    print(cal_score(matrix),matrix)
    score.append(cal_score(matrix))
    step.append(s)
    maxnum.append(max(matrix))

score = np.array(score)
step = np.array(step)
maxnum = np.array(maxnum)
np.save('./result/random_score',score)
np.save('./result/random_step',step)
np.save('./result/random_max',maxnum)
plt.hist(score)
plt.show()
plt.hist(step)
plt.show()
plt.hist(maxnum)
plt.show()

print ('score mean: ', np.mean(score), '\tvar: ', np.var(score))
print ('step mean: ', np.mean(step), '\tvar: ', np.var(step))
