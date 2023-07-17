
def hill_climbing(problem,state):
    ''' Returns a state as the solution of the problem '''
    ans=problem.neighbors(state)
    best=problem.value(state)
    p=state
    n=len(ans)
    for i in range(0,n):
        b=problem.value(ans[i])
        if b>=best:
            best=b
            p=ans[i]        
    return tuple(p)

def hill_climbing_random_restart(problem, limit = 10):
    state = problem.initial()
    cnt = 0
    while problem.goal_test(state) == False and cnt < limit:
        o=state
        state = hill_climbing(problem,state)
        if o==state:
            break
        cnt += 1       
    return state
