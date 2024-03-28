from veiculos import *

tipo=input("Qual o seu veículo?\n1: Carro\n2: Moto\n")

while tipo not in ["1", "2"]:
  print("Digite 1 para moto e 2 para carro")
  tipo=input("Qual o seu veículo?\n1: Carro\n2: Moto\n")
  if tipo=="1":
    marca=input("Qual a marca do seu veículo? ")
    ano=int(input("Qual o ano do seu veículo? "))
    preco=float(input("Qual o preço do seu veículo? "))
    modelo=input("Qual o modelo do carro? ")
    potencia=int(input("Qual a potência do carro em cavalos? "))
    carro=(marca, ano, preco, modelo, potencia)
    print(carro.info())
  elif tipo=="2":
    marca=input("Qual a marca do seu veículo? ")
    ano=int(input("Qual o ano do seu veículo? "))
    preco=float(input("Qual o preço do seu veículo? "))
    cilindrada=int(input("Qual a cilindrada da moto? "))
    moto=Moto(marca, ano, preco, cilindrada)
    print(moto.info())
  else:
    print("Você escolheu uma opção inexistente.")