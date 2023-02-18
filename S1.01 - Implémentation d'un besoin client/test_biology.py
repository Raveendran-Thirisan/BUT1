def est_base(c):
    assert est_base('A')
    assert est_base('G')
    

def est_adn(s):
    assert est_adn("AAGT")
    assert not est_adn("ABGT")


def arn(adn):
    assert arn('ATT')
    assert arn ('ATGCCCT')
    
    
    
def arn_to_codons(arn):
    assert arn_to_codons("CGUAAU")
    assert arn_to_codons("CGUAAUGC")
    
    
    
def load_dico_codons_aa(filename):
    load_dico_codons_aa(codon_aa.json)
    

def codons_stop(dico):
    assert codons_stop(["ACC"])
    assert codons_stop(["AAA"]
    
    
def codons_to_aa(codons, dico):
    assert codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"],dico)
    assert codonq_to_aa (["UUU","CUA","UAC"],dico)