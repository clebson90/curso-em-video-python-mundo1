#1-
print("olá mundo")

#2-
nome = input("qual seu nome? ")
print(f"é um prazer te conhecer {nome}")

#3-
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
soma = n1 + n2
print(f"A soma entre {n1} e {n2} é igual a {soma}!")

#4-
algo = input("Digite algo: ")
print(f"O tipo primitivo desse valor é: {type(algo)}")
print(f"Só tem espaços? {algo.isspace()}")
print(f"É um número? {algo.isnumeric()}")
print(f"É alfabético? {algo.isalpha()}")
print(f"É alfanumérico? {algo.isalnum()}")
print(f"Está em maiúsculas? {algo.isupper()}")
print(f"Está em minúsculas? {algo.islower()}")
print(f"Está capitalizada? {algo.istitle()}")

#5-
num = int(input("Digite um número: "))
print(f"Analisando o valor {num}, seu antecessor é {num - 1} e o seu sucessor é {num + 1}")

#6-
num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f"O dobro de {num} vale {dobro}.")
print(f"O triplo de {num} vale {triplo}.")
print(f"A raiz quadrada de {num} é igual a {raiz:.2f}.")

#7-
nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(f"A média entre {nota1:.1f} e {nota2:.1f} é igual a {media:.1f}")

#8-
metros = float(input("Uma distância em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"A medida de {metros}m corresponde a {centimetros:.0f}cm e {milimetros:.0f}mm")

#9-
num = int(input("Digite um número para ver sua tabuada: "))
print("-" * 12)
print(f"{num} x {1:2} = {num * 1}")
print(f"{num} x {2:2} = {num * 2}")
print(f"{num} x {3:2} = {num * 3}")
print(f"{num} x {4:2} = {num * 4}")
print(f"{num} x {5:2} = {num * 5}")
print(f"{num} x {6:2} = {num * 6}")
print(f"{num} x {7:2} = {num * 7}")
print(f"{num} x {8:2} = {num * 8}")
print(f"{num} x {9:2} = {num * 9}")
print(f"{num} x {10:2} = {num * 10}")
print("-" * 12)

#10-
real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = real / 3.27
print(f"Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}")

#11-
largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))
area = largura * altura
tinta = area / 2
print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.3f}m².")
print(f"Para pintar essa parede, você precisará de {tinta:.4f}l de tinta.")

#12-
preco = float(input("Qual é o preço do produto? R$ "))
novo_preco = preco - (preco * 5 / 100)
print(f"O produto que custava R$ {preco:.2f}, na promoção com desconto de 5% vai custar R$ {novo_preco:.2f}")

#13-
salario = float(input("Qual é o salário do funcionário? R$ "))
novo_salario = salario + (salario * 15 / 100)
print(f"Um funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {novo_salario:.2f}")

#14-
celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura de {celsius}°C corresponde a {fahrenheit}°F!")

#15-
dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos Km rodados? "))
total = (dias * 60) + (km * 0.15)
print(f"O total a pagar é de R$ {total:.2f}")

#16-
from math import trunc
num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}")

#17-
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")

#18-
from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo que você deseja: "))
radiano = radians(angulo)
print(f"O ângulo de {angulo} tem o SENO de {sin(radiano):.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cos(radiano):.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tan(radiano):.2f}")

#19-
from random import choice
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")

#20-
from random import shuffle
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será:")
print(lista)

#21-
import pygame
pygame.init()
pygame.mixer.music.load("mp3.mp3")
pygame.mixer.music.play()
input("Pressione Enter para parar a música")

#22-
frase = input("Qual o seu nome?")
print(frase.upper())
print(frase.lower())
print(len(frase.strip()) - frase.count(" "))
print(frase.find(" "))

#23-
num = int(input("digite um numero de o a 9999? "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"unidade:{u}\n dezena:{d}\n centena:{c}\n milhar:{m}")

#24
cidade = input("em qual cidade vc nasceu? ").strip()
print(cidade[:5].upper() == "SANTO")

#25-
nome = input("qual seu nome? ").strip()
print("SILVA" in nome.upper())

#26-
frase = input("digite a frase ").strip().lower()
print(frase.count("a"))
print(frase.find("a")+1)
print(frase.rfind("a")+1)

#27-
nome = input("qual o seu nome completo? ").strip()
print(f"seu primeiro nome é {nome.split()[0]}")
print(f"seu ultimo nome é {nome.rsplit()[-1]}")

#28-
import random
n_sorteado = random.randint(0 , 5)
n = int(input("digite um numero! "))
if n == n_sorteado:
    print("parabens vc acertou")
else:
    print("vc errou")
print(n_sorteado)

#29-
v = int(input("a velocidade permitida é 80km (quanto vc tava?) "))
v_normal = 80
multa = (v_normal - v) * 7 *-1
if v > v_normal:
    print(f"vc foi multado \n valor é {multa}")
else:
    print("velocidade normal")

#30-
n = int(input("digite um numero! "))
print(n)
if n % 2 == 0:
    print("numero é par")
else:
    print("numero é impar")

#31-
d = int(input("qual a distancia da viagem? "))
pr1 = d * 0.50
pr2 = d * 0.45
if d <= 200:
    print(f"valor cobrado será {pr1}")
elif d > 200:
    print(f"valor cobrado será {pr2}")
print("boa viagem!")

#32-
from datetime import date
ano = int(input("qual o ano? (digite 0 pra saber o ano atual)"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"o {ano} é bissexto")
else:
    print(f" o {ano} não é bissexto")

#33-
n1 = int(input("digite um numero! "))
n2 = int(input("digite um numero! "))
n3 = int(input("digite um numero! "))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f"o menor número é {menor}")
print(f"o maior número é {maior}")

#34-
s = float(input("qual o seu salario? "))
aumento1 = s / 100 * 110
aumento2 = s / 100 * 115
if s > 1250.00:
    print(f" o aumento sera de {aumento1}")
elif s <= 1250.00:
    print(f" o aumento sera de {aumento2}")

#35-
l1 = int(input("qual o comprimento? "))
l2 = int(input("qual o comprimento? "))
l3 = int(input("qual o comprimento? "))
if l1 + l2 > l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print("é um triangulo")
else:
    print("não é um triangulo")