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

# Podemos reverter a ordem do nosso deck()
for card in reversed(deck):
    print(card)

# Podemos ordenar o deck() de acordo com a carta mais alta

# Define o critério de ordenação
suits_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
   rank_value = FrenchDeck.ranks.index(card.rank)
   return rank_value * len(suits_value) + suits_value[card.suit]

# Ordena, revertido ou não (basta definir o reverse)
sorted(deck, key=spades_high, reverse=True)

# +++++++++++++ #
# Mixin, não inicializa valores, por não implementar o __init__()
class Mammal:
    
    def drink_milk(self):
        return True

# Classe pai, que será herdada futuramente
class Animal:
    """Classe para criar Animais genéricos."""
    
    # Construtor da classe, pode receber argumentos.
    def __init__(self, name):
        print('Dentro da classe')
        self.name = name
        
    def __repr__(self):
        return self.name.title()
    
    def talk(self):
        return '{} is talking'.format(self.name)
    

class Dog(Animal, Mammal):
    """Especialização da classe Animal e com o mixin Mammal"""
    
    # Atributos da classe, cada instancia terá sua versão
    paws = 4
    hungry = False
    angry = False
    
    def __init__(self, name, tricks=None):
        """
        Metodo construtor da subclasse, recebe um novo argumento chamado tricks 
        que deve ser uma lista
        
        :param tricks: argumento que deve ser uma lista
        :param name: string que define um nome
        :usage: dog = Dog('nome', tricks=['Rolar','Falar'])
        :return: instancia da classe Dog()
        """
        if tricks:
            self.tricks = list(tricks)
        else:
            self.tricks = []
        
        print('Dentro da subclasse')
        # Chama o metodo da classe pai de acordo com o MRO cls.__mro__ ou help(Cls)
        # para mais informações
        super(Dog, self).__init__(name)
  
    def talk(self):
        """Metodo para sobrescrever o original da classe Pai."""
        times = 2 if not self.angry else 4
        bark = 'Wof! ' * times
        return '{}: barks - {}'.format(self.name, bark)


    def set_hungry(self):
        """Metodo que deixa o dog faminto."""
        if not self.hungry:
            self.hungry = True
            self.angry = True
            print('{} is now hungry and angry.'.format(self.name))
        else:
            self.angry = True
            print('{} is already hungry feed him!'.format(self.name))

    def feed(self):
        """Metodo que deixa o dog calmo e alimentado."""
        self.hungry = False
        self.angry = False
        print('{} is now fed and calm.'.format(self.name))