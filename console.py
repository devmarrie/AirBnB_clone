#!/usr/bin/python3

import cmd

"""
Console 0.0.1
"""

class HBNBCommand(cmd.Cmd):
    """
    Including a prompt
    """
    prompt = "(hbnb)"
    
    def emptyline(self):
        """If not overriden it repeats the last empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_quit(self, args):
        """Exit using quit() method"""
        print("Quitting")
        raise SystemExit
    
    def do_EOF(self, args):
        """Exit using EOF"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    
    

