#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ The command interpreter for Bnb """
    prompt = '(hbnb) '
    classes = {"BaseModel", "User", "State", "City", "Place",
               "Amenity", "Review"}

    def do_create(self, line):
        """ Creates an object of certain class """
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        newObjects = eval(line)()
        print(newObjects.id)
        newObjects.save()

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        if not len(line):
            print("** class name missing **")
            return
        aux = line.split()
        if aux[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(aux) < 2:
            print("** instance id missing **")
            return
        if aux[0] + '.' + aux[1] not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            print(storage.all()[aux[0] + '.' + aux[1]])

    def do_destroy(self, line):
        """
            Destroy the string representation of an instance
            based on the class name and id
        """
        if not len(line):
            print("** class name missing **")
            return
        aux = line.split()
        if aux[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(aux) < 2:
            print("** instance id missing **")
            return
        if aux[0] + '.' + aux[1] not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[aux[0] + '.' + aux[1]]
        storage.save()

    def do_all(self, line):
        """ Prints all the objects """
        aux = line.split()
        if not len(line):
            print([objects for objects in storage.all().values()])
            return
        if aux[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([objects for objects in storage.all().values()
            if strings[0] == objects.__class__.__name__])



    def help_quit(self):
        """ Prints the help for the quit """
        print("Quit command to exit the program")

    def emptyline(self):
        """ Do nothing """
        pass

    def do_EOF(self, line):
        """ Get out of the cmd """
        print("")
        return True

    def do_quit(self, line):
        """ Exit the aplication """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
