# [Ex 34] Verifique se determinados empréstimos podem ser realizados

print("--------------------------------------------------------------------")
print("Banco Polar ❄️")
print("--------------------------------------------------------------------\n")

print("Olá, por favor me informe seus dados para verificar se o empréstimo é valido!")

renda = int(input("Por favor informe a sua renda mensal:"))
emprestimoDesejado = int(input("Informe o valor do empréstimo que deseja:"))
prestacoes = int(input("Em quantas prestaçôes deseja pagar o mesmo?"))

limiteEmprestimo = 10*renda
limitePrestacoes = renda*0.3

prestacao = emprestimoDesejado/prestacoes
if (emprestimoDesejado > limiteEmprestimo):
    print("Infelizmente seu empréstimo não pode ser disponibilizado...")
elif (prestacao > limitePrestacoes):
    print("Infelizmente seu empréstimo não pode ser disponibilizado...")
else:
    print("Parabéns, seu empréstimo foi aprovado!")