#!/usr/bin/env python3

import sys	 #é necessário para rodar os comandos sys

#Aplicando uma restrição para que apenas as entradas com o numero correto de argumentos sigam o código
if len(sys.argv) < 6 or len(sys.argv) > 6:
    sys.exit("Digite uma sequencia e quatro números inteiros")
if len(sys.argv) == 6:
#A sequencia deve ser um string
    if sys.argv[1].isdigit():
        seq = str(sys.argv[1])
# Restringindo os números à inteiros menores que a sequencia
    if sys.argv[2].isdigit():
        n1 = int(sys.argv[2])
    elif n1 > len(seq):
        sys.exit("Os números não podem ser maiores que a sequencia!")
	else:
        sys.exit("Digite uma sequencia e quatro números inteiros")
	if sys.argv[3].isdigit():
		n2 = int(sys.argv[3])
	elif n2 > len(seq):
        sys.exit("Os números não podem ser maiores que a sequencia!")
    else:
        sys.exit("Digite uma sequencia e quatro números inteiros")
	if sys.argv[4].isdigit():
		n3 = int(sys.argv[4])
	elif n3 > len(seq):
        sys.exit("Os números não podem ser maiores que a sequencia!")
    else:
        sys.exit("Digite uma sequencia e quatro números inteiros")
	if sys.argv[5].isdigit():
		n4 = int(sys.argv[5])
    elif n4 > len(seq):
        sys.exit("Os números não podem ser maiores que a sequencia!")	
	else :
		sys.exit("Digite uma sequencia e quatro números inteiros")
# Os éxons são obtidos por estas subsequencias
cds1 = seq[n1:(n2-1)]
cds2 = seq[n3:(n4-1)]
#Condicionando a formação da sequencia final e a mostrando
if "ATG" in cds1[0:3]:
	if "TAG" or "TAA" or "TGA" in cds[(n4-3):n4]:
		print(cds1 + cds2)
	else:
		print("os éxons não formam uma sequencia funcional")


