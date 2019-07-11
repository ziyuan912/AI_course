import numpy as np


def game_state(mat):
    """for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'"""
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for i in range(len(mat)):  # check for any zero entries
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'


score_list = {
    0: 0, 2: 0, 4: 4, 8: 16, 16: 48, 32: 128, 64: 320, 128: 768,
    256: 1792, 512: 4096, 1024: 9216, 2048: 20480, 4096: 45056
}


def cal_score(mat):
    score = 0
    for i in range(4):
        for j in range(4):
            score += score_list[mat[i][j]]
    return score


def printgrid(mtx):
    for i in range(4):
        print (mtx[i])
    print ('\n')


def add_block(mtx):
    new_block = 2 if np.random.random_sample() > 0.1 else 4
    place = []
    for i in range(4):
        for j in range(4):
            if mtx[i][j] == 0:
                place.append([i, j])
    new_place = place[np.random.randint(len(place))]
    mtx[new_place[0]][new_place[1]] = new_block
    return mtx
