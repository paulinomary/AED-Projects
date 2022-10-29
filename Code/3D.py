###   ARVORE AVL   ###

from sys import stdout, stdin

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write('\n')

def out(n):
    stdout.write(str(n))

loop = True

class Node:
    def __init__(self,value):
        self.esq = None
        self.dir = None
        self.info = value

class Paciente:
    def __init__(self, numUtente):
        self.numUtente = numUtente
        self.vacina = []
        self.data = []

    def __str__(self):
        s = str(self.numUtente) + " "
        for i in range (len(self.vacina)):
            s+= self.vacina[i] + " " + str(self.data[i]) + " "
        return s[ :-1 ]

    def info(self, vacina, data):
        self.vacina.append(vacina)
        self.data.append(data)
        self.vacina, self.data = (list(x) for x in zip(*sorted(zip(self.vacina, self.data))))

class Tree:
    def __init__(self):
        self.node = None
        self.altura = -1
        self.equilibrio = 0

    def inserir(self, value):
        if not self.node:
            self.node = Node(value)
            self.node.esq = Tree()
            self.node.dir = Tree()
            print("NOVO UTENTE CRIADO")

        elif value.numUtente == self.node.info.numUtente:
            if (value.vacina[0] in self.node.info.vacina):
                indice = self.node.info.vacina.index(value.vacina[0])
                self.node.info.data[indice] = value.data[0]
                print("VACINA ATUALIZADA")

            else:
                self.node.info.info(value.vacina[0], value.data[0])
                print("NOVA VACINA INSERIDA")

        elif value.numUtente < self.node.info.numUtente:
            self.node.esq.inserir(utente)

        elif value.numUtente > self.node.info.numUtente:
            self.node.dir.inserir(utente)

        self.reequilibrar()

    def reequilibrar(self):
        self.atualizaAlturas(rec=False)
        self.atualizaEquilibrios(False)
        while self.equilibrio < -1 or self.equilibrio > 1:
            if self.equilibrio > 1:
                if self.node.esq.equilibrio < 0:
                    self.node.esq.rotacaoEsq()
                    self.atualizaAlturas()
                    self.atualizaEquilibrios()

                self.rotacaoDir()
                self.atualizaAlturas()
                self.atualizaEquilibrios()

            if self.equilibrio < -1:

                if self.node.dir.equilibrio > 0:
                    self.node.dir.rotacaoDir()
                    self.atualizaAlturas()
                    self.atualizaEquilibrios()

                self.rotacaoEsq()
                self.atualizaAlturas()
                self.atualizaEquilibrios()

    def atualizaAlturas(self, rec = True):
        if self.node:
            if rec:
                if self.node.esq:
                    self.node.esq.atualizaAlturas()
                if self.node.dir:
                    self.node.dir.atualizaAlturas()

            self.altura = 1 + max(self.node.esq.altura, self.node.dir.altura)
        else:
            self.altura = -1

    def atualizaEquilibrios(self, rec = True):
        if self.node:
            if rec:
                if self.node.esq:
                    self.node.esq.atualizaEquilibrios()
                if self.node.dir:
                    self.node.dir.atualizaEquilibrios()

            self.equilibrio = self.node.esq.altura - self.node.dir.altura
        else:
            self.equilibrio = 0

    def rotacaoDir(self):
        nr = self.node.esq.node
        nsub = nr.dir.node
        ar = self.node

        self.node = nr
        ar.esq.node = nsub
        nr.dir.node = ar

    def rotacaoEsq(self):
        nr = self.node.dir.node
        nsub = nr.esq.node
        ar = self.node

        self.node = nr
        ar.dir.node = nsub
        nr.esq.node = ar

    def print(self, root):
        if root.node != None:
            self.print(root.node.esq)
            outln(root.node.info)
            self.print(root.node.dir)

    def procura(self, val):
        if self.node == None:
            return None
        n = self.node
        while n.info.numUtente != val:
            if val < n.info.numUtente:
                n = n.esq.node
            else:
                n = n.dir.node
            if n == None:
                return None
        return n.info

    def apaga(self):
        self.node = None

if __name__ == "__main__":
    arvore = Tree()
    while loop:
        entrada = [str(i) for i in readln().split()]
        comando = entrada[0]

        if comando == "ACRESCENTA":
            numUtente = entrada[1]
            vacina = entrada[2]
            data = entrada[3]
            utente = Paciente(int(numUtente))
            utente.info(vacina,int(data))
            arvore.inserir(utente)

        elif comando == "CONSULTA":
            numUtente = entrada[1]
            if arvore.procura(int(numUtente)) != None:
                outln(arvore.procura(int(numUtente)))
                outln("FIM")
            else:
                outln("NAO ENCONTRADO")

        elif comando == "LISTAGEM":
            arvore.print(arvore)
            outln("FIM")

        elif comando == "APAGA":
            arvore.apaga()
            outln("LISTAGEM DE NOMES APAGADA")

        elif comando == "FIM":
            loop = False