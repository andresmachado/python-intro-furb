#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:29:15 2017

@author: andre
"""

me = {'name': 'Andre', 'idade':29}

# A. is_key_there
# Dado um dicionario e uma chave, verifique
# se esta chave existe naquele dicionario
# se existir retorne 'Chave encontrada: <valor_da_chave>!'
# caso contrário, retorne 'Não encontrado a chave <k> no dict <d>!'
def is_key_there(d, k):
    if k in d:
        return 'Chave encontrada: {}!'.format(d[k])
    else:
        return 'Não encontrado a chave {} no dict {}!'.format(k, d)


# B. dict_union
# Dado uma lista de dicionarios, crie um
# unico dicionario com todos os outros
# dica: o metodo d.update(d) pode ser
# usado para ajudar nesta tarefa
# ex.: dict_list = [{1: 20, 2:30}, {3: 120, 4:310}, {5: 220, 6:430}]
# retorna {1: 20, 2:30, 3: 120, 4:310, 5: 220, 6:430}
def dict_union(dict_list):
    # seu codigo aqui
    dic4 = {}
    for d in dict_list:
        dic4.update(d)
    return dic4


# C. sum_dict_values
# Dado um dicionario, some todos os valores
# e retorne o total dessa soma. O dicionario pode ter
# valores heterogeneos, neste caso retorne a string 'impossivel'
# dica: Voce pode verificar o tipo do valor 
# com a funcao isinstance(object, classinfo)
# Tudo em Python é objeto!
def sum_dict_values(d):
    total = 0
    for v in d.values():
        if not isinstance(v, (int, float)):
            return 'Impossivel!'
        total += v
    return total


# D. get_min_max
# Dado um dicionario, retorne o maior e o menor valor
# ex.: my_dict = {'x':500, 'y':5874, 'z': 560}
# returna "Maximo: 5874, Minimo: 500"
def get_min_max(d):
    key_max = max(d.keys(), key=(lambda k: d[k]))
    key_min = min(d.keys(), key=(lambda k: d[k]))
    return "Maximo: {}, Minimo: {}".format(d[key_max], d[key_min])
