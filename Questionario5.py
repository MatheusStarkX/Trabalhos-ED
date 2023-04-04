#Nome: Matheus Felipe Magalhães de Assis
#Matrícula: 19/0035242
#Disciplina: Estrutura de Dados
#E-mail: matheusfelipemdeassis@gmail.com

#Questionário 5 ED

#Questão 1

class ArvoreBinaria:
    def __init__(self,dado=None,esq=None,dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

    def insertesq(self,newNode):
        if self.esq == None:
            self.esq = ArvoreBinaria(newNode)
        else:
            t = ArvoreBinaria(newNode)
            t.esq = self.esq
            self.esq = t

    def insertdir(self,newNode):
        if self.dir == None:
            self.dir = ArvoreBinaria(newNode)
        else:
            t = ArvoreBinaria(newNode)
            t.dir = self.dir
            self.dir = t

    def pegadir(self):
        return self.dir

    def pegaesq(self):
        return self.esq

def imprime(raiz,quant,patama,cont=0):
    if quant >= patama:
        if raiz:
            if cont == 0:
                print('(',end='')
            else:
                print(' (',end='')
            print(raiz.dado,end='')
            imprime(raiz.esq,quant,patama,1)
            imprime(raiz.dir,quant,patama,1)
            print(')',end='')
        else:
            print(' ()',end='')
    else:
        quant += 1
        if raiz.esq:
            imprime(raiz.esq,quant,patama,cont)
            print()
        if raiz.dir:
            imprime(raiz.dir,quant,patama,cont)

def mostra_nivel(raiz,patama):
    cont = 0
    quant = 0
    imprime(raiz,quant,patama,cont)

#Questão 2

class ArvoreBinaria:
    def __init__(self,dado=None,esq=None,dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def rotaciona_direita(raiz):
    if raiz:
        if raiz.esq:
            novaraiz = raiz.esq
            raiz.esq = novaraiz.dir
            novaraiz.dir = raiz
            return novaraiz
        return raiz

#Questão 3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def altura(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.altura(node.left)
        if node.right:
            hright = self.altura(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
        
quant = int(input())
elem = input().split()
arvore = BinarySearchTree()

for n in elem:
    arvore.insert(int(n))

print(arvore.altura()-1)

#Questão 4 - ERRO QUANDO NÃO É PASSADO NADA - RAIZ==NONE (90%)

class ArvoreBinaria:
    def __init__(self,dado=None,esq=None,dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def imprime(raiz,cont=0):
    if raiz:
        if cont == 0:
            print('(',end='')
        else:
            print(' (',end='')
        print(raiz.dado,end='')
        imprime(raiz.esq,1)
        imprime(raiz.dir,1)
        print(')',end='')
    else:
        print(' ()',end='')

def mostra(raiz):
    cont = 0
    imprime(raiz)

#Questão 5

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value <= x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value <= parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def simetric_traversal(self, node=None,cont=0):
        if node is None:
            node = self.root
        if node:
            if cont == 0:
                print('(',end='')
            else:
                print(' (', end='') 
            print(node, end='')
            if node.left:
                self.simetric_traversal(node.left,1)
            else:
                print(' ()',end='')
            if node.right:
                self.simetric_traversal(node.right,1)
            else:
                print(' ()',end='')
            print(')', end='')

quant = int(input())
if quant == 0:
    print('()')
else:
    elem = input().split()
    arvore = BinarySearchTree()

    for n in elem:
        arvore.insert(int(n))

    arvore.simetric_traversal()

#Questão 6

class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

def vai(arvore,pref,cont):
    if arvore:
        print(arvore.dado)
        if arvore.filhos != []:
            cont += 1
            for i in range(len(arvore.filhos)):
                for j in range(cont):
                    print(pref,end='')
                vai(arvore.filhos[i],pref,cont)

def mostra(arvore,pref):
    cont = 0
    vai(arvore,pref,cont)

#Questão 7 - https://github.com/alexallsup/Stern-Brocot/blob/master/procedural_sb.py

def mediant(frac1, frac2):
    return (frac1[0]+frac2[0], frac1[1]+frac2[1])

def compare_fracs(frac1, frac2):
	return frac1[0]*frac2[1] > frac2[0]*frac1[1]

def create_node(frac):
    root_node = ProcSBNode()
    while root_node.frac != frac:
        if compare_fracs(root_node.frac, frac):
            child_frac = mediant(root_node.left_frac, root_node.frac)
            root_node = ProcSBNode(frac=child_frac, is_left_child=True, parent=root_node, left=root_node.left_frac, right=root_node.frac)
        else:
            child_frac = mediant(root_node.right_frac, root_node.frac)
            root_node = ProcSBNode(frac=child_frac, is_left_child=False, parent=root_node, left=root_node.frac, right=root_node.right_frac)
    return root_node

class ProcSBNode():
    def __init__(self, frac=(1,1), is_left_child=True, parent=None, left=(0,1), right=(1,0)):
        self.parent = parent 
        self.frac = frac 
        self.is_left_child = is_left_child 
        self.left_frac = left 
        self.right_frac = right
        self.l_counted = False
        self.r_counted = False

    def get_left_child(self):
        return ProcSBNode(frac=mediant(self.frac, self.left_frac), is_left_child=True, parent=self, left=self.left_frac, right=self.frac)

    def get_right_child(self):
        return ProcSBNode(frac=mediant(self.frac, self.right_frac), is_left_child=False, parent=self, left=self.frac, right=self.right_frac)

    def denom(self):
        return self.frac[1]

    def numer(self):
        return self.frac[0]

x = int(input())
saidanum = []
saidadem = []

for i in range(x):
    caminho = input()
    pato = ProcSBNode()

    for letra in caminho:
        if letra == 'E':
            pato = pato.get_left_child()
        else:
            pato = pato.get_right_child()

    saidanum.append(pato.numer())
    saidadem.append(pato.denom())

for j in range(len(saidanum)):
    print(saidanum[j],'/',saidadem[j])

#Questão 8 - ERRO EM 3 TESTES ESCONDIDOS (70%)

class ArvoreBinaria:
    def __init__(self,dado=None,esq=None,dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

    def insertesq(self,newNode):
        if self.esq == None:
            self.esq = ArvoreBinaria(newNode)
        else:
            t = ArvoreBinaria(newNode)
            t.esq = self.esq
            self.esq = t

    def insertdir(self,newNode):
        if self.dir == None:
            self.dir = ArvoreBinaria(newNode)
        else:
            t = ArvoreBinaria(newNode)
            t.dir = self.dir
            self.dir = t

    def pegadir(self):
        return self.dir

    def pegaesq(self):
        return self.esq

def imprime(raiz,cont=0):
    if raiz:
        if cont == 0:
            print('(',end='')
        else:
            print(' (',end='')
        print(raiz.dado,end='')
        imprime(raiz.esq,1)
        imprime(raiz.dir,1)
        print(')',end='')
    else:
        print(' ()',end='')

def mostra(raiz):
    cont = 0
    imprime(raiz)

def altura(raiz):
    if raiz:
        hesq = 0
        hdir = 0
        if raiz.esq:
            hesq = altura(raiz.esq)
        if raiz.dir:
            hdir = altura(raiz.dir)
        if hdir > hesq:
            return hdir + 1
        return hesq +1

def difaltura(raiz):
    if raiz:
        if raiz.esq:
            left = altura(raiz.esq)
        else:
            left = 0
        if raiz.dir:
            right = altura(raiz.dir)
        else:
            right = 0
        raiz.dado = left - right
        if raiz.esq:
            difaltura(raiz.esq)
        if raiz.dir:
            difaltura(raiz.dir)
        
        return raiz
        
def findIndex(Str, si, ei):
    if (si > ei):
        return -1
    s = []
    for i in range(si, ei + 1):
        if (Str[i] == '('):
            s.append(Str[i])
        elif (Str[i] == ')'):
            if (s[-1] == '('):
                s.pop(-1)
                if len(s) == 0:
                    return i
    return -1

def treeFromString(Str, si, ei):
    if (si > ei):
        return None
    root = ArvoreBinaria(ord(Str[si]) - ord('0'))
    index = -1
    if (si + 1 <= ei and Str[si + 1] == '('):
        index = findIndex(Str, si + 1, ei)
    if (index != -1):
        root.esq = treeFromString(Str, si + 2,
                                index - 1)
        root.dir = treeFromString(Str, index + 2,
                                    ei - 1)
    return root

seque = input()
aux = ''
boa = ''

for i in range(len(seque)-1):
    if i != 0 and seque[i] != ' ':
        aux = aux + seque[i]
print(seque)

root = treeFromString(aux, 0, len(aux) - 1)
mostra(difaltura(root))