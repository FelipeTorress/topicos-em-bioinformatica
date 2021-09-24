RNAm = "AUGGCCCUGCAGGUGAAGGAAACACUCCCGCCAAUUAGAAAAUGCGUUAAGCGGUGCGUUAGUUCCCACGGACAGUGCGACACCCGAGGCAUAAUGAAUUACCCCCUCAUGAACAAGACACUUAAGCGCAACGGUCCUAUGAGAAUUCAUGCCAGUUGUGCUUAUUCCGCUGGAAGGCUGCGCGUCACAACGCGGUUAGUAUCUCGUAGGAGAAGUUAUUGUACUACCCACUCGAGUGGGUAUCCUCUCAACAGAGAGGUCCGGGAGAAAUAUGCUGAAGUACAGGAUUCGGUGUAUGCAAAAUAA"
cadeiaDeAminoacidos = ""

#start = ["AUG"]
#stop = ["UAA","UAG","UGA"]
geneticCode = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L', 
'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST', 
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', 
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}

count = 0 #contador para auxiliar pegar de 3 em 3 as bases nitrogenadas
aminoacidoAux = '' #variavel auixiliar para salvar as 3 bases com que se vai trabalhar

for base in RNAm:
    aminoacidoAux+=base
    count+=1
    if count == 3:
        if aminoacidoAux == "AUG":
            count = 0
            aminoacidoAux = ''
            continue
        elif aminoacidoAux == "UAA" or aminoacidoAux == "UAG" or aminoacidoAux == "UGA":
            break
        else:
            cadeiaDeAminoacidos += geneticCode[aminoacidoAux]
            count = 0
            aminoacidoAux = ''


arquivo = open('cadeia_de_aminoacidos.txt','w')
arquivo.write(cadeiaDeAminoacidos)
arquivo.close()