
from datetime import date
ano_Atual = date.today().year
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
Calculo = ano_Atual - ano_nascimento
if Calculo >=18:
    print("Voto Obrigatório")
elif Calculo >16:
    print("Voto Opcional")
else:
    Print("Não pode Votar")
