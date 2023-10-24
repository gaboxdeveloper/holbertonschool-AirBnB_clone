#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for the console"""
    prompt = "(hbnb) "

    def do_quit(self):
        """Exit the program"""
        return True

    def do_EOF(self):
        """Exit the program (Ctrl+D)"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
