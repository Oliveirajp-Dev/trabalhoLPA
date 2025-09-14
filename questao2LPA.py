print('-='*37)
print('|OLÁ, SEJA BEM-VENDO A LOJA DE GELADOS DO JOÃO PEDRO PEREIRA DE OLIVEIRA |') # menssagem de boas vindas.
print('-='*37)
print(' -'*10, 'CARDÁPIO','- '*10 )
print(' -'*25) 
print('-'*3,'| Tamanho','| Cupuaçu (CP) |  Açai (AC) |','-'*3) # opções do cardapio.
print('-'*3,'|    P   ','|   R$ 9.00    |  R$ 11.00  |','-'*3)
print('-'*3,'|    M   ','|   R$ 14.00   |  R$ 16.00  |','-'*3)
print('-'*3,'|    G   ','|   R$ 18.00   |  R$ 20.00  |','-'*3)
print(' -'*25)
total_pedido=0 # variavel acumuladora, para somar e acumular valores dentro do loop.
continuar_pedido=True  #variavel booleana 
while continuar_pedido: # loop principal com o valor da variavel booleana, dizendo que enquanto esta variavel for verdade o loop continuara em execução.
    sabor_desejado=input('Digite o sabor desejado ( CP/AC ):')
    
    # aqui estou verificando as condições de sabor, preço e tamanho
    if sabor_desejado != 'cp' and sabor_desejado != 'ac':
        print('sabor invalido. tente novamente')
        continue
    tamanho=input('digite o tamanho desejado ( P/M/G) :')
    if tamanho != 'p' and tamanho != 'm' and tamanho !='g':
        print('tamanho invalido, tente novamente')
        continue
    if sabor_desejado == 'cp':
        nome='cupuaçu'   # aqui estou definindo o nome de acordo com á opção desejada, para que não apareça no console somente CP, e sim o nome correspondete a opção, de uma forma que fica mais entendivel.
        if tamanho == 'p':
            preco=9.00
        elif tamanho =='m':
            preco=14.00
        else:
            preco=18.00
    if sabor_desejado == 'ac':
        nome='açai'
        if tamanho == 'p':
            preco=11.00
        elif tamanho== 'm':
            preco=16.00
        else:
            preco=20.00
    print('voce pediu um {} no tamanho {}: R$ {:.2f}'.format(nome, tamanho,preco)) # aqui irá exibir o pedido do cliente, com todos os dados escolhidos por ele.
    
    total_pedido+=preco #variavel acumuladora que calculando o valor do pedido de acordo com o preço do produto desejado e da quantidade.
    while True: # laço secundario, criado para verificar a resposta se ela é sim ou não e retornando, caso a resposta seja diferente de sim ou não (S/N), caso o cliente digite outra coisa por engano ou descuido, ele retornará a pergunta se ele deseja mais alguma coisa ou se não e encerrar o programa.
        resposta=input('deseja mais alguma coisa? (S/N):')
        if resposta == 's':
            break # a resposta sendo sim, o loop se encerra e retorna para o loop principal, para pondendo assim ser feito outros pedidos.
        elif resposta == 'n':
            print('total a ser pago:{:.2f}'.format(total_pedido))
            print('volte sempre!')
            continuar_pedido=False
            break # verificando a resposta for Não, exibindo assim o total a ser pago,e uma menssagem de volte sempre, e encerrando assim o loop principal.        
        else:
            print('opção invalida!') # se caso a resposta for diferente de (S/N) como ja citado a cima, o programa vai exibir uam mensagem de opção invalida e retornara a pergunta se deseja algo.
            
print('FIM DO PROGRAMA!!!')