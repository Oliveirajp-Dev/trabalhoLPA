print('-='*28)
print('|bem vindo a copiadora do JOÃO PEDRO PEREIRA DE OLIVEIRA|') # menssagem de boas vindas
print('-='*28)


def escolha_serviço(): # função de escolha de serviço
    while True:
        global preco# variavel acumuladora para calcular o preço dos serviços
        serviço=input('ENTRE COM O TIPO DE SERVIÇO DESEJADO:\nDIG - digitação\nICO - impressão colorida\nIPB - impressão preto e branco\nFOT - fotocópia\n>>')
        if serviço != 'dig' and serviço!= 'ico' and serviço != 'ipb' and serviço!= 'fot': # verificando as condições de entrada se são verdadeiras, retornando a menssagem escolha invalida caso o usuario digite algo diferennte das opções.
            print('XXX  escolha invalida, entre com o tipo de serviço novamente.')
            continue
        elif serviço == 'dig': # verificando se a entrada é igual e algum dos serviços prestados pela copiadora, e mostrando o nome do serviço
            nome='digitação'
            preco= 1.10
             # variavel acumuladora + o preço do serviço desejado 
            print('o valor do serviço {} por pagina é R${:.2f}'.format(nome,preco)) # imprimindo os dados de acordo com o serviço escolhido, nome e o preço por paginas.
        elif serviço == 'ico':
            nome='impressão colorida'
            preco= 1.00
            
            print('o valor do serviço {} por pagina é R${:.2f}'.format(nome,preco))
        elif serviço == 'ipb':
            nome='impressão preto e branco'
            preco= 0.40
            
            print('o valor do serviço {} por pagina é R${:.2f}'.format(nome,preco))
        elif serviço == 'fot':
            nome='fotocopia'
            preco = 0.20
            
            print('o valor do serviço {} por pagina é R${:.2f}'.format(nome,preco))
        break
            
         # retornando o valor da variavel acumuladora, com o valor do serviço escolhido, para que esse valor possa ser usada fora da função para realizar o calculo final.
            
def num_pagina(): # função para o numero de paginas
    while True:
        global pagina
        try:  # utilizado para tratar um possivel erro, caso o usuario entre por exemplo com algum caracter que nao seja um numero, para que o codigo não quebre e sim mostre uma menssagem de aviso, para o usuario digitar um numero, que no caso é um numero inteiro.
            pagina=int(input('DIGITE O NUMERO DE PAGINÁS:'))
            if pagina < 20:
                pagina=pagina
            elif pagina<200:
                desconto=0.15
                pagina-=pagina*desconto
            elif pagina < 2000:
                desconto=0.20
                pagina-=pagina*desconto
            elif pagina < 20000:
                desconto =0.25
                pagina-=pagina*desconto
            elif pagina >=20000:
                print('não aceitamos tantas paginas de uma vez')
                print('entre novamente com a quantidade de paginas:')
                continue 
            break
            
        except(ValueError):
            print('digite apenas numeros') # menssagem de aviso, para o usuario digitar apenas numeros.

def serviço_extra(): # função de serviço extra 
    while True:
        preco_extra=0 # variavel acumuladora
        try:
            print('--'*19)
            extra=int(input('DESEJA ADICIONAR MAIS ALGUM SERVIÇO? :\n1 - ENCADERNAÇÃO SIMPLES - R$15.00\n2 - ENCADERNAÇÃO CAPA DURA - R$40.00\n0 - NÃO DESEJO MAIS NADA\n>>'))
            if extra != 1 and extra!= 2 and extra!= 0: # verificando as entradas, se são validas e repetindo a pergunta com o loop caso a entrada seja diferente de alguma das opções listadas.
                print('Opção invalida, tente novamente.')
                continue # repetindo o loop com  a pergunta.
            elif extra == 1:
                preco_extra=15.00 # variavel acumuladora com o valor do serviço
            elif extra == 2:
                preco_extra=40.00
            else:
                preco_extra = 0 # caso o usuario não deseje mais nada e queira sair, a variavel acumuladora não recebe valores e se mantem com o  valor padrão de zero, não alterando assim em nada no valor do calculo final.
            return preco_extra
        except(ValueError):
            print('opçao invalida')
     #programa principal 

escolha_serviço()  # chamando a função de serviço escolhido e o  valor da variavel correspondente para realizar o calculo final.
num_pagina()
# preco_extra=serviço_extra()
total=preco*pagina

print('total:R${:.2f} (serviço: {:.2f} * paginás: {:.2f})'.format(total,preco,pagina))