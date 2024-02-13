#!/usr/bin/python3

"""
    CMD MODULE
    for building line oriented command interpreters
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    CLASSES = {
            'BaseModel': BaseModel
    }

    def emptyline(self):
        """This should do nothing on an empty line"""
        pass

    def do_EOF(self, line):
        """ Exits the program"""
        print()
        return True

    def do_quit(self, line):
        """ Quits the console"""
        True

if __name__ == '__main__':
    HBNBCommand().cmdloop()