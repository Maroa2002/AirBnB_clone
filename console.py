#!/usr/bin/python3
import cmd

"""The console module"""


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
