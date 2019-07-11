import matplotlib.pyplot as plt
import numpy as np

methods = ['weight', 'smooth', 'space',
           'adjacent']
# methods = ['greedy', '2_greedy', '3_greedy']

score = []
step = []
best = []

for m in methods:
    score.append(np.load('result/'+m+'_score.npy'))
    step.append(np.load('result/'+m+'_step.npy'))
    best.append(np.load('result/'+m+'_max.npy'))

"""bins = np.linspace(0, 70000, 10)
plt.xlabel("game score")
plt.hist(score, bins, label=methods)
plt.legend(methods, loc='best')
plt.savefig("heuristic_score.png")"""


bins = np.linspace(0, 2400, 8)
plt.xlabel("number of step")
plt.hist(step, bins, label=methods)
plt.legend(methods, loc='best')
plt.savefig("heuristic_step.png")

_4096 = np.zeros(len(methods))
_2048 = np.zeros(len(methods))
_1024 = np.zeros(len(methods))
_512 = np.zeros(len(methods))
_256 = np.zeros(len(methods))
print(best[0][0])
for i in range(100):
    for j in range(len(methods)):
        if max(best[j][i]) == 4096:
            _4096[j] += 1
        elif max(best[j][i]) == 2048:
            _2048[j] += 1
        elif max(best[j][i]) == 1024:
            _1024[j] += 1
        elif max(best[j][i]) == 512:
            _512[j] += 1
        else:
            _256[j] += 1

print ("%10s"%"methods"+"\t4096\t2048\t1024\t512\t256-\tscore\t\tstep")
for i in range(len(methods)):
    print ("%10s"%methods[i]+"\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.2f\t%.2f" % (
            _4096[i],_2048[i], _1024[i], _512[i],
            _256[i], np.mean(score[i]), np.mean(step[i])))
