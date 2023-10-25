#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for the console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)

    def do_EOF(self, arg):
        """Exit the program (Ctrl+D)"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
