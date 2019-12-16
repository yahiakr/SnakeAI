def obstacles(body):
    obstacles = [0,0,0,0]
    for i, c in enumerate(body):
        if c.pos[0] <= 0 or (neighbor(c.pos,(-1,0)) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[3] = 1
        if c.pos[0] >= c.rows-1 or (neighbor(c.pos,(1,0)) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[2] = 1
        if c.pos[1] >= c.rows-1 or (neighbor(c.pos,(0,1)) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[1] = 1
        if c.pos[1] <= 0 or (neighbor(c.pos,(0,-1)) in list(map(lambda z:z.pos,body[i+1:]))) : obstacles[0] = 1
        break
    return obstacles

def neighbor(pos,dirc):
    return (pos[0]+dirc[0], pos[1]+dirc[1])

def control(snake,move):
    moves = [[0, -1],[0, 1],[1, 0],[-1, 0]]
    snake.dirnx = moves[move][0]
    snake.dirny = moves[move][1]
    snake.turns[snake.head.pos[:]] = [snake.dirnx, snake.dirny]

