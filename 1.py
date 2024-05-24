from collections import deque

def water_jug_bfs(jug1_cap,jug2_cap,target):
    visited=set()
    path=[]
    q=deque()
    q.append((0,0))

    while q:
        state=q.popleft()
        if state in visited:
            continue
        visited.add(state)
        path.append(state)
        jug1,jug2=state
        if jug1==target or jug2==target:
            path.append(state)
            printsteps(path)
            return True
        q.append((jug1_cap,jug2))
        q.append((jug1,jug2_cap))
        q.append((0,jug2))
        q.append((jug1,0))
        pour_to_jug2=min(jug1, jug1_cap-jug2)
        q.append((jug1-pour_to_jug2,jug2+pour_to_jug2))
        pour_to_jug1=min(jug2,jug2_cap-jug1)
        q.append((jug1+pour_to_jug1,jug2-pour_to_jug1))
    print("no solution")
    return False
def printsteps(l):
    for i in l:
        print(i)
jug1_cap= 5
jug2_cap = 3
target = 2

water_jug_bfs(jug1_cap, jug2_cap, target)







