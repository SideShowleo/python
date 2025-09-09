nota1 = float(input("Digite a nota da Atividade 01: "))
nota2 = float(input("Digite a nota da Atividade 02: "))
nota3 = float(input("Digite a nota da Atividade 03: "))

resu = ((nota1 + nota2 + nota3) /3)
print(f"A Sua media foi de:{resu}")
if resu >= 5:
    print("Você está de Recuperação")
elif resu >= 7:
    print("Você foi Aprovado!")
else:
    print("Você foi reprovado!")