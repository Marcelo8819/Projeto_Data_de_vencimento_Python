from functions import *

print("=============================\n")
print("Qual a data de vencimento? ")
print("Formato sugerido: Dia-Mês-Ano. Exemplo: 01-09-2000\n")
print("=============================\n")

due_date = input("")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("Entrada inválida!")
