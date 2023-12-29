print("-"*30)
print("Supermecados Tarão Filial 03")
print("-"*30)

produto=" "
preço=0
soma= 0
contador= 0
menorp=0
barato=" "
p1000=0
while True:
    produto = str(input("informe o nome do produto: "))
    preço= float(input("informe o preço: R$  "))
    soma+=preço
    contador+=1
    if preço > 1000:
        p1000+=1
    if contador==1:
        menorp=preço
        barato=produto
    else:
        if preço < menorp:
            menorp=preço
            barato=produto
    escolha=" "
    while escolha not in "SN":
        escolha=str(input("Quer Continuar? [S/N]  ")).upper()
    if escolha =="N":
        break
print("-"*30)
print(f"Total de R${soma} ")
print("-"*30)
print(f"Com {p1000} produto(s) acima de R$1000.00")
print("-"*30)
print(f"Com o produto mais barato sendo o/a {barato}, custando {menorp}")
