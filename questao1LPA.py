print('-='*19)
print('BEM-VINDO A LOJA DO JOÃO PEDRO PEREIRA')
print('-='*19)
 # solicita ao usuario quen entre com o valor do produto e a quantidade desejada do respectivo produto.
valor=float(input('digite o valor do produto desejado: ')) # valor do tipo float pois valores contem numeros quebrados.
quantidade=int(input('digite a quantidade desejada do produto: ')) # quantidade do tipo inteiro pois não contem numeros quebrados como  valores.
print('>'*41)
# aqui estou calculando a multiplicação do para saber o valor total sem descontos. 
total_sem_desconto=valor*quantidade
#declarei a variavel desconto do tipo float, mas é algo opcional, eu preferi fazer. 
desconto:float
#aqui estou fazendo o calculo das condições, para saber qual desconto aplicar ou se o produto não tera descontos.

if total_sem_desconto < 2500:
    desconto=0 # se, valor total sem o desconto fo menor que 2500, o produto não tera descontos.
    
elif total_sem_desconto < 6000:
    desconto=0.04 # senão se, o valor total sem descontos for menor que 6000, logo ele automaticamente sera maior ou igual a 2500, aplicando assim o desconto de 4%.
    
elif total_sem_desconto < 10000:
    desconto=0.07 # senão se, o valor total sem descontos for menor que 10000, logo ele automaticamente sera maior ou igual a 6000, aplicando assim o desconto de 7%.
    
else:
    desconto=0.11 # senão, se todas as condições a cima forem falsas o valor lagicamente sera igual ou superior a 10000, aplicando assim o desconto maximo de 11%.
    
valor_total_com_desconto=total_sem_desconto*(1-desconto) # calculo para saber qual sera o valor do produto ja com o desconto aplicado.

print('O valor total sem o desconto é: R${:.2f}'.format(total_sem_desconto)) # e por fim, os respectivos valores, com e sem desconto.
print('O valor total com o desconto é: R${:.2f}'.format(valor_total_com_desconto))