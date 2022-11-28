import wget
import matplotlib.pyplot as plt
from collections import Counter
import os
from turtle import color


#FAZ O UPLOAD DO LIVRO,SE ELE NÃO EXISTIR NO REPOSITORIO

if os.path.exists('dracula.txt'):
    print("Arquivo já existe, e não será baixado.")
else:
    print("Arquivo não existe, baixando...")
    wget.download('https://www.gutenberg.org/files/16429/16429-0.txt','livro.txt')


# ABRE E LE O ARQUIVO
with open('dracula.txt',encoding="utf-8") as arquivo:
    texto = arquivo.read().lower()


# ELIMINA OS CARACTERES ESPECIAIS
texto_filtrado = ''.join([letra for letra in texto if letra.isalpha() or letra == ' '])


# CRIA UM DICIONARIO
letras = [l for l in texto_filtrado if l.isalpha()]
frequencia_letras = Counter(letras)


# EXIBE O GRAFICO DA FREQUENCIA DE LETRAS
rotulos, valores = zip(*frequencia_letras.most_common(5))
plt.title('frequência de letras')
plt.bar(rotulos,valores)
plt.xlabel('Letras')
plt.ylabel('Frequência')

# adiciona um rótulo centralizado no topo da barra
for i, v in enumerate(valores):
    plt.text(i, v, str(v), fontweight='bold',horizontalalignment='center',verticalalignment='bottom',color='blue')
    
plt.show()
    
