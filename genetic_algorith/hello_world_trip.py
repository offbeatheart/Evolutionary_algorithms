import random

target = "hello world"
population = []
population_size = 8
pop_fit = []
generation = 0
MaxGenerations = 60
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

    def tournment(self,pop,pop_size):
        offspring = []

        for fight in range(pop_size):
            contestant1 = random.randrange(0,pop_size)
            contestant2 = random.randrange(0,pop_size)

            print(pop[contestant1],pop[contestant2])

            if evaluations(target,pop[contestant1]) >= evaluations(target,pop[contestant2]):
                offspring.append(pop[contestant1])
            else:
                offspring.append(pop[contestant1])

        return offspring

class  variation():
    def __init__(self):
        pass

    def parent_selector(self,pop): # should cloning be able to occur in this population my verdict no dolly will be made another day
        pop_len = len(pop)
        parent1 = -1
        parent2  =-1
        while parent1 == parent2:
            parent1 = random.randrange(0,pop_len)
            parent2 = random.randrange(0,pop_len)
    
    def crossover(self,pop):
        pass



        
select = selection()

population = setup(population_size,target)
print(population[0],target)
print(evaluations(target,population[0]))
population = select.tournment(population,population_size)