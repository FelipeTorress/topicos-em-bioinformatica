# Aluno: Felipe da Rocha Torres
DNA = "ATAGGTACACTCAAGGACCGAGCCTTTACGGCATTAAATTAATCTGGTAAAGTGGATTCTAAGGAACAAACGCTCCTTTGGTCAATCGCTGGGGAGGCGTCTCCAGCGTTCACCCTTAACCATATTTTGTAGAATATAGTGACGCTTACAAGATCGTGGTTCCAGACTTCTTAGACGCACTAACTTATACAATTTAAACGTCCGAATTCGACGATGTACCTTAGCACATCGGCAGACAGGGATCACAATACACAGAGATTGGCGGTGTCGGAATACTTTCCACACCAGATTGTCGCAAACGCCATGTTCCGTTGCTTATCGAAATACATTGTTGCCAACCCACCGAGTGGGGTAAATCTAGGTGTATCGGCATAGTTTGGTTCCGGAATGATATCGGTACGAACTCTCGATGAAACCGTAGTCGACGCAACGTAGCGGTGCATAGGTGAATACGAAAGCCGAACAGAGCCACTTTCGTCCACAGGCGTGGCGGCCAAGTCTGCTTACAACTGCACTATACGCCTAACCATCTGTCTAATGTCCTTCGTCCAGAACGTGGTCCAACCCTGTCTCCTCTAATGTTATATGCCCCGAGTCTTCGGCGCCAGGTACCAGGGTAATCGGATCGGTAGAGACCCAAGTTATCCGGGCTTGGATGAATGTAACAGTTCATGGTCATTCGCATTCGAACCACAGACAGTACTCAATATTCTGCGTCCCTTGACATATGACGGACCTGTTATTATCTTTCAAGAGCGGCGCTGCGAGCCAGCTTCGTTATCGTTGTTGCGATCCGTATAAACCGGTCGTCCCGAGATAATAAGATGAAAAATGGGCCCTTAATCGGTATCGTGGAGTCCTGAAGAGGCCTGTAGTCTCACCACATCCTCTGATGATAGGTGTGTTATCGGTATGTTCGTATGCCACCAATTGCGTGGCGCCCACCTAAAGGAGGCATTTTGACAGTCTAGCGACAAGTCAGTGCCTGACAGGGGCATAAGAATACGTTTGCCACGTACGACCTAATCTAGCCCCTAACCGGGGAAATATCCTCCTTTAGTTGCCCTGAGCGAGATTAACTGCGACTACCGAAACTTTTTCATAGCGACAGCTGGTGGTTGGGACTCCTCGATACGAGCTGTATAACCTCTGAGGATACACACGTGCTCTGGCACTACCCTACGGTGAATACAGGGGCGGGCAACAGCGCCTCAGACATGTGACGAATATTTCGTAGAGAATTCCTGCCTCGCTCCGTCGAAAAATGGAAGAGTACCCGACACCACCATCTACGACACAGTGGATTGCTAGGTTGCACTTCGGAGAAATCCGTGTTCCCCATCTACGCGCCGGATCCAAAGTTCGGTGGTATCTAGCTACATATTCTGTTTGTTATTCAAGGTCTAACTCTTGTTCTTATTGCAGAAGACTCTAACTTCCCGACACGTGTTCGCTCGTTAATTCGGAAATCGGAACTGGATTAGTCACCTGCAACCTAGG"
RNA = ""

for bases in DNA:
    if bases == "A":
        RNA+="U"
    elif bases == "T":
        RNA+="A"
    elif bases == "G":
        RNA+="C"
    elif bases == "C":
        RNA+="G"

arquivo = open("RNA_Mensageiro.txt" ,"w")
arquivo.write(RNA)
arquivo.close()