from class_constant import Constant
from class_method import Method
from clear import clear_screen


if __name__ == '__main__':
    clear_screen()

    books = Method.load_data()

    while True:
        print('\n\nP Y T H O N'
              '\n\n    B O O K S'
              '\n\n        O  S E U  A C E R V O  D E  L I V R O S  D I G I T A L'
              '\n\n_________________________________________________________________________________________'
              '\n'
              '\n\n                               P Á G I N A  I N I C I A L                                '
              '\n'                                                               
              '\n\nAbaixo, encontra-se um conjunto de seis operações que podem ser realizadas em seu acervo.'
              '\n\nQual operação você deseja realizar?'
              '\n\n1. Alterar Dados    2. Buscar Livro    3. Registar Livro    4. Remover Livro    5. Visualizar Acervo'
              '    6. Sair')

        method = input('\nDigite o número que representa a operação escolhida por você e pressione ENTER.\n> ')

        method = Method.analyze_input(method, 'method', lower_limit=1, upper_limit=6)

        clear_screen()

        if method != Constant.EXIT():
            books = Method.execute(method, books)
        else:
            clear_screen()
            break

        print('\n\nVocê gostaria de continuar gerenciando seu acervo?'
              '\n\n1. Sim    2. Não')

        answer = input('\nDigite o número que representa a opção escolhida por você e pressione ENTER.\n> ')

        answer = Method.analyze_input(answer, 'answer', lower_limit=1, upper_limit=2)

        clear_screen()

        if answer == Constant.NO():
            break
