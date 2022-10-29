"""
            Tempos Relatórios
    3.1 -> Linear vs Binária
    3.2 -> Linear vs Árvore Binária
    3.3 -> Linear vs AVL
                                """
import random, time, matplotlib.pyplot as plt

data = []
numutente = random.randint(1, 999999999)
vacinas = ["covid", "papeira", "tetano", "gripe", "hepatite-b", "polio"]
vacina = random.choice(vacinas)
date = str(random.randint(10, 28)) + str(random.randint(10, 12)) + str(random.randint(2017, 3000))
utente = [numutente, {vacina: date}]
y_linear_1 = []
y_binary_1 = []
y_bst_1 = []
y_avl_1 = []


# LINEAR
def consulta_linear(data, numutente):
    for i in range(len(data)):
        if int(data[i][0]) == numutente:
            return
    return


def acrescenta_linear(data, numutente, vacina, date, utente):
    x = 0
    for j in range(len(data)):
        if data[j][0] == numutente:
            x = 1
            if vacina in data[j][1]:
                data[j][1][vacina] = date
            else:
                data[j][1][vacina] = date
    if x == 0:
        order(data, utente)


def order(data, utente):
    y = False
    for i in range(len(data)):
        if utente[0] <= data[i][0]:
            data.insert(i, utente)
            y = True
            break
    if y == False:
        data.append(utente)


search = 0
insert = 0
n = 0
x = []

for i in range(11):
    data = []
    start = time.time()
    for a in range(insert):
        numutente = random.randint(1, 999999999)
        vacinas = ["covid", "papeira", "tetano", "gripe", "hepatite-b", "polio"]
        vacina = random.choice(vacinas)
        date = str(random.randint(10, 28)) + str(random.randint(10, 12)) + str(random.randint(2017, 3000))
        utente = [numutente, {vacina: date}]
        acrescenta_linear(data, numutente, vacina, date, utente)
    for b in range(search):
        numutente = random.randint(1, 999999999)
        consulta_linear(data, numutente)
    end = time.time()
    print("TEMPO LINEAR PARA N=", n, " É:", end - start, "S")
    x.append(n)
    y_linear_1.append(end - start)
    n += 100
    search *= int(0.1 * n)
    insert += int(0.9 * n)


# BINARIO

def binarysearch(data, numutente):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if numutente < data[mid][0]:
            last = mid - 1
        elif numutente > data[mid][0]:
            first = mid + 1
        else:
            break


search = 0
insert = 0
n = 0
for i in range(11):
    data = []
    start = time.time()
    for a in range(insert):
        numutente = random.randint(1, 999999999)
        vacinas = ["covid", "papeira", "tetano", "gripe", "hepatite-b", "polio"]
        vacina = random.choice(vacinas)
        date = str(random.randint(10, 28)) + str(random.randint(10, 12)) + str(random.randint(2017, 3000))
        utente = [numutente, {vacina: date}]
        acrescenta_linear(data, numutente, vacina, date, utente)
    for b in range(search):
        numutente = random.randint(1, 999999999)
        binarysearch(data, numutente)
    end = time.time()
    print("TEMPO BINARIO PARA N=", n, " É:", end - start, "S")
    y_binary_1.append(end - start)
    n += 1000
    search *= int(0.1 * n)
    insert += int(0.9 * n)
# BST
search = 0
insert = 0
n = 0
for i in range(11):
    data = []
    start = time.time()
    for a in range(insert):
        numutente = random.randint(1, 999999999)
        vacinas = ["covid", "papeira", "tetano", "gripe", "hepatite-b", "polio"]
        vacina = random.choice(vacinas)
        date = str(random.randint(10, 28)) + str(random.randint(10, 12)) + str(random.randint(2017, 3000))
        utente = [numutente, [vacina, data]]


        class Node:
            def __init__(self, value):
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
                for i in range(len(self.vacina)):
                    s += self.vacina[i] + " " + str(self.data[i]) + " "
                return s[:-1]

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

    for b in range(search):
        numutente = random.randint(1, 999999999)


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
    end = time.time()
    print("TEMPO ARVORE BINARIA PARA N=", n, " É:", end - start, "S")
    y_bst_1.append(end - start)
    n += 1000
    search *= int(0.1 * n)
    insert += int(0.9 * n)

# AVL
search = 0
insert = 0
n = 0
for i in range(11):
    data = []
    start = time.time()
    for a in range(insert):
        numutente = random.randint(1, 999999999)
        vacinas = ["covid", "papeira", "tetano", "gripe", "hepatite-b", "polio"]
        vacina = random.choice(vacinas)
        date = str(random.randint(10, 28)) + str(random.randint(10, 12)) + str(random.randint(2017, 3000))
        utente = [numutente, [vacina, data]]


        class Node:
            def __init__(self, value):
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
                for i in range(len(self.vacina)):
                    s += self.vacina[i] + " " + str(self.data[i]) + " "
                return s[:-1]

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

            def atualizaAlturas(self, rec=True):
                if self.node:
                    if rec:
                        if self.node.esq:
                            self.node.esq.atualizaAlturas()
                        if self.node.dir:
                            self.node.dir.atualizaAlturas()

                    self.altura = 1 + max(self.node.esq.altura, self.node.dir.altura)
                else:
                    self.altura = -1

            def atualizaEquilibrios(self, rec=True):
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

    for b in range(search):
        numutente = random.randint(1, 999999999)


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
    end = time.time()
    print("TEMPO ARVORE AVL PARA N=", n, " É:", end - start, "S")
    y_avl_1.append(end - start)
    n += 1000
    search *= int(0.1 * n)
    insert += int(0.9 * n)

# PLOTS
plt.plot(x, y_linear_1, '-b', marker='o', label="Pesquisa Linear")
plt.plot(x, y_binary_1, '-g', marker='o', label="Pesquisa Binária")
plt.plot(x, y_bst_1, '-y', marker='o', label="Árvore Pesquisa Binária")
plt.plot(x, y_avl_1, '-r', marker='o', label="Árvore AVL")

plt.legend()

plt.show()
