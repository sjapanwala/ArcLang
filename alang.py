#!/usr/bin/env python3
import subprocess, getpass, os, time
from os import sys
from os import system

variables = {
        "errorlevel" : {
            "type": "int",
            "value": 0
            },
        "uname" : {
            "type": "str",
            "value": getpass.getuser()
            },
        "verion": {
            "type": "flt",
            "value": 0.1
            },
        "sysupdt": {
            "type": "str",
            "value": "www.github.com/sjapanwala"
            }
        }

math_operators = ("+","-","*","/","//","%")

def tokenization(user_input):
    """
    precedence list:
        variables = ?var = is a var
        spaces = _hello or he_llo = this adds a space
        math 
    """
    try:
        token_array = user_input.split(" ")
        for i,token in enumerate(token_array):
            # check for precedence
            if "?" in token[0]:
                recovered = deVar(token)
                token_array[i] = recovered
            if "_" in token:
                a,b = add_space(token)
                token_array[i] = f"{a} {b}"
            if "(" in token:
                token_array = do_math(token_array)
        return token_array
    except Exception as e:
        return ["undefined"]

file_contents = []

def open_file(filename):
    with open(filename, "r") as file:
        for line in file:
            file_contents.append(line.strip())
    run_file(file_contents)

def run_file(file_contents):
    for codeline in file_contents:
        tokenizer = tokenization(codeline)
        func_caller(tokenizer)

def func_caller(tokens):
    if "showtokens" in tokens:
        print(tokens)
    user_input = tokens[0]
    if user_input in globals() and callable(globals()[user_input]):
        globals()[user_input](list(tokens[1:]))
    else:
        print(f"\033[91merror: \033[0mthe command '{user_input}' is not recognized")

def type_check(value):
    if isinstance(value, int):
        return "int"
    elif isinstance(value, str):
        return "str"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, list):
        return "arr"  
    else:
        return "?" 

def add_space(chunk):
    sp_idx = chunk.find("_")
    return chunk[:sp_idx], chunk[sp_idx+1:]

def deVar(variable):
    if variable[1:] in variables:
        var_val = variables[variable[1:]]["value"]
        var_type = variables[variable[1:]]["type"]
        if var_type == "str":
            return str(var_val)
        elif var_type == "int":
            return int(var_val)
        elif var_type == "arr":
            var_val = list(var_val)
            return var_val
        elif var_type == "bool":
            return bool(var_val)
        else:
            return "\033[90mUndefined\033[0m"
    else:
        return "\033[90mUndefined\033[0m"


def varlist(a):
    print(variables)

def set(tokens):
    """
    set x = "hello world"
    set y = 10;int

    values can be categorized as (str,int,flt,bool,arr) by adding a semicolon after the value
    but if no value types are added, it will be auto typed

    expected input:
        tokens (arr) -> ["set","x","=","10;int"]
    return value (int): this is the error code
        if successful:
            return 0
        else:
            return 1
    """
    if "=" not in tokens:
        return 0
    else:
        eq_place = tokens.index("=")
        var_key = tokens[eq_place-1]
        var_valueraw = tokens[eq_place+1]
        
        # Check if there is a semicolon and process accordingly
        if var_valueraw.find(";") > -1:
            semi_idx = var_valueraw.find(";")
            var_val = var_valueraw[:semi_idx]
            var_type = var_valueraw[semi_idx+1:]
        else:
            var_val = var_valueraw
            var_type = type_check(var_val)

        # Store the variable in the variables dictionary
        variables[var_key] = {
            "type": var_type,
            "value": var_val
        }
    
def stdout(tokens):
    """
    stdout aggregates everything in the list, so no use for quotes
    to add a space you need to add a "_", this is done in the tokenizer
    also adds spaces after every index
    expected:
    ["hello","world"] -> helloworld
    """
    phrase = ""
    try:
        for i in tokens:
            if len(phrase) > 1:
                phrase += " "
            phrase += str(i)
        print(f"\033[33mSTDOUT \033[0m{phrase}")
        return 0
    except Exception as e:
        return 1


def stdin(tokens):
    """
    This is essentially the same as defining a variable, but this will be taken as real-time input
    instead of a set value. It follows typing as "stdin myVar;int please add your age"
    where:
    - var_key is "myVar"
    - var_type is int
    - it will ask the user "please add your age"
    """
    if not tokens:
        print("\033[91merror: \033[0mplease add expected params")
        return 1

    var_keyraw = tokens[0]
    
    if var_keyraw.find(";") == -1:
        print("\033[91merror: \033[0mno type specified")
        return 1

    try:
        semi_idx = var_keyraw.find(";")
        var_key = var_keyraw[:semi_idx]
        var_type = var_keyraw[semi_idx+1:]
        
        var_types = ["str","int","bool","arr"]
        if var_type not in var_types:
            print("\033[91merror: \033[0minvalid type provided")
            return 1

        phrase = " ".join(tokens[1:])
        
        var_val = input(f"\033[33mSTDIN \033[0m{phrase} ")
        
        if not var_val:
            var_val = "not specified"
        variables[var_key] = {
            "type": var_type,
            "value": var_val
        }

        return 0

    except Exception as e:
        print(f"\033[91merror: \033[0m{str(e)}")
        return 1

def clear(void):
    os.system("clear")
    return 0

def do_math(tokens):
    first = tokens.index("(")
    last = len(tokens) - 1 - list(reversed(tokens)).index(")")
    eq = eval("".join(tokens[first + 1:last]).replace(" ", ""))
    tokens[first] = eq 
    del tokens[first + 1:last + 1]
    return tokens

def main():
    if len(sys.argv) > 1:
        open_file(sys.argv[1])
    else:
        command = ""
        while command.lower() != "exit":
            command = input(f"console> ")
            tokens = tokenization(command)
            func_caller(tokens)
if __name__ == "__main__":
    main()
