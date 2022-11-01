#!/usr/bin/python3
import cmd
import re
from shlex import split
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

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Including a prompt
    """
    prompt = "(hbnb)"
    doc_header = 'Console_doc_header'
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

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
            storage.save()

    def do_all(self, args):
        """
        prints all string representation of all instances based
        or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        all = storage.all()
        new = args.split()
        if new[0] not in self.model:
            print("** class doesn't exist **")
        else:
            all2 = []
            for v in all().values():
                if len(new[1]) > 0 and new[0] == v.__class__.__name__:
                    all2.append(v.__str__())
                elif len(new) == 0:
                    all2.append(v.__str__())
            print(all2)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email
        Usage: update <class name> <id>
        <attribute name> "<attribute value>"
        """
        argl = args.split()
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in self.model:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
