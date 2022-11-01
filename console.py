#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

"""
Console 0.0.1
This contains the interaction of our code with the
Interprator
"""

class HBNBCommand(cmd.Cmd):
    """
    Including a prompt
    """
    prompt = "(hbnb)"
    doc_header = 'Air Bnb help clone center'
    misc_header = 'Console_misc_header'
    undoc_header = 'Console_undoc_header'
    ruler = '-'
    model = ["BaseModel", "User", "Place",
             "State", "City", "Amenity", "Review"
             ]

    def emptyline(self):
        """If not overriden it repeats the last empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")
    
    def default(self, args):
        """
        User.all()
        <classname>.all()
        """
        clsname, mthd = args.split(".")
        m = re.match('*(^[^(]+)', mthd)

        if mthd == 'all()':
            self.do_all(clsname)
        if mthd == 'count()':
            self.do_count(clsname)
        if mthd == 'show()':
            self.do_show(m,)
        
    def do_quit(self, args):
        """Exit using quit method"""
        return True

    def do_EOF(self, args):
        """Exit using EOF"""
        return True

    def do_create(self, args):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        Ex: $ create BaseModel
        """
        arg1 = args.split()
        if len(arg1) == 0:
            print("class name missing **")
        elif arg1[0] not in self.model:
            print("** class doesn't exist **")
        else:
            new_id = eval("{}().id".format(arg1[0]))
            print(new_id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        <show BaseModel 1234-1234-1234>
        """
        all = storage.all()
        new = args.split()
        if len(new) == 0:
            print("** class name missing **")
        elif new[0] not in self.model:
            print("** class doesn't exist **")
        elif len(new) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new[0], new[1]) not in all:
            print("no instance found")
        else:
            print(all["{}.{}".format(new[0], new[1])])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        all = storage.all()
        new = args.split()
        if len(new) == 0:
            print("** class name missing **")
        elif new[0] not in self.model:
            print("** class doesn't exist **")
        elif len(new) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new[0], new[1]) not in all:
            print("no instance found")
        else:
            del all["{}.{}".format(new[0], new[1])]


    def do_all(self, arg):
        """
        prints all string representation of all instances based
        or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        all = storage.all()
        if arg not in self.model:
            print("** class doesn't exist **")
        else:
            all2 = []
            for v in all.values():
                if arg == v.__class__.__name__:
                    all2.append(v)    
            print(all2)

    def do_update(self, args):
        """
        (hbnb) <classname> <id> <attr_name> <new_value>
        """
        all = storage.all()
        params = args.split(" ")
        clsname = params[0]
        clsid = params[1]
        attr = params[2].replace('"', "")
        new_val = params[3].replace('"', "")
        if len(params) == 0:
            print("** class name missing **")
        elif clsname not in self.model:
            print("** class doesn't exist **")
        elif len(params) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(clsname,clsid) not in all:
            print("** no instance found **")
        elif len(params) == 1:
            print("** value missing **")
        else:
            found = None
            for obj in all.values():
                found = obj
                break
            if found is not None:
                setattr(found, attr, new_val)
                storage.save()

    def do_count(self,arg):
        ct = 0
        for v in storage.all().values():
            if v.__class__.__name__ == arg:
                ct += 1
        print(ct)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
