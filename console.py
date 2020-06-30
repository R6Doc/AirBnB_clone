#!/usr/bin/python3
""" Module for base class """


import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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

    def do_update(self, arg):
        """Update an instance based on class, attr, id, etc"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

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
