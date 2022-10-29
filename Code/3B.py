###   PESQUISA BINARIA   ###

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

def binSearch(dados, numUtente):
    primeiro = 0
    ultimo = len(dados) - 1
    while primeiro <= ultimo:
        media = (primeiro + ultimo) // 2
        if dados[media][0] == numUtente:
            out(numUtente)
            for v, d in sorted(dados[media][1].items()):
                out(' ' + v + ' ' + d)
            outln("")
            outln("FIM")
            break
        else:
            if numUtente < dados[media][0]:
                ultimo = media - 1
            else:
                primeiro = media + 1
    else:
        outln("NAO ENCONTRADO")

def order(dados, utente):
    val = False
    for i in range(len(dados)):
        if utente[0] <= dados[i][0]:
            dados.insert(i, utente)
            val = True
            break
    if val == False:
        dados.append(utente)



while loop is True:
    n = [str(i) for i in readln().split()]
    comand = n[0]

    if comand == "ACRESCENTA":
        numUtente = n[1]
        vacina = n[2]
        data = n[3]
        utente = [numUtente, {vacina: data}]
        x = 0
        for j in range(len(dados)):
            if dados[j][0] == numUtente:
                x = 1
                if vacina in dados[j][1]:
                    dados[j][1][vacina] = data
                    outln("VACINA ATUALIZADA")
                else:
                    dados[j][1][vacina] = data
                    outln("NOVA VACINA INSERIDA")
        if x == 0:
            order(dados, utente)
            outln("NOVO UTENTE CRIADO")


    elif comand == "CONSULTA":
        numUtente = n[1]
        binSearch(dados, numUtente)

    elif comand == "LISTAGEM":
        for i in range(len(dados)):
            out(dados[i][0])
            for j in sorted(dados[i][1]):
                out(' ' + j + ' ' + dados[i][1][j])
            outln('')
        outln("FIM")

    elif comand == "APAGA":
        dados.clear()
        outln("LISTAGEM DE NOMES APAGADA")

    elif comand == 'FIM':
        loop = False