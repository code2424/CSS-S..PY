import time
import datetime
import sys

start = time.time()
print(datetime.datetime.now())

# Reading the input file and parsing it into two lists
data_set_u = []
data_set_v = []
file_path = r'C:\Users\chara\Downloads\SCC\scc.txt'  # Full path to the file
with open(file_path) as f:
    for ln in f:
        if len(ln.strip()) > 0:  # Adjusted to strip whitespace and check if line is not empty
            u, v = map(int, ln.split())
            data_set_u.append(u)
            data_set_v.append(v)

print('Open file time: {:.2f}s'.format(time.time() - start))
print(datetime.datetime.now())

# Rest of your code..

# Setting recursion limit based on the size of the graph
sys.setrecursionlimit((max(data_set_u + data_set_v) + len(data_set_u)) * 100)

def DFS_Loop(nodes, edges_u, edges_v):
    num = max(edges_u + edges_v)
    start_time_DFS_Loop = time.time()
    global t, s, visited, leader, f
    t = 0
    s = None
    visited = [False] * num
    leader = [None] * num
    f = [None] * num

    for i in range(num, 0, -1):
        if not visited[i - 1]:
            s = i
            DFS(i, edges_u, edges_v)
    print('End of DFS_Loop() time: {:.2f}s'.format(time.time() - start_time_DFS_Loop))
    print('End of DFS_Loop() whole time: {:.2f}s'.format(time.time() - start))

def DFS(node, edges_u, edges_v):
    global t, s
    visited[node - 1] = True
    leader[node - 1] = s
    arc = [edges_v[i] for i, x in enumerate(edges_u) if x == node]
    for i in arc:
        if not visited[i - 1]:
            DFS(i, edges_u, edges_v)
    t += 1
    f[node - 1] = t

DFS_Loop(data_set_u, data_set_u, data_set_v)
print('DFS_Loop time: {:.2f}s'.format(time.time() - start))

# Reversing the graph
rev_u, rev_v = data_set_v, data_set_u
new_u = [None] * len(rev_u)
new_v = [None] * len(rev_v)

for i, val in enumerate(f):
    for i_v, val_v in enumerate(rev_v):
        if val_v == i + 1:
            new_v[i_v] = val
    for i_u, val_u in enumerate(rev_u):
        if val_u == i + 1:
            new_u[i_u] = val

data_set_u = new_u
data_set_v = new_v

print('Reverse data time: {:.2f}s'.format(time.time() - start))

DFS_Loop(data_set_u, data_set_u, data_set_v)
print('DFS_Loop time: {:.2f}s'.format(time.time() - start))

# Calculating the size of strongly connected components (SCCs)
count_list = [0] * len(leader)
i_count_list = 0

while leader:
    count_list[i_count_list] = leader.count(leader[0])
    indices = [i for i, x in enumerate(leader) if x == leader[0]]
    for _ in indices:
        leader.remove(leader[0])
    i_count_list += 1

print('Calc time: {:.2f}s'.format(time.time() - start))

sorted_count_list = sorted(count_list, key=int, reverse=True)
print(sorted_count_list[:5])
print(datetime.datetime.now())
