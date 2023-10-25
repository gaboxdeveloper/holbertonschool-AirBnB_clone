#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for the console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Exit the program (Ctrl+D)"""
        return True

    def emptyline(self) -> bool:
        return super().emptyline()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
