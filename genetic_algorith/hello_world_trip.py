target = "hello world"

def evaluations(target,solution):
    fitness = 0
    for letter in range(len(target)):
        if solution[letter] == target[letter]:
            fitness += 1
    
    return fitness

def termination(target, solution):
    if target == solution:
        return True 
    else:
        False 

