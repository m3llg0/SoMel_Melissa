import livros
        
aux = True

print('Sistema de Gestão de Biblioteca')
print(' ')

while aux == True:
    print('1 - Adicionar livro')
    print('2 - Emprestar livro')
    print('3 - Devolver livro')
    print('4 - Mostrar lista de livros')
    print('5 - Mostrar lista de livros emprestados')
    print('6 - Mostrar lista de livros disponíveis')
    print('7 - Sair')
    op = int(input('Selecione uma opção: '))
    
    if op == 7:
        aux = False
        break
    
    elif op == 1:
        titulo_ = str(input('Digite o nome do livro: '))
        autor_ = str(input('Digite o nome do autor do livro: '))
        ano_pub_ = int(input('Digite o ano da publicação do livro: '))
        status_ = 'Disponível'
        novo_livro = livros.Livros(titulo_ , autor_ , ano_pub_, status_)
        livros.Biblioteca.adicionar_livros(titulo_)
        

    elif op == 2:
        titulo_ = str(input('Digite o nome do livro que deseja emprestar: '))
        status_ = 'Disponível'
        livros.Biblioteca.emprestar_livros(titulo_)

    elif op == 3:
        titulo_ = input('Digite o nome do livro que deseja devolver: ')
        livros.Biblioteca.devolver_livros(titulo_)

    elif op == 4:
        livros.Biblioteca.mostrar_livros(titulo_)
    
    elif op == 5:
        livros.Biblioteca.ver_emprestados()
    
    elif op == 6:
        livros.Biblioteca.ver_disponiveis()
    
    else:
        print('Opção inválida')
