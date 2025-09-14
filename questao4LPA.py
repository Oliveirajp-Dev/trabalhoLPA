print('\n','>'*5,'|Bem vindo a BIBLIOTECA João pedro pereira de oliveira|','<'*5,'\n')
 # menssagem de boas vindas com meu nome

lista_livro=[] # lista vazia para armazenar os livros cadastrados
id_global=0 # variavel acumuladora para controlar o ID de cada livro adicionado

def cadastrar_livro(id): # função para cadastrar livros
    print('-'*15, 'MENU CADASTRAR LIVRO', '-'*15)
    id+=1 # idicionando o ID do livro para que comece em 1
    print(f'id do livro: {id}')
    nome_livro=input('digite o nome do livro que deseja cadastrar: ') # dados dos livros que forem ser cadastrados
    nome_autor=input('digite o nome do autor do livro que deseja cadastrar: ')
    nome_editora=input('digite o nome da editora do livro que deseja cadastrar: ')
    print('-'*55)
    
    livro={ # dicionario para armazenar os dados dos livros adicionados
        'id':id,
        'nome':nome_livro,
        'autor': nome_autor,
        'editora': nome_editora
    }
    lista_livro.append(livro) #adicionando o livro cadastrado a lista de livros
    return id # retornado o ID para o programa principal
    
    
def consultar_livro(): # função para consultar livros
    while True: # menu de consulta com todas as opções de consulta disponivel
        print('\n','-'*15, 'MENU CONSULTAR LIVRO', '-'*15,'\n')
        try:
            opcao=int(input('Qual a opção desejda:\n1 - CONSULTAR TODOS OS LIVROS \n2 - CONSULTAR LIVRO POR ID\n3 - CONSULTAR LIVRO(S) POR AUTOR\n4 - RETORNAR\n>>> '))
            if opcao==1: # condição para consultar todos os livros cadastrados
                for livro in lista_livro:
                    print(f'id: {livro['id']}\nnome: {livro['nome']}\nautor: {livro['autor']}\neditora: {livro['editora']}')
                    
            elif opcao == 2: # condição para consultar por ID 
                while True:
                    procura_id=False # variavel booleana, iniciando em false, e caso o ID digitado seja verdadeiro, ela recebe o valor true e encerra o laço, e é exibido o livro correspondente ao ID digitado, caso o ID digitado não corresponda a nenhum ID da lista de livros, o programa exibe a mensagem de id nao encontrado e o laço se repete, e o programa repete a pergunta
                    id=int(input('digite o ID do livro: '))
                    for livro in lista_livro:
                        if livro['id'] == id:
                            print(f'id: {livro['id']}\nnome: {livro['nome']}\nautor: {livro['autor']}\neditora: {livro['editora']}')
                            procura_id=True
                    if procura_id == True:
                        break
                                
                    else:
                         print('ID nao encontrado')
                        
                            
            elif opcao== 3: # condição para consulta por nome do autor
                while True:
                    procura_autor=False # variavel booleana, mesma coisa da condição 2
                    autor=input('digite o nome do autor do(s) livro(s): ')
                    for livro in lista_livro:
                        if livro['autor'] == autor:
                            print(f'id: {livro['id']}\nnome: {livro['nome']}\nautor: {livro['autor']}\neditora: {livro['editora']}')
                            procura_autor=True
                    if procura_autor == True:
                        break
                    else:
                        print('autor não encontrado!')
                        
            
            elif opcao ==4: # condição de retorno ao menu principal
                break
            else:
                print('opção invalida, tente novemente')
                continue
        
            
        except(ValueError):
            print('digite uma das opções validas')
            
            
def remover_livro(): # funçaõ para remover livros da lista
    while True:
        try:
            remove=False # variavel booleana, iniciando em false, mesmo exemplo das consultas por ID e AUTOR
            print('\n','-'*15, 'MENU REMOVER LIVRO', '-'*15,'\n')
            remover=int(input('digite o ID do livro que deseja remover: '))
            for livro in lista_livro:
                if livro['id']== remover:
                    lista_livro.remove(livro)
                    print('livro removido com sucesso!')
                    remove=True
            if remove==True:
                break
            else:
                print('ID não encontrado')
            
        except(ValueError):
            print('digite apenas numeros')
    
                   
        
      #programa principal 
while True:
    print('-'*15, 'MENU PRINCIPAL', '-'*15)
    try: # menu de  opções do programa principal, com todas as opções disponiveis
        escolha=int(input('escolha a opção desejada:\n1 - CADASTRAR LIVRO\n2 - CONSULTAR LIVRO(S)\n3 - REMOVER LIVRO\n4 - SAIR\n>>>'))
        if escolha == 1:
            cadastrar_livro(id_global) # chama a função de cadastrar livros
            id_global+=1 # aumenta o id global apos cada cadastro
        elif escolha == 2:
            consultar_livro()
        elif escolha == 3:
            remover_livro()
        elif escolha == 4:
            print('encerrando')
            break
        else:
            print(' opção invalida')
    except(ValueError):
        print('digite uma opção valida')

        
        
        