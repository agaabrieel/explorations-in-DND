import numpy as np
import matplotlib.pyplot as plt

def gen_data(n):

    data1, data2, data3 = [], [], []
    for i in range(n):
        v1 = np.random.randint(1, 21)
        v2 = np.random.randint(1, 21, 2)
        v3 = np.random.randint(1, 21, 2)
        data1.append(v1)
        data2.append(max(v2))
        data3.append(min(v3))
    
    return data1, data2, data3

data1, data2, data3 = gen_data(50_000)
bins = np.linspace(0, 21, 21)

fig, axs = plt.subplots(1)

plt.hist([data1, data2, data3], bins, label = ['1d20', '1d20 c/ vantagem', '1d20 c/ desvantagem'], density = True)
plt.axvline(np.average(data1), color = 'r', label = 'Média de 1d20')
plt.axvline(np.average(data2), color = 'g', label = 'Média de 1d20 com vantagem')
plt.axvline(np.average(data3), color = 'y', label = 'Média de 1d20 com desvantagem')
plt.legend(loc = 'upper left')

plt.show()