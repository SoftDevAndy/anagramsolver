# Andrew Sweeney
# G00237144
# February 2016

# A small script that creates a graph from the results of running the program a certain amount of times


import matplotlib.pyplot as plt
import solver

count = 1
iterations = []
time = []

while count < 10:

    kv = solver.fullprogram()

    iterations.append(kv['Time'])
    time.append(count)

    if count % 10 == 0:
        print(count)

    count += 1

plt.plot(time, iterations)
plt.show()
