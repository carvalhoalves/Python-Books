class File:
    @staticmethod
    def new_line():
        with open('books.txt', 'a') as Text_File:
            Text_File.write('\n')

    @staticmethod
    def read_lines():
        with open('books.txt', 'r') as Text_File:
            return [line for line in Text_File.readlines()]

    @staticmethod
    def remove(string, lines):
        with open('books.txt', 'w') as Text_File:
            for line in lines:
                if line != string:
                    Text_File.write(line)

    @staticmethod
    def write(string):
        with open('books.txt', 'a') as Text_File:
            Text_File.write(string + ';')
