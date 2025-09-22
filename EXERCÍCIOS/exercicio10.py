'''Programa que solicite duas notas de um aluno, imprima sua média e o resultado final:
Se a média for maior ou igual a 6.0 APROVADO
Senão REPROVADO'''

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda noita do aluno: "))

media = (nota1 + nota2) / 2

if media > 6:
    print(f"Média: {media}, aluno APROVADO")
else:
    print(f"Média: {media}, aluno REPROVADO")
