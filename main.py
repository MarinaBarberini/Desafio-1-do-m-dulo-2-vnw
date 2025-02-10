# missao 1: restaurando as regras escolares

nota = input('Insira a nota do aluno: ')
if nota >= 6:
    print('O aluno foi aprovado.')
else:
    print('O aluno foi reprovado.')

# missao 2: o sistema eleitoral secreto

idade = input('Insira a idade: ')
if idade >= 16:
    print('O aluno pode votar.')
else:
    print('O aluno ainda não pode votar.')

# missao 3: recuperando o sistema de notas

nota = input('Insira a nota: ')
if nota >= 90:
    print('Parabéns, você tirou A!')
elif nota < 90 and nota > 80:
    print('Muito bem, você tirou B.')
elif nota < 80 and nota > 70:
    print('Bom trabalho, você tirou C.')
elif nota < 70 and nota > 60:
    print('Fique atento, você tirou D.')
elif nota < 40:
    print('Estude um pouco mais, você tirou F.')

# missao 4: restaurando a identificacao de números

primeiro_valor = input('Insira o primeiro valor: ')
segundo_valor = input('Insira o segundo valor: ')
print(primeiro_valor + segundo_valor)

# missao 5: recuperando o cofre de segurança

senha = input('Digite a senha: ')
if senha == 'python123':
    print('Acesso permitido.')
else:
    print('Acesso negado.')

    # missao 6: reforcando a seguranca e a contagem do sistema
    contador = 1

while contador < 11:
    print(contador)
    contador += 1

    # missao 7: organizando a lista

lista = [8, 3, 10, 1, 5]
lista.sort()
print(lista)

# missao 8: acessando o registro de aluno
alunos = ("Ana", 'Bruno', 'Carla', 'Daniel', 'Eduardo')
print(alunos[0])
print(alunos[-1])

# missao 9:


def numero(n):
    dobro = (n*2)
    return f'O dobro de {n} é {dobro}'


resultado = numero(3)
print(resultado)

# missao 10:


def contar_letras(nome):
    quantidade = len(nome)
    return f"O nome {nome} tem {quantidade} letras."


resultado = contar_letras('Ana')
print(resultado)
