#Eduardo Lourenço da Silva
#Engenhraria de Software - 01/2024
#19/03/2024
import math

print("\nLista de exercícios 1 (18/03/2024)")

def ex01():
    print("Exercício 01")
    print("Alô mundo")

def ex02():
    print("Exercício 02")
    num = int(input("Entre com o número: "))
    print(f"O número informado foi {num}")

def ex03():
    print("Exercício 03")
    num1 = int(input("Entre com o primeiro número: "))
    num2 = int(input("Entre com o segundo número: "))
    soma = num1 + num2
    print(f"A soma dos números {num1} e {num2} é: {soma}.")

def ex04():
    print("Exercício 04")
    nota1 = float(input("Entre com a primeira nota: "))
    nota2 = float(input("Entre com a segunda nota: "))
    nota3 = float(input("Entre com a terceira nota: "))
    nota4 = float(input("Entre com a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média é de: {media}.")

def ex05():
    print("Exercício 05")
    metros = float(input("Entre com o valor em metros: "))
    centimetros = metros * 100
    print(f"{metros} metros = {centimetros} centímetros.")

def ex06():
    print("Exercício 06")
    raio = float(input("Entre com o valor do raio do círculo, em metros: "))
    area = math.pi * raio**2
    print(f"Área do círculo: {area} m")

def ex07():
    print("Exercício 07")
    lado = float(input("Entre com o valor do lado do quadrado: "))
    area = lado ** 2
    print(f"Área do quadrado: {area}")
    print(f"Área do quadrado (dobro): {area * 2}")

def ex08():
    print("Exercício 08")
    valorHora = float(input("Entre com o quanto você ganha por hora trabalhada: "))
    horasMes = float(input("Entre com a quantidade de horas que você trabalhou no mês: "))
    salario = valorHora * horasMes
    print(f"Salário: {salario}")

def ex09():
    print("Exercício 09")
    altura = float(input("Entre com a altura da pessoa em metros: "))
    pesoIdeal = (72.7 * altura) - 58
    print(f"O peso ideal: {pesoIdeal} kg")

def ex10():
    print("Exercício 10")
    peso = float(input("Entre com o peso total dos peixes em quilo (kg): "))
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print(f"Peso excedente: {excesso} kg\nMulta: R$ {multa}")
    else:
        print(f"Livre de multas!\nPeso menor que o limite.")

def ex11():
    print("Exercício 11")
    valorHora = float(input("Entre com o quanto você ganha por hora trabalhada: "))
    horasMes = float(input("Entre com a quantidade de horas que você trabalhou no mês: "))
    salarioBruto = valorHora * horasMes
    desImpostoRenda = salarioBruto * 0.11
    desInss = salarioBruto * 0.08
    desSindicato = salarioBruto * 0.05
    salarioLiquido = salarioBruto - (desImpostoRenda + desInss + desSindicato)
    print("-----------------------------------")
    print(f"Salário bruto    : + R$ {salarioBruto}")
    print(f"Imposto de renda : - R$ {desImpostoRenda}")
    print(f"INSS             : - R$ {desInss}")
    print(f"Sindicato        : - R$ {desSindicato}")
    print("-----------------------------------")
    print(f"Salário líquido  : = R$ {salarioLiquido}")

def ex12():
    print("Exercício 12")
    fahrenheit = float(input("Entre com o valor da temperatura em graus Fahrenheit: "))
    celsius = (5 * (fahrenheit - 32) / 9)
    print(f"Temperatura em graus Celsius: {celsius} C°")

def start():
    ex = int(input("\nEntre com o número do ex (1 a 12):"))
    if ex == 1:
        ex01()
    elif ex == 2:
        ex02()
    elif ex == 3:
        ex03()
    elif ex == 4:
        ex04()
    elif ex == 5:
        ex05()
    elif ex == 6:
        ex06()
    elif ex == 7:
        ex07()
    elif ex == 8:
        ex08()
    elif ex == 9:
        ex09()
    elif ex == 10:
        ex10()
    elif ex == 11:
        ex11()
    elif ex == 12:
        ex12()
    else:
        print("Ex não encontrado ;(")
    start()

start()
