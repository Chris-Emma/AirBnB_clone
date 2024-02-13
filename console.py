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
        """This shouls do nothing on an empty line"""
        pass

    def do_EOF(self, line):
        """ Exits the console when EOF command is entered"""
        print()

    def do_quit(self, line):
        """ Quits the console"""
        True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
