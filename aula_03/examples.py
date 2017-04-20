#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:08:17 2017

@author: andre
"""

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """Cria um baralho tradicional iterável."""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    

# Card('Q', 'hearts') in deck
# Card('7', 'beats') in deck

# for card in reversed(deck):
#    print(card)

suits_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
   rank_value = FrenchDeck.ranks.index(card.rank)
   return rank_value * len(suits_value) + suits_value[card.suit]


# +++++++++++++ #

class Mammal:
    
    def drink_milk(self):
        return True

class Animal:
    
    def __init__(self, name):
        print('Dentro da classe')
        self.name = name
        
    def __repr__(self):
        return self.name.title()
    
    def talk(self):
        return '{} is talking'.format(self.name)
    

class Dog(Animal, Mammal):
    paws = 4
    hungry = False
    angry = False
    
    def __init__(self, name, tricks=None):
        if tricks:
            self.tricks = list(tricks)
        else:
            self.tricks = []
        
        print('Dentro da subclasse')
        super(Dog, self).__init__(name)
  
    def talk(self):
        times = 2 if not self.angry else 4
        bark = 'Wof! ' * times
        return '{}: barks - {}'.format(self.name, bark)


    def set_hungry(self):
        if not self.hungry:
            self.hungry = True
            self.angry = True
            print('{} is now hungry and angry.'.format(self.name))
        else:
            self.angry = True
            print('{} is already hungry feed him!'.format(self.name))

    def feed(self):
        self.hungry = False
        self.angry = False
        print('{} is now fed and calm.'.format(self.name))