import os.path
import sys
from src import Menu
from src import analyzer


def throw_error(error):
    print(error)
    exit()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # Open the GUI if no arguments are given
        # check if customtkinter is installed
        try:
            import customtkinter
        except ImportError:
            throw_error('Error: customtkinter is not installed. Please install it using the following command: '
                        'pip install customtkinter.')
        menu = Menu.Menu()
    elif len(sys.argv) == 2:
        # Run the script for the given path
        path = sys.argv[1]

        if os.path.exists(path) and os.path.isfile(path):
            analyzer.main(path, 'cli')
        else:
            throw_error('Error: Invalid path: [' + path + '].')
