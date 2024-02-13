#!/usr/bin/python3

"""
    cmd module for building line oriented command interpreters
"""

import cmd
from models.base_model import BaseModel
from models import storage
import re

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

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

    def do_create(self, line):
        """  Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            object = self.CLASSES[class_name]()
            object.save()
            print(object.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()
        # objects = storage.all()

        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
