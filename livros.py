class Livros:
    def __init__(self, nome, autor, ano_pub, status):
        self.autor = autor
        self.ano_pub = ano_pub
        self.status = status
        self.nome = nome
    
    
    def status_livros (self, status):

        if status == 'Disponível':
            print ('O livro está disponível')
        
        else:
            print ('O livro foi emprestado')

lista_livros = []
lista_emprestados = []
lista_disponiveis = []

class Biblioteca(Livros):
    def __init__ (self, nome, autor, ano_pub, status):
        self.autor = autor
        self.ano_pub = ano_pub
        self.status = status
        self.nome = nome
    
    def adicionar_livros (titulo):
        lista_livros.append(titulo)
        print(' ')
        print('Livro adicionado!')
        print(' ')
        lista_disponiveis.append(titulo)
    
    
    def emprestar_livros (titulo):
        lista_emprestados.append(titulo)
        print(' ')
        print('Status  do livro ', titulo, ' mudado para Emprestado.' )
        print(' ')
        lista_disponiveis.remove(titulo)
    
    def devolver_livros (titulo):
        lista_disponiveis.append(titulo)
        print(' ')
        print('O livro ', titulo, ' agora está disponível.')
        print(' ')
        lista_emprestados.remove(titulo)

    def mostrar_livros (self):
        print(' ')
        print('Estes são os livros da nossa biblioteca: ' )
        print(lista_livros)
        print(' ')
    
    def ver_emprestados ():
        print('Lista de emprestados: ')
        print(lista_emprestados)

    def ver_disponiveis():
        print('Lista de disponíveis: ')
        print (lista_disponiveis)
