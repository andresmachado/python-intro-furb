#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 23:54:11 2017

@author: andre
"""

"""
a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
a - b                              # letters in a but not in b
a | b                         # letters in either a or b
a & b             # letters in both a and b
a ^ b                              # letters in a or b but not both
"""

"""
O metodo zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
"""

"""
Agrupando objetos com dict()

names = ['carlos', 'marcelo', 'charles', 'felipe', 'andre', 'suelle',
'gustavo']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

"""

"""
Contando com dicionarios
cores = ['vermelho', 'verde', 'azul', 'amarelo', 'verde', 'azul', 'amarelo',
'amarelo']

d = {}
for cor in cores:
    if cor not in d:
        d[cor] = 0
    d[cor] += 1
"""

"""
Utilizando dicionarios para formatar strings
a_dict = dict(nome='Andre', idade='29')
"Meu nome é {nome} e eu tenho {idade} anos".format(**a_dict)
"""



"""
Exemplo de iterador
def g123():
    yield 1
    yield 2
    yield 3
"""

"""
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()

cards = [(rank, suit) for suit in suits
                      for rank in ranks]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
"""

"""
- namedtuples

somenamedtuple._make(iterable)
somenamedtuple._asdict()
somenamedtuple._replace(kwargs)
somenamedtuple._fields

- Transformar dict em uma namedtuple

City = namedtuple('City', 'name lat lng')
d = {'name': 'LAX', 'lat': 33.9425, 'lng': -118.408056}
lax = City(**d)
"""