adn = ['A','T','G','C']


def est_base(c):
    pass
    return c in adn


def est_adn(s):
    pass
    for c in s:
            if not est_base(c):
                return False
    return True

def arn(adn):
    pass
    arn = ''
    if not est_adn(adn):
        print ("Cette ADN n'existe pas")
        return None
    for c in adn:
        if c == 'A':
            arn = arn+ 'A'
        if c == 'C':
            arn = arn+ 'C'
        if c == 'G':
            arn = arn+ 'G'
        if c == 'T':
            arn = arn+ 'U'
    print(arn)


def arn_to_codons(arn):
    pass
    codons = []
    if len (arn) <3:
        return False
    for i in range (len(arn)// 3) :
        j=0
        tmp= ""
        while j < 3:
            tmp+=arn[j]
            j+=1
        codons.append (tmp)
        arn = arn[3::]
    return codons

from json import *
def load_dico_codons_aa(filename):
    pass
    fichier = open(filename,"r")
    json = fichier.read()
    fichier.close()
    dicoadn = loads(json)
    return dicoadn


def codons_stop(dico):
    pass
    t = []
    for v in codons:
        if v not in dico.keys():
            t.append(v)
    return t
    
def codons_to_aa(codons, dico):
    pass
    t = []
    arret = codons_stop(codons,dico)
    
    for a in codons:
        if a in arret:
            return t
        if a in dico.keys():
            t.append(dico[a])
    return t




def nextIndice(tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass
