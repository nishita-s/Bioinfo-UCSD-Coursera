edges = []

with open('/home/nishita/Downloads/dataset_203_6.txt','r+') as f:
    lines = [line[:-1] for line in f]

# To get all the edges (adjacencies) listed in list edges
for line in lines:
    line = ''.join(line.split(":")).split(" ")
    if len(line) == 2:
        edges.append(line)
    else:
        for i in range(1,len(line)):
            edges.append([line[0],line[i]])

nodes = []
path = []

def out_degree(o, arr):
    count = 0
    for ar in arr:
        if (ar[1]) == o:
            count += 1

    return count

def in_degree(i, arr):
    count = 0
    for ar in arr:
        if (ar[0]) == i:
            count += 1
    return count

for edge in edges:
    if out_degree(edge[0],edges) < in_degree(edge[0],edges):
        start_index = edge[0]
        break

for edge in edges:
    if out_degree(edge[1],edges) > in_degree(edge[1],edges):
        end_index = edge[1]
        break

edges.append([start_index,end_index])

nodes.append(start_index) #assigning the starting node
while(len(nodes)):
    exists = 0
    for edge in edges:
        if edge[0] == nodes[len(nodes)-1]:
            nodes.append(edge[1])
            edges.remove(edge)
            exists = 1
            break
    if exists == 0:
        x = nodes.pop()
        path.append(x)

path.reverse()
path.pop(1)
for x in path:
    print(x, end=" ")
