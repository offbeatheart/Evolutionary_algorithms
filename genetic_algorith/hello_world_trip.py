import random

target = "hello world"
population = []
pop_fit = []
generation = 0
# MaxGenerations = 60
# greatest_of_each_generation = []

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


class selection():
    def __init__(self):
        pass

    def tournment(self,pop,pop_size,fit):
        offspring = []

        for fight in range(pop_size):
            contestant1 = random.randrange(0,pop_size)
            contestant2 = random.randrange(0,pop_size)

            if fit[contestant1] >= fit[contestant2]:
                offspring.append(pop[contestant1])
            else:
                offspring.append(pop[contestant1])

        return offspring
    
select = selection()

population = setup(8,target)
print(population[0],target)
print(evaluations(target,population[0]))