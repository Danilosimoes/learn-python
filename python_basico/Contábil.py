horasTrabalhas = float(input("Digite a quantidade de horas que você trabalhou: "))
valorHora = float(input("Digite o valor das horas trabalhadas: "))
percentualDesconto = float(input("Digite o percentual de desconto: "))

salarioBruto = horasTrabalhas * valorHora
totalDesconto = (percentualDesconto/100) * salarioBruto
salarioLiquido = salarioBruto - totalDesconto

print("As horas trabalhadas foram ", horasTrabalhas, "\nO salário bruto foi R$ ", salarioBruto, "\nO desconto foi de ", totalDesconto, "\nO salário líquido é de R$ ", salarioLiquido)