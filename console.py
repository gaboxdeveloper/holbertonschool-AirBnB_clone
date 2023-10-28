#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class for the console"""
    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'State': State,
        'User': User,
        'Review': Review,
        '': ''
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
        else:
            keys = args[0] + '.' + args[1]
            if keys not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[keys].__str__())

    def do_destroy(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        if arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            class_name = self.__classes[arg]
            for key, value in objects.items():
                print(value)

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            attr_value_str = args[3]
            obj = objects[key]
            if key not in objects:
                print("** no instance found **")
            else:
                if hasattr(obj, args[2]):
                    attr_type = type(getattr(obj, args[2]))
                else:
                    print("** instance has no attribute {} **".format(args[2]))
                try:
                    attr_value = attr_type(attr_value_str)
                except ValueError:
                    print(f"** invalid {args[2]} value **")
                    return
                setattr(obj, args[2], attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
