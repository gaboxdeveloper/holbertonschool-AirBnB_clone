#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for the console"""
    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
        }
    
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Exit the program (Ctrl+D)"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = self.__classes[arg]()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """show info of the instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return


    def do_all(self, arg):
        if arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(f"")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
