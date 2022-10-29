###   PESQUISA LINEAR   ###

from sys import stdin, stdout


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write('\n')


def out(n):
    stdout.write(str(n))


dados = []
loop = True


def order(dados, utente):
    val = False
    for i in range(len(dados)):
        if utente[0] <= dados[i][0]:
            dados.insert(i, utente)
            val = True
            break
    if val == False:
        dados.append(utente)


def linearsearch(dados, numUtente):
    a = 0

    for i in range(len(dados)):
        if int(dados[i][0]) == numUtente:
            a = 1
            return i
    if a == 0:
        return "NAO ENCONTRADO"


while loop is True:
    n = [str(i) for i in readln().split()]
    comando = n[0]

    if comando == "ACRESCENTA":
        numUtente = int(n[1])
        vacina = n[2]
        data = n[3]
        utente = [numUtente, {vacina: data}]
        x = 0
        for j in range(len(dados)):
            if dados[j][0] == numUtente:
                x=1
                if vacina in dados[j][1]:
                    dados[j][1][vacina] = data
                    outln("VACINA ATUALIZADA")
                else:
                    dados[j][1][vacina] = data
                    outln("NOVA VACINA INSERIDA")
        if x==0:
            order(dados, utente)
            outln("NOVO UTENTE CRIADO")

    elif comando == "CONSULTA":
        numUtente = int(n[1])
        if linearsearch(dados, numUtente) != "NAO ENCONTRADO":
            out(numUtente)
            for chave, valor in sorted(dados[linearsearch(dados,numUtente)][1].items()):
                out(' ' + chave + ' ' + valor)
            outln("")
            outln("FIM")
        else:
            outln(linearsearch(dados, numUtente))

    elif comando == "LISTAGEM":
        for i in range(len(dados)):
            out(dados[i][0])
            for j in sorted(dados[i][1]):
                out(' ' + j + ' ' + dados[i][1][j])
            outln('')
        outln("FIM")

    elif comando == "APAGA":
        dados.clear()
        outln("LISTAGEM DE NOMES APAGADA")

    elif comando == "FIM":
        loop = False