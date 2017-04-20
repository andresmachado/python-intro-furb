 # -*- coding: utf-8 -*-
"""
@author: Andre
"""

# A. donuts
# Dado um contador (int) de donuts, retorne uma string
# na forma 'Quantidade de: <count>', aonde <count> é
# o número informado. Entretanto, se o contador for 10 ou mais,
# user a palavra 'muitos' no lugar do contador atual
# Ex.: donuts(5) retorna 'Quantidade de donuts: 5'
# e donuts(24) retorna 'Quantidade de donuts: muitos!
def donuts(count):
    if count < 10:
        return 'Quantidade de donuts: ' + str(count)
    else:
        return 'Quantidade de donuts: muitos'

# print(donuts(5))
# print(donuts(10))

# B. both_ends
# Dado uma string 's', retorne a string feita os 2 primeiros
# e os 2 ultimos caracteres da string original.
# Entao, 'spring' retorna 'spng', entretanto se a string for
# menor que dois, o retorno é vazio
def both_ends(s):
  if len(s) < 2:
    return ''
  first2 = s[0:2]
  last2 = s[-2:]
  return first2 + last2

# print(both_ends('spring'))
# print(both_ends('winter'))
# print(both_ends('summer'))
# print(both_ends('s'))

# C. fix_start
# Dado uma string s, retorne uma string aonde todas as
# ocorrências da primeira letra sejam alteradas por '*'
# apenas nao altere o primeiro caractere
# ex.: 'babble' retorna 'ba**le'
# Dica: s.replace(stra, strb) retorna uma versao da string s
# aonde todas as ocorrencias de sao trocadas por strb.
def fix_start(s):
  front = s[0]
  back = s[1:]
  fixed_back = back.replace(front, '*')
  return front + fixed_back

# print(fix_start('babble'))
# print(fix_start('abracadabra'))
# print(fix_start('alakazam'))

# D. MixUp
# Dado duas strings, retorne uma unica string com
# as strings a e b separadas por espaço, trocando os 2 primeiros
# caracteres de cada string
# Ex.
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  a_swapped = b[:2] + a[2:]
  b_swapped = a[:2] + b[2:]
  return a_swapped + ' ' + b_swapped

# print(mix_up('mix', 'pod'))
# print(mix_up('dog', 'dinner'))
# print(mix_up('cat', 'fish'))

# A. match_ends
# Dada uma lista de strings, retorne a contagem de
# strings com tamanho maior que ou igual a 2 e que
# a primeira e o ultimo caracteres sejam os mesmos

def match_ends(words):
  count = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      count = count + 1
  return count

# print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
# print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
# print(match_ends(['aaa', 'be', 'abc', 'hello']))

# B. front_x
# Dado uma lista de strings, retorne uma lista com as
# strings ordenadas, exceto o grupo de caracteres que
# que começam com a letra 'x'.
# ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] resulta em
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: Voce pode fazer isso criando duas listas e ordenando-as
# antes de concatena-las

def front_x(words):
  x_list = []
  other_list = []
  for w in words:
    if w[0] == 'x':
      x_list.append(w)
    else:
      other_list.append(w)
  return sorted(x_list) + sorted(other_list)

# print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
# print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))



