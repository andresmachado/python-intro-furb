#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:35:26 2017

@author: andre
"""
from math import pi
pi = 3.1415

formato_tabela = '{0:^6} | {1:^9} | {2:^10}'
produtos = [
    (2, 'Amarelo', 18.50),
    (5, 'Verde', 48.50),
    (2, 'Azul', 78.50),
]

"""
'{} + {} = {}'.format(10, 10, 20)
'{0} + {1} = {2}'.format(10, 10, 20)  # esse é o padrão
'{0} + {0} = {1}'.format(10, 20)
'{1} + {0} = {2}'.format(30, 20, 10)  # evite fazer isso para não confundir

a_string = '{cidade} é muito bonito(a) durante o(a) {estação}'
a_string.format(cidade='Bruxelas', estação='Inverno')

'O total é R${0}'.format(59.8912313)
'O total é R${0:.2f}'.format(59.8912313)
'A porcentagem é de {0:.2%}'.format(0.8912313)

'{0:<10} | {1:<10} | {2:<10}'.format('Qtd.', 'Cor', 'Valor')
'{0:>10} | {1:>10} | {2:>10}'.format('Qtd.', 'Cor', 'Valor')
'{0:^6} | {1:^9} | {2:^10}'.format('Qtd.', 'Cor', 'Valor')
'{0:+^6} | {1:=^9} | {2:-^10}'.format('Qtd.', 'Cor', 'Valor')
'{0:+^6} | {1:=^9} | {2:-^10}'.format('Qtd.', 'Cor', 'Valor')

print(formato_tabela.format('Qtd.', 'Cor', 'Valor R$'))
for qtd, cor, valor in produtos:
    print(formato_tabela.format(qtd, cor, valor))
    
'{0:e} {0:f} {0:%}'.format(.0000031)

format(math.pi, '6.3f')
format('Python', '.<12')
format('Python', '.>12')
format('Python', '.^12')
"""
