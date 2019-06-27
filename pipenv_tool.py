import os
import sys

print(sys.executable)
print(sys.version)


class Text:
    a = '''
    1 = update/sync pipenv --skip-lock option

    2 = install a module with --skip-lock option

    3 = get list of virtualenvs

    4 = shell

    '''
    b = '\n'

class Pipenv:

    pipenv_path = ''
    actual_path = ''

    def updatepipenv(self):
        os.chdir(Pipenv.pipenv_path)
        os.system('python3 -m pipenv install --skip-lock')

    def install(self):
        mod_to_install = input('which module?  ')
        os.chdir(Pipenv.pipenv_path)
        os.system('python3 -m pipenv install {} --skip-lock'.format(mod_to_install))
        print(b)

    def getlist(self):
        os.chdir(actual_path)
        a = os.listdir()   
        for x in a:
            b = x.split('-')
            print(b)

    def shell(self):
        os.chdir(Pipenv.pipenv_path)
        os.system('python3 -m pipenv shell')

    def main(self):
        choice = input(Text.a)
        if choice == '1':
            print(Text.b)
            self.updatepipenv()

        elif choice == '2':
            print(Text.b)
            self.install()

        elif choice == '3':
            print(Text.b)
            self.getlist()

        elif choice == '4':
            print(Text.b)
            self.shell()


if __name__ == '__main__':
    pipenv = Pipenv()
    pipenv.main()

