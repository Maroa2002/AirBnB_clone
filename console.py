#!/usr/bin/python3
"""The console module"""

import cmd
from models import storage
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def emptyline(self):
        """called if empty line is entered
        it does nothing"""

        pass

    def do_quit(self, arg):
        """command to exit the program"""

        return True

    def do_EOF(self, arg):
        """Exits the program at EOF"""

        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""

        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """prints the string representation of an instance
        based on the class name and id"""

        if len(arg) == 0:
            print("** class name missing **")
            return
        class_names = shlex.split(arg)
        if class_names[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if class_names[1]:
                name = "{}.{}".format(class_names[0], class_names[1])
                if name not in storage.all().keys():
                    print("* no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""

        if len(arg) == 0:
            print("** class name missing **")
            return

        class_names = shlex.split(arg)
        if class_names[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if class_names[1]:
                name = "{}.{}".format(class_names[0], class_names[1])
                if name not in storage.all().keys():
                    print("* no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""

        class_names = shlex.split(arg)
        obj_li = []
        if len(arg) == 0:
            for objects in storage.all().values():
                obj_li.append(objects)
            print(obj_li)
        elif class_names[0] in HBNBCommand.classes:
            for key, objects in storage.all().items():
                if class_names[0] in key:
                    obj_li.append(objects)
            print(obj_li)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)."""

        class_names = shlex.split(arg)
        if len(class_names) >= 4:
            key = "{}.{}".format(class_names[0], class_names[1])

            arg_3 = class_names[3]
            arg_3 = arg_3.strip('"')
            arg_3 = arg_3.strip("'")

            if "." in arg_3:
                cast = float
            elif arg_3.isdigit():
                cast = int
            else:
                cast = str

            setattr(storage.all()[key], class_names[2], cast(arg_3))
            storage.all()[key].save()
        elif len(class_names) == 0:
            print("** class name missing **")
        elif class_names[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(class_names) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(class_names[0], class_names[1]))\
                not in storage.all().keys():
            print("** no instance found **")
        elif len(class_names) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
