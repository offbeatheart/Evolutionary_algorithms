import random

target = "hello world"
alphabet = []
population = []
generation = 0
MaxGenerations = 60
greatest_of_each_generation = []

def setup(population_size,target): # specific to the problem at hand 
    temp_population = []

    for solution in range(population_size):
        solution = ""
        for letter in range(len(target)):
            temp_letter = chr(random.randrange(ord('a'),ord('z')+2))
            if temp_letter == '{':
                temp_letter = ' '
            solution += temp_letter

        temp_population.append(solution)

    return temp_population

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

print(setup(8,target))