target = "hello world"
generation = 0
MaxGenerations = 60
greatest_of_each_generation = []

def evaluations(target,solution):
    fitness = 0
    for letter in range(len(target)):
        if solution[letter] == target[letter]:
            fitness += 1
    
    return fitness

def termination(target, solution):
    if target == solution:
        return True 
    elif generation == MaxGenerations:
        return True 
    else:
        return False 
    # elif greatest_of_each_generation > 3:
    #     if abs()

