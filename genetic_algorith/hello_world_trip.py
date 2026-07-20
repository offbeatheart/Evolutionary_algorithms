import random,time

t0 = time.time()

target = "hello world"
population_size = 4
population = []
population_fitness = []

generation = 0
MaxGenerations = 99999999999999

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

def termination(target, pop):
    for chromosome in range(len(pop)):
        if target == pop[chromosome]:
            print(pop[chromosome])
            return True 
        elif generation == MaxGenerations:
            return True  
    return False 

class selection():
    def __init__(self):
        pass

    def tournment(self,pop):
        pop_size = len(pop)
        offspring = []

        for fight in range(pop_size):
            contestant1 = random.randrange(0,pop_size)
            contestant2 = random.randrange(0,pop_size)
            if evaluations(target,pop[contestant1]) >= evaluations(target,pop[contestant2]):
                offspring.append(pop[contestant1])
            else:
                offspring.append(pop[contestant2])

        return offspring

class variation():
    def __init__(self):
        pass

    def parent_selector(self,pop): 
        pop_len = len(pop)
        parent1 = -1
        parent2  =-1
        while parent1 == parent2: # should cloning be able to occur in this population my verdict no dolly will be made another day
            parent1 = random.randrange(0,pop_len)
            parent2 = random.randrange(0,pop_len)

        return parent1 ,parent2
    
    def crossover(self,pop):

        parent1, parent2 = self.parent_selector(pop)

        pivot = random.randrange(1,len(pop))
        offspring = pop[parent1][:pivot] + pop[parent2][pivot:]

        return offspring

    def mutation(self,chromosome,mutation_rate):
        newbred =chromosome

        for allele in range(len(chromosome)):
            if random.randrange(0,100 +1) <= mutation_rate * 100:
                
                temp_letter = chr(random.randrange(ord('a'),ord('z')+2))
                if temp_letter == '{':
                    temp_letter = ' '
                newbred =  newbred[:allele] + temp_letter + newbred[allele +1:]

        return newbred
                
        
select = selection()
var = variation()

population = setup(population_size,target)

while not termination(target,population):
    population = select.tournment(population)
    next_gen = []
    for chromosome in range(population_size):
        temp =var.crossover(population)
        next_gen.append(var.mutation(temp,0.01))

    population = next_gen
    generation += 1 
    print(generation)

t1 = time.time()
print("Generations:",generation)

print("time:",t1-t0)