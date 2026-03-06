#Sistema de Notas de Alunos como se fosse um boletim

qnt = int(input("Quantos alunos deseja cadastrar? "))      #Aqui ele solicita a quantidade de alunos
alunos = []                                                #Aqui a gente cria uma lista para os alunos que vao ser listados

for i in range(qnt):                                       #Aqui cria um loop com a quantidade de alunos que foi solicitada
    nome = input("Digite o nome do aluno: ")               #Aqui a gente cadastra o nome do aluno np sistema
    notas = []                                             #Aqui a gente cria uma lista para as notas que vão ser listadas

    for j in range(3):                                     #Aqui a gente cria um loop para solicitar as 3 notas que o sistema pede
        try:                                               #Aqui a gente cria o try para quando digitar algo diferente da nota repitir o loop
            nota = float(input("Digite a nota: "))
            notas.append(nota)                             #Aqui a gente leva as notas que foram solicitadas para a lista notas
        except ValueError:                                 #Aqui é except que acompanha o try para se digitar algo diferente da nota repitir o processo
            print('Valor invalido, Digite um numero!')

    alunos.append({
        "nome" : nome,
        "notas" : notas
    })                                                     #Aqui a gente adiciona as notas junto com o nome dos alunos

medias = []

for aluno in alunos:                                       #Aqui a gente cria um loop para cada aluno da lista alunos
    nome = aluno[0]                                        #Aqui solicita o aluno na posição zero
    notas = aluno[1]                                       #Aqui sua respectiva nota de acordo com o aluno da posição zero
    media = sum(notas) / len(notas)                        #Aqui a gente faz a media de cada aluno
    medias.append({
        "nome" : nome,
        "media" : media
    })
    if media >= 7:
        situacao = 'Aprovado!'
    elif media >= 5:
        situacao = 'Está de recuperação!'
    else :
        situacao = 'Reprovado!'

    print('------------------------')
    print("Aluno:", nome)
    print(f'Notas: {notas}')
    print(f"Média: {media:.2f}")
    print(f'Situação: {situacao}')
    print("------------------------")

maior_media = max(medias, key=lambda x: x[1])
menor_media = min(medias, key=lambda x: x[1])

print('-------------------------------------------')
print(f'Quem teve a maior media foi {maior_media[0]} com {maior_media[1]:.2f}')
print(f'Quem teve a menor media foi {menor_media[0]} com {menor_media[1]:.2f}')
print('-------------------------------------------')