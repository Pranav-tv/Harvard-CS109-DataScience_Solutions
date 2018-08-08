#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:15:55 2018

@author: pranav
"""

import numpy as np

def simulate_prizedoor(nsim):
    
    return np.array(np.random.randint(3,size = nsim))


def simulate_guess(nsim):

    return np.array(np.random.randint(3,size = nsim))

def goat_door(prizedoors,guesses):
    choices = set((0,1,2))
    numbers = []
    for x,y in zip(prizedoors, guesses):
        numbers.append((choices - set((x,y))).pop())
    return(np.array(numbers))
        
      
def switch_guess(guesses, goatdoors):
    choices = set((0,1,2))
    numbers = []
    for x,y in zip(guesses, goatdoors):
        numbers.append((choices - set((x,y))).pop())
    return(np.array(numbers))     

def win_percentage(guesses, prizedoors):
    count = 0
    for x,y in zip(guesses, prizedoors):
        if x == y:
            count+=1
    return(count/len(guesses)*100)


nsim = int(input("Enter the number of simulations: "))

prizedoors = simulate_prizedoor(nsim)

guesses = simulate_guess(nsim)

goatdoors = goat_door(prizedoors, guesses)

switchedchoice = switch_guess(guesses, goatdoors)

winning_with_original_choice = win_percentage(guesses,prizedoors) 

winning_with_switched_choice = win_percentage(switchedchoice,prizedoors) 

print("\nWinning % with original choice = {}".format(winning_with_original_choice))

print("\nWinning % with switched choice = {}".format(winning_with_switched_choice))









