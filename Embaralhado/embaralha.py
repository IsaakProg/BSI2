# Desafio Proposto
"""
Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo é acertar a palavra em até 5 tentativas. Informe sempre quantas tentativas ele ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (que mude de forma aleatória). Ao final, mostre a palavra correta e o número de tentativas que ele utilizou.
"""


from time import sleep
from random import choice
from funcoes import *
import json


# Carrega o arquivo json e converte para python
palavras_json = open("palavras.json", "r", encoding="utf-8")
palavras = json.load(palavras_json)


# Cria os menus com os temas especificados no parametro
tema = menu("Tema da Palavras:", ["cidades", "frutas", "paises", "objetos"])
dificuldade = menu("Nivel de Dificuldade:", ["Facil", "Intermediário", "Dificil"])


# Sorteia uma palavra de acordo com o tema e dificuldade escolhido
dificuldade = dificuldade - 1

if tema == 1:
    palavra_sorteada = choice(palavras["cidades"][dificuldade])

elif tema == 2:
    palavra_sorteada = choice(palavras["frutas"][dificuldade])

elif tema == 3:
    palavra_sorteada = choice(palavras["paises"][dificuldade])

elif tema == 4:
    palavra_sorteada = choice(palavras["objetos"][dificuldade])


# Embaralha a palavra sorteada
palavra_embaralhada = embaralha_palavra(palavra_sorteada)


# Verifica se o jogador acertou a palavra
verifica_acerto(palavra_embaralhada, palavra_sorteada)
