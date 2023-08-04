from class_book import Book
from class_constant import Constant
from class_file import File
from clear import clear_screen


class Method:
    @staticmethod
    def alter(books):
        print('\n\nVocê escolheu realizar alterações nas informações do registro de um livro.')

        edition, title = Method.__get_data_to('alter')

        book = Method.__linear_search(books, edition, title)

        if book is not None:
            # IF THE REFERENCE OF THE OBJECT IS NOT NONE, THEN
            #
            print('\n\nAntes de iniciar as alterações no registro deste livro, leia as informações abaixo.'
                  '\n'
                  '\n\n . Você pode realizar no máximo oito alterações.'
                  '\n\n    . Ao informar o número de alterações, digite sempre números inteiros entre 1 e 8.'
                  '\n\n    . Mesmo que um registro seja composto por sete campos de dados explícitos, você poderá '
                  'alterar também o número (implícito) de autores do livro.'
                  '\n\n    . Caso queria alterar o número de autores, não deixe de modificar também o(s) nome(s) do(s) '
                  'autor(es) do livro.'
                  '\n\n       . Esta ação é necessária para que a coerência entre as informações seja mantida.'
                  '\n\n . Você pode optar por não realizar alterações.'
                  '\n\n    . Neste caso, digite o número zero.'
                  '\n'
                  '\n\nQuantas alterações você deseja realizar?')

            changes = input('\nDigite o número correspondente e pressione ENTER.\n> ')

            changes = Method.analyze_input(changes, 'changes', lower_limit=0, upper_limit=8)

            clear_screen()

            if changes > 0:
                if changes < 8:
                    if changes > 1:
                        print(f'\n\nVocê escolheu realizar {changes} alterações.', end='')
                    else:
                        print('\n\nVocê escolheu realizar uma única alteração.', end='')

                    print(f'\n\nAbaixo, encontram-se listados – por número de indentificação – todos os campos que um '
                          f'registro pode apresentar.'
                          f'\n'
                          f'\n\n 1. Número de Autores'
                          f'\n\n 2. Nome(s) Completo(s) do(s) Autor(es)'
                          f'\n\n 3. Título (e Subtítulo) do Livro'
                          f'\n\n 4. Edição do Livro'
                          f'\n\n 5. Local da Publicação'
                          f'\n\n 6. Editora do Livro'
                          f'\n\n 7. Ano de Publicação'
                          f'\n\n 8. ISBN')

                    if changes > 1:
                        print(f'\n\nPara realizar as alterações, escolha os {changes} campos que serão modificados.'
                              f'\n\nEm seguida, digite na lista abaixo os números que correspondem a cada um deles e '
                              f'pressione ENTER.')
                    else:
                        print('\n\nPara realizar a alteração, escolha o campo que será modificado.'
                              '\n\nEm seguida, digite na lista abaixo o número que corresponde ao campo escolhido e '
                              'pressione ENTER.')

                    print('\n\nLista de Alterações', end='')
                else:
                    print('\n\nVocê escolheu realizar o número máximo de alterações no registro deste livro.'
                          '\n\nPreencha todos os oito campos com os dados necessários e siga as orientações que serão '
                          'apresentadas em alguns deles.')

                attributes = list()
                #
                # THIS LIST WILL CONTAIN THE ID. NUMBER OF EACH FIELD OR ATTRIBUTE THAT SHOULD BE ALTERED OR UPDATED
                # THROUGH THE METHOD '__set(attributes, book)'.

                for i in range(changes):
                    if changes < 8:
                        index = input(f'\n\n . Alterar Campo'
                                      f'\n\n    . Número de Ident.: ')

                        index = Method.analyze_input(index, 'index', lower_limit=1, upper_limit=8)

                        attributes.append(index)
                    else:
                        attributes.append(i + 1)

                if changes < 8:
                    clear_screen()

                    if changes > 1:
                        print(f'\n\nForam identificados {changes} campos em sua lista de alterações.'
                              f'\n\nPreencha cada um deles com os dados necessários e – se existirem – siga as '
                              f'orientações que serão apresentadas.')
                    else:
                        print('\n\nFoi identificado um único campo em sua lista de alterações.'
                              '\n\nFaça seu preenchimento adequadamente e – se existirem – siga as orientações '
                              'apresentadas por ele.')

                Method.__remove(book)  # REMOVE FROM THE FILE THE LINE THAT CONTAINS THE OUTDATED DATA OF THE BOOK.

                while True:
                    Method.__set(attributes, book)  # SET ALL THE UPDATED ATTRIBUTES OF THE BOOK OBJECT.

                    print('\n\nNão existem mais campos a serem preenchidos.'
                          '\n\nVocê deseja concluir a realização deste processo de alteração ou você deseja corrigí-lo?'
                          '\n\n1. Concluir    2. Corrigir')

                    option = input('\nDigite o número que representa a opção escolhida por você e pressione ENTER.\n> ')

                    option = Method.analyze_input(option, 'option', lower_limit=1, upper_limit=2)

                    clear_screen()

                    if option == Constant.CORRECT():
                        print('\n\nVocê escolheu realizar a correção do processo de alteração de dados.')

                        if changes < 8:
                            if changes > 1:
                                print(f'\nPreencha os {changes} campos do registro com os dados necessários e '
                                      f'– se existirem – siga as orientações que serão apresentadas.')
                            else:
                                print('\nPreencha o campo abaixo adequadamente e – se existirem – siga as orientações '
                                      'apresentadas por ele.')
                        else:
                            print('\nPreencha todos os oito campos com os dados necessários e siga as orientações que '
                                  'serão apresentadas em alguns deles.')
                    else:
                        Method.__write(Method.__get_attributes(book))  # WRITE IN THE FILE A LINE WITH THE UPDATED DATA.
                        break

                print('\n\nAs alterações foram realizadas com sucesso!')
            else:
                print('\n\nVocê optou por não realizar alterações.')
        else:
            print(f'\n\nTítulo: {title}'
                  f'\n\nEdição: {edition}'
                  f'\n'
                  f'\n\nO procedimento de alteração de informações não pôde ser realizado.'
                  f'\n\nSeu acervo não contém nenhum registro com o título e a edição deste livro.')

    @staticmethod
    def analyze_input(string, variable, lower_limit=-Constant.INF(), upper_limit=Constant.INF()):
        while True:
            if string.isnumeric():
                if int(string) < lower_limit or int(string) > upper_limit:
                    if variable == 'method':
                        print('\n\nVocê entrou com uma operação inválida.')
                    else:
                        if variable == 'answer' or variable == 'option':
                            print('\n\nVocê entrou com uma opção inválida.')
                        else:
                            if variable == 'changes' or variable == 'index' \
                                    or variable == 'len_authors' or variable == '__set_len_authors':
                                Method.__identify(variable)

                                print('Você entrou com um número inválido.')
                else:
                    break
            else:
                Method.__identify(variable)

                print('Você entrou com uma sequência inválida de caracteres.')

            string = Method.__get_input(variable)

        return int(string)

    @staticmethod
    def execute(method, books):
        if method == Constant.ALTER():
            Method.alter(books)
        else:
            if method == Constant.SEARCH():
                Method.search(books)
            else:
                if method == Constant.REGISTER():
                    books.append(Method.register())
                else:
                    if method == Constant.REMOVE():
                        books = Method.remove(books)
                    else:
                        if method == Constant.VIEW():
                            Method.view(books)

        return books

    @staticmethod
    def __get_attributes(book):
        return [
            str(book.len_authors),
            book.authors,
            book.title,
            book.edition,
            book.city,
            book.publisher,
            book.year,
            book.book_number
        ]

    @staticmethod
    def __get_data_to(method):
        print('\nEsta operação será feita a partir da obtenção dos dados referentes ao título e a edição do livro.')

        if method == 'alter':
            title = input('\nDigite o título do livro cujo registro você deseja alterar e pressione ENTER.\n> ')
        else:
            if method == 'remove':
                title = input('\nDigite o título do livro que você deseja remover do acervo e pressione ENTER.\n> ')
            else:
                title = input('\nDigite o título do livro que você quer encontrar e pressione ENTER.\n> ')

        clear_screen()

        print('\n\nEste livro possuí edição especificada?'
              '\n\n1. Sim    2. Não')

        answer = input('\nDigite o número que representa a opção escolhida por você e pressione ENTER.\n> ')

        answer = Method.analyze_input(answer, 'answer', lower_limit=1, upper_limit=2)

        clear_screen()

        if answer == Constant.YES():
            print(f"\n\nNo campo Edição, digite a edição do livro de acordo com o padrão 'N. ed.' e pressione ENTER."
                  f"\n\n . Título: {title}")

            edition = input(f'\n . Edição: ')
        else:
            edition = 'N.E'

        clear_screen()

        return edition, title

    @staticmethod
    def __get_input(variable):
        if variable == 'method':
            string = input('\nDigite um número que representa uma das seis operações foram apresentadas a você e '
                           'pressione ENTER.\n> ')
        else:
            if variable == 'answer' or variable == 'option':
                string = input('\nDigite um número que representa uma das duas opções que foram apresentadas a você e '
                               'pressione ENTER.\n> ')
            else:
                if variable == 'len_authors':
                    string = input('\nDigite um número inteiro positivo que corresponda à quantidade de autores do '
                                   'livro e pressione ENTER.\n> ')
                else:
                    if variable == '__set_len_authors':
                        string = input('\n   Digite um número inteiro positivo que corresponda à quantidade de autores '
                                       'do livro e pressione ENTER.'
                                       '\n   > ')
                    else:
                        if variable == 'changes':
                            string = input('\nDigite um número inteiro entre 1 e 8 que corresponda à quantidade de '
                                           'alterações que você deseja realizar e pressione ENTER.\n> ')
                        else:
                            string = input('\n      Digite um número de identificação que corresponda a um dos oito '
                                           'campos disponíveis para alteração.'
                                           '\n      > ')

        return string

    @staticmethod
    def __identify(variable):
        if variable == 'index':
            print('\n\n      ', end='')
        else:
            if variable == '__set_len_authors':
                print('\n\n   ', end='')
            else:
                print('\n')

    @staticmethod
    def __linear_search(books, edition, title):
        for book in books:
            if book.edition == edition and book.title == title:
                return book

        return None

    @staticmethod
    def load_data():
        books, lines = list(), File.read_lines()

        for line in lines:
            line = line.split(';')

            del line[len(line) - 1:]  # DELETE THE BLANK SPACE IN THE LAST INDEX OF THE LIST.

            len_authors, len_line = int(line[0]), len(line)  # THIS len(line) == PREVIOUS len(line) - 1

            authors, data = list(), [len_authors]

            if len_authors > 1:
                for index in range(1, len_authors + 1):
                    authors.append(line[index])  # ADD ALL THE AUTHORS TO THE LIST OF AUTHORS.
            else:
                authors.append(line[1])  # ADD THE ONLY AUTHOR TO THE LIST.

            data.append(authors)

            for index in range(len_authors + 1, len_line):
                data.append(line[index])  # GET THE REMAINING DATA OF THE LINE.

            books.append(Book(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
            #            Book(len_authors, authors, title, edition, city, publisher, year, book_number)

        return books

    @staticmethod
    def __print_data_of(book):
        if book.len_authors > 1:
            print('\n . Autores')
        else:
            print('\n . Autor')

        for author in book.authors:
            print(f'    . {author}\n')

        print(f' . Título'
              f'\n    . {book.title}')
        print(f'\n . Edição'
              f'\n    . {book.edition}')
        print(f'\n . Local da Publicação'
              f'\n    . {book.city}')
        print(f'\n . Editora'
              f'\n    . {book.publisher}')
        print(f'\n . Ano de Publicação'
              f'\n    . {book.year}')
        print(f'\n . ISBN'
              f'\n    . {book.book_number}')

    @staticmethod
    def register():
        print('\n\nVocê escolheu realizar o registro de um livro em seu acervo digital.')

        while True:
            data = list()

            print('\nQuantos autores o livro possuí?')

            len_authors = input('\nDigite o número correspondente e pressione ENTER.\n> ')

            len_authors = Method.analyze_input(len_authors, 'len_authors', lower_limit=1)

            data.append(str(len_authors))

            clear_screen()

            print('\n\n Ficha Técnica do Livro – Registro de Dados')

            authors = list()

            if len_authors > 1:
                print('\n\n . Nomes Completos dos Autores')

                for i in range(len_authors):
                    author = input(f'\n      {i + 1}. Nome: ')
                    author = author.strip(';')

                    authors.append(author)
            else:
                author = input('\n\n . Nome Completo do Autor: ')
                author = author.strip(';')

                authors.append(author)

            data.append(authors)

            print('\n\n . Título (e Subtítulo) do Livro'
                  '\n\n      . No campo a seguir, escreva título e subtítulo (se houver) seguindo o padrão '
                  "'Título: Subtítulo'.")

            title = input('\n\n      . Nome do Livro: ')

            data.append(title)

            print('\n\n . Edição do Livro'
                  "\n\n      . Este campo deve ser preenchido conforme o padrão 'N. ed.', no qual N é o número da "
                  "edição."
                  '\n\n      . Caso o livro não tenha sua edição especificada, preencha o campo a seguir com a sigla '
                  'N.E (Não-Especificada).')

            edition = input('\n\n      . Edição: ')

            data.append(edition)

            print('\n\n . Local da Publicação'
                  '\n\n      . Este campo deve ser preenchido somente com o nome da cidade em que o livro foi '
                  'publicado.'
                  '\n\n      . Não preencha este campo com informações como estado ou país.')

            city = input('\n\n      . Cidade: ')

            data.append(city)

            publisher = input('\n\n . Editora do Livro: ')

            data.append(publisher)

            year = input('\n\n . Ano de Publicação: ')

            data.append(year)

            book_number = input('\n\n . ISBN: ')

            data.append(book_number)

            print('\n\nNão existem mais campos a serem preenchidos.'
                  '\n\nVocê deseja concluir a realização deste registro ou você deseja corrigi-lo?'
                  '\n\n1. Concluir    2. Corrigir')

            option = input('\nDigite o número que representa a opção escolhida por você e pressione ENTER.\n> ')

            option = Method.analyze_input(option, 'option', lower_limit=1, upper_limit=2)

            clear_screen()

            if option == Constant.CORRECT():
                print('\n\nVocê escolheu realizar a correção do registro.')
            else:
                Method.__write(data)  # WRITE IN THE FILE ALL THE DATA COLLECTED ABOUT THE BOOK.
                break

        print('\n\nO registro foi realizado com sucesso!')

        return Book(len_authors, authors, title, edition, city, publisher, year, book_number)

    @staticmethod
    def remove(books):
        print('\n\nVocê escolheu remover um livro de seu acervo digital.')

        edition, title = Method.__get_data_to('remove')

        book = Method.__linear_search(books, edition, title)

        if book is not None:
            # IF THE REFERENCE OF THE OBJECT IS NOT NONE, THEN
            #
            Method.__remove(book)  # REMOVE FROM THE FILE THE LINE THAT CONTAINS THE DATA OF THE FOUND BOOK.

            del books[books.index(book)]  # REMOVE THE BOOK FROM THE LIST OF BOOKS.

            print('\n\nO livro foi removido com sucesso!')
        else:
            print(f'\n\nTítulo: {title}'
                  f'\n\nEdição: {edition}'
                  f'\n'
                  f'\n\nO livro não pôde ser removido.'
                  f'\n\nSeu acervo não contém nenhum registro com o título e a edição deste livro.')

        return books

    @staticmethod
    def __remove(book):
        data = str()

        attributes = Method.__get_attributes(book)

        for attribute in attributes:
            if not isinstance(attribute, list):  # IF THE ATTRIBUTE IS NOT AN INSTANCE OF LIST
                data += attribute + ';'
            else:
                for author in attribute:
                    data += author + ';'

        File.remove(data + '\n', File.read_lines())

    @staticmethod
    def search(books):
        print('\n\nVocê escolheu buscar por um livro em seu acervo digital.')

        edition, title = Method.__get_data_to('search')

        book = Method.__linear_search(books, edition, title)

        if book is not None:  # IF THE REFERENCE OF THE OBJECT IS NOT NONE, THEN THE BOOK WAS FOUND.
            print('\n\nO livro foi encontrado!'
                  '\n'
                  '\n\n Ficha Técnica'
                  '\n')

            Method.__print_data_of(book)
        else:
            print(f'\n\nTítulo: {title}'
                  f'\n\nEdição: {edition}'
                  f'\n'
                  f'\n\nO livro não foi encontrado.'
                  f'\n\nSeu acervo não contém nenhum registro com o título e a edição deste livro.')

    @staticmethod
    def __set(attributes, book):
        print('\n\n Ficha Técnica do Livro – Alteração de Dados')

        for attribute in attributes:
            if attribute == Constant.LEN_AUTHORS():
                len_authors = input('\n\n . Número de Autores: ')

                book.len_authors = Method.analyze_input(len_authors, '__set_len_authors', lower_limit=1)
            else:
                if attribute == Constant.AUTHORS():
                    authors = list()

                    if book.len_authors > 1:
                        print('\n\n . Nomes Completos dos Autores')

                        for i in range(book.len_authors):
                            author = input(f'\n      {i + 1}. Nome: ')
                            author = author.strip(';')

                            authors.append(author)
                    else:
                        author = input('\n\n . Nome Completo do Autor: ')
                        author = author.strip(';')

                        authors.append(author)

                    book.authors = authors
                else:
                    if attribute == Constant.TITLE():
                        print('\n\n . Título (e Subtítulo) do Livro'
                              '\n\n      . No campo a seguir, escreva título e subtítulo (se houver) seguindo o padrão '
                              "'Título: Subtítulo'.")

                        book.title = input('\n\n      . Nome do Livro: ')
                    else:
                        if attribute == Constant.EDITION():
                            print('\n\n . Edição do Livro'
                                  "\n\n      . Este campo deve ser preenchido conforme o padrão 'N. ed.', no qual N é "
                                  "o número da edição."
                                  '\n\n      . Caso o livro não tenha sua edição especificada, preencha o campo a '
                                  'seguir com a sigla N.E (Não-Especificada).')

                            book.edition = input('\n\n      . Edição: ')
                        else:
                            if attribute == Constant.CITY():
                                print('\n\n . Local da Publicação'
                                      '\n\n      . Este campo deve ser preenchido somente com o nome da cidade em que '
                                      'o livro foi publicado.'
                                      '\n\n      . Não preencha este campo com informações como estado ou país.')

                                book.city = input('\n\n      . Cidade: ')
                            else:
                                if attribute == Constant.PUBLISHER():
                                    book.publisher = input('\n\n . Editora do Livro: ')
                                else:
                                    if attribute == Constant.YEAR():
                                        book.year = input('\n\n . Ano de Publicação: ')
                                    else:
                                        book.book_number = input('\n\n . ISBN: ')

    @staticmethod
    def view(books):
        print(f'\n\nVocê escolheu visualizar seu acervo digital.')

        registers = len(books)

        if registers > 0:
            if registers > 1:
                print(f'\nNo momento, ele apresenta um total de {registers} livros registrados.')
            else:
                print('\nNo momento, ele apresenta um único livro registrado.')

            print('\n\n Lista de Livros do Acervo')

            index = 1

            for book in books:
                print(f'\n\n {index}.')

                Method.__print_data_of(book)

                index += 1
        else:
            print('\nNo momento, ele encontra-se vazio.')

    @staticmethod
    def __write(data):
        for index in range(len(data)):
            if index != 1:
                File.write(data[index])
            else:
                for author in data[index]:
                    File.write(author)

        File.new_line()
