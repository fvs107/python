import os


class FileGenerator:
    def __init__(self):
        pass

    def Start(self):
        self.make_initial_folders()
        self.create_files_per_folders()

    def make_initial_folders(self):
        os.mkdir('Pasta 1')
        os.mkdir('Pasta 2')
        os.mkdir('Pasta 3')
        os.mkdir('Pasta 5')

    def create_files_per_folders(self):
        base_directory = os.getcwd()
        os.chdir('Pasta 1')
        with open('texto.txt', 'w') as file:
            file.write('Boa noite turma')
            pass

        os.chdir(base_directory)
        os.chdir('Pasta 2')
        with open('texto.txt', 'w') as file:
            file.write('Boa noite turma')
            pass

        os.chdir(base_directory)
        os.chdir('Pasta 3')
        with open('texto.txt', 'w') as file:
            file.write('Boa noite turma')
            pass

        os.chdir(base_directory)
        os.chdir('Pasta 4')
        with open('texto.txt', 'w') as file:
            file.write('Boa noite turma')
            pass


generator = FileGenerator()
generator.Start()