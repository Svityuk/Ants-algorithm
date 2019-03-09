import numpy as np


def runner(n_iter ,n_ants):
    shortest_path= np.inf
    for time in range(n_iter):
        all_paths=[]
        for ant in range (n_ants):
            path= get_path()
            all_paths.append(path)

        for p in all_paths:
            if p < shortest_path:
              shortest_path=p

        for i in range(a):
            for j in range(a):
                update_pheromone(i,j,all_paths)
    return shortest_path

def update_pheromone(i,j,all_paths):
    sum=0
    for p in all_paths:
        sum += q/p
    pheromone[i][j] = sum


def get_path():
    path=0
    for i, j in gen_path():
        path += matrix[i][j]
    return path

def gen_path():
    path=[]
    start=0
    prev=start
    used =set()
    used.add(start)
    for i in range(a-1):
        new= pick_new_city(prev, used)
        path.append((prev, new))
        used.add(new)
        prev = new
    path.append((prev, start))
    return path

def pick_new_city(prev, used):
    row_ph = np.copy(pheromone[prev])
    row_ph[list(used)] = 0
    row= row_ph ** alpha *((1.0/ matrix[prev])**beta)
    n_row=row/row.sum()

    new = np.random.choice(range(a), 1, p=n_row)[0]
    return new

first_row=[int(i) for i in input().split()]
a=len(first_row)
alpha, beta = 2.5, 2.5
q = 0.95
matrix=np.zeros((a, a))
pheromone = np.ones(matrix.shape) / a
matrix[0]=first_row

for i in range(1, a):
    new_row = [int(j) for j in input().split()]
    matrix[i] = new_row

for i in range(a):
    matrix[i][i] = np.inf

print(int(runner(100,100)))