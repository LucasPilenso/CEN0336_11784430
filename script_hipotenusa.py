#!/usr/bin/env python3

import sys # requisito para as funções sys

#Restrição para aceitar apenas entradas com a quantidade certa de argumentos
if len(sys.argv) < 3 or len(sys.argv) > 3:
	sys.exit("Digite DOIS números")
#Aplicando as condições e declarando as variáveis a e b
if len(sys.argv) == 3:
    if sys.argv[1].isdigit():
        a = int(sys.argv[1])
        if  a > 499 or a < 1:
            sys.exit("Os números devem ser positivos menores que 500")
    else:
        sys.exit("Os números devem ser inteiros positivos menores que 500")
    if sys.argv[2].isdigit():
        b = int(sys.argv[2])
        if b > 499 or b < 1:
            sys.exit("Os números devem ser positivos menores que 500")
    else:
        sys.exit("Os números devem ser inteiros")
#A operação utilizada para o resultado contida na variável c e a exibição do resultado
c = (a ** 2 + b ** 2)
print("O quadrado da hipotenusa para o triangulo retângulo com lados X=", a," e Y=", b , "é Z=", c)


