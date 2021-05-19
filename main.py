from kraken_api.kraken_service import KrakenService
from neural_network.organism import Organism
from neural_network.ecosystem import Ecosystem
import numpy as np
import json
from helpers.logger import Logger
import time

service = KrakenService()

# The function for creating the initial population
organism_creator = lambda : Organism([9, 16, 16, 16, 3], output='softmax')

def simulate_and_evaluate(organism, trials=1):
    for i in range(trials):
        #get current data to run the trial on
        resp = service.getTicker()
        #print to console 
        print("Running Generation: " + str(i)+" of "+str(trials)+" using the following as input: ")
        print(resp)
        #run the trial 
        action = organism.predict(np.array([resp.organism_input]))
        #print the action
        print("Actions for trial " + str(i)+": \n"+ str(action))
        action = np.argmax(action.flatten())
        #the selected actions will determine buy, sell, or hold for this trial
        time.sleep(1)
    return organism.profit
# Create the scoring function and build the ecosystem
scoring_function = lambda organism : simulate_and_evaluate(organism)
# Create the ecosystem
ecosystem = Ecosystem(organism_creator, scoring_function, population_size=1, holdout=0.1, mating=True)
# Save the fitness score (profit) of the best organism in each generation
#best_organism_scores = [ecosystem.get_best_organism(include_reward=True)[1]]

generations = 1
for i in range(generations):
    ecosystem.generation()
    #this_generation_best = ecosystem.get_best_organism(include_reward=True)



#######################################################################################################################

# The function to create the initial population
#organism_creator = lambda : Organism([1, 16, 16, 16, 1], output='linear')
# The function we are trying to learn. numpy doesn't have tau...
#true_function = lambda x : np.sin(2 * np.pi * x) #
# The loss function, mean squared error, will serve as the negative fitness
#loss_function = lambda y_true, y_estimate : np.mean((y_true - y_estimate)**2)

#def simulate_and_evaluate(organism, replicates=1):
#    X = np.random.random((replicates, 1))
#    predictions = organism.predict(X)
#    loss = loss_function(true_function(X), predictions)
#    return -loss
#
# Ecosystem requires a function that maps an organism to a real number fitness
#scoring_function = lambda organism : simulate_and_evaluate(organism, replicates=100)
# Create the ecosystem
#ecosystem = Ecosystem(organism_creator, scoring_function, 
#                      population_size=100, holdout=0.1, mating=True)
# Save the fitness score of the best organism in each generation
#best_organism_scores = [ecosystem.get_best_organism(include_reward=True)[1]]
#generations = 201
#for i in range(generations):
#    ecosystem.generation()
#    this_generation_best = ecosystem.get_best_organism(include_reward=True)
#    best_organism_scores.append(this_generation_best[1])