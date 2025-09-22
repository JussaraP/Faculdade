import csv
import math

def lerNumeros(): # Função para ler os números do teclado
    vet_jussara = []
    while True:
        try:
            num = int(input("Digite um número inteiro positivo ou -1 para parar: "))
            if num == -1:
                break
            if num > 1:
                if num not in vet_jussara:  # evita duplicados
                    vet_jussara.append(num)
            else:
                print("Número inválido!")
        except ValueError:
            print("Inválido! Digite apenas números inteiros")
    return vet_jussara


def quebrarChave(n):  # Função para quebrar a chave RSA (achar um divisor e inferir o outro)
    limite = int(math.isqrt(n))  # raiz quadrada inteira de n
    for i in range(2, limite + 1):
        if n % i == 0:
            return i, n // i
    return 1, n  # se não achou nenhum divisor, o número é primo



def imprimirResultados(vetor, div1, div2): # Função para imprimir resultados
    for i in range(len(vetor)):
        print(f"{vetor[i]} tem divisores {div1[i]} e {div2[i]}")


def salvar_csv(vetor, div1, div2, nome="jussara"): # Função para salvar em CSV
    nome_arquivo = f"relat_{nome}.csv"
    with open(nome_arquivo, mode="w", newline="") as file:
        escritor = csv.writer(file)
        for i in range(len(vetor)):
            escritor.writerow([vetor[i], div1[i], div2[i]])
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")


def main():
    vet_jussara = lerNumeros()
    jussara_div1 = []
    jussara_div2 = []

    for num in vet_jussara:
        d1, d2 = quebrarChave(num)
        jussara_div1.append(d1)
        jussara_div2.append(d2)

    imprimirResultados(vet_jussara, jussara_div1, jussara_div2)
    salvar_csv(vet_jussara, jussara_div1, jussara_div2, "jussara")

# Executa o programa
if __name__ == "__main__":
    main()
