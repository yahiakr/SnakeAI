from scipy.spatial import distance

moves = [(0, -1),(0, 1),(1, 0),(-1, 0)]
d_name = ['Up','Down','Right','Left']

def neighbor(pos,dirc):
    return (pos[0]+dirc[0], pos[1]+dirc[1])

def obstacles(body):
    obstacles = [0,0,0,0]
    for i, c in enumerate(body):
        if c.pos[0] <= 0 or (neighbor(c.pos,moves[3]) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[3] = 1
        if c.pos[0] >= c.rows-1 or (neighbor(c.pos,moves[2]) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[2] = 1
        if c.pos[1] >= c.rows-1 or (neighbor(c.pos,moves[1]) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[1] = 1
        if c.pos[1] <= 0 or (neighbor(c.pos,moves[0]) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[0] = 1
        break
    return obstacles

def distances(head,x):
    distances = []
    for i in range(len(moves)):
        distances.append(round(distance.euclidean(neighbor(head,moves[i]) , x),4))

    return distances

def turn(pos,move):
    if pos[1] == 0:
        tmp = move * -1
        return (pos[0] * tmp,0)
    else : 
        return (0,pos[1] * move)

def control(snake,move):
    if move == 0 : return
    else :
        if move == 2 : move = -1
        m = turn((snake.dirny,snake.dirnx),move)
        snake.dirnx = m[0]
        snake.dirny = m[1]
        snake.turns[snake.head.pos[:]] = [snake.dirnx, snake.dirny]

