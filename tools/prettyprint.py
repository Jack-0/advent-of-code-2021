#!/bin/python3.9
"""
Pretty Print

A simple tool to print information in a pretty way to the terminal
"""

class PrettyPrint:
    # ANSI colors
    COLOR_RESET = '\033[0m'
    COLOR_CYAN = '\033[0;36m'
    COLOR_YELLOW = '\033[1;33m'
    COLOR_RED = '\033[1;31m'
    def __init__(self):
        return

    def p(self, color:str, label:str, msg:str, sub_msg:str=""):
        print(color + label + PrettyPrint.COLOR_RESET + str(msg))
        if sub_msg != "":
            print(color + "[....] " + PrettyPrint.COLOR_RESET + sub_msg)

    def info(self, msg:str, sub_msg:str=""):
        self.p(PrettyPrint.COLOR_CYAN, "[INFO] ", str(msg), sub_msg)

    def warn(self, msg:str, sub_msg:str=""):
        self.p(PrettyPrint.COLOR_YELLOW, "[WARN] ", str(msg), sub_msg)

    def debug(self, msg:str, sub_msg:str=""):
        self.p(PrettyPrint.COLOR_RED, "[DBUG] ", str(msg), sub_msg)
