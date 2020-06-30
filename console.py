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
            print([str(value) for key, value in storage.all().items()])
            return
        if aux[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([str(value) for key, value in storage.all().items()
              if aux[0] == type(value).__name__])

    def do_update(self, line):
        """ Update an instace """
        aux = line.split()
        if not len(line):
            print("** class name missing **")
            return
        if aux[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(aux) == 1:
            print("** instance id missing **")
            return
        if len(aux) == 2:
            print("** attribute name missing **")
            return
        if len(aux) == 3:
            print("** value missing **")
            return
        keyWord = aux[0] + '.' + aux[1]
        if keyWord not in storage.all().keys():
            print("** no instance found **")
            return
        try:
            setattr(storage.all()[keyWord], aux[2], eval(aux[3]))
        except:
            setattr(storage.all()[keyWord], aux[2], aux[3])

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

    def default(self, line):
        """ Executes the process with the class name """
        lineSplited = line.split(".")
        className = lineSplited[0]
        command = lineSplited[1].split('(')[0]
        newLine = command + " " + className + " " + " "
        string = lineSplited[1].split('(')[1].replace(')', "").split(", ")
        argument = command + " " + className + " " + " " \
            .join(el.replace('"', "") for el in string)
        self.onecmd(argument)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
