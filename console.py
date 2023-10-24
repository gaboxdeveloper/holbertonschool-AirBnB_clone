#!/usr/bin/python3
"""Console module"""
import cmd


if __name__ == '__main__':
    import cmd

    class HBNBCommand(cmd.Cmd):
        prompt = '(hbnb) '

        def do_quit(self, arg):
            """Exit the program"""
            return True

        def do_EOF(self, arg):
            """Exit the program (Ctrl+D)"""
            return True

        def emptyline(self):
            """Do nothing on an empty line"""
            pass

    HBNBCommand().cmdloop()
