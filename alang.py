#!/usr/bin/env python3
import subprocess, getpass, os, time
from os import sys
from os import system
import operator

variables = {
        "errorlevel" : {
            "cat": "preset",
            "type": "int",
            "value": 0
            },
        "uname" : {
            "cat": "preset",
            "type": "str",
            "value": getpass.getuser()
            },
        "version": {
            "cat": "preset",
            "type": "flt",
            "value": 0.1
            },
        "readme": {
            "cat": "preset",
            "type": "str",
            "value": "Access The Readme Here: https://www.github.com/sjapanwala/ArcLang"
            },
        "x" : {
            "cat": "assigned",
            "type": "int",
            "value": 11
            },
        "y" : {
            "cat": "assigned",
            "type": "int",
            "value": 10
        }
    }


def tokenization(user_input):
    """
    precedence list:
        variables = ?var = is a var
        spaces = _hello or he_llo = this adds a space
        math 
    """
    try:
        if not user_input:
            return None
        token_array = user_input.split(" ")
        for i,token in enumerate(token_array):
            # check for precedence
            if "?" in token[0]:
                recovered = deVar(token)
                token_array[i] = recovered
            if "_" in token:
                a,b = add_space(token)
                token_array[i] = f"{a} {b}"
        if "(" in token_array:
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
    if tokens == None:
        return 1
    if "showtokens" in tokens:
        print(tokens)
    user_input = tokens[0]
    if isinstance(user_input, str):
        if user_input[0] == "!":
            quick_commands(user_input)
            return 0
    if user_input in globals() and callable(globals()[user_input]):
        error_code = globals()[user_input](list(tokens[1:]))
        return error_code
    else:
        print(f"\033[91merror: \033[0mthe command '{user_input}' is not recognized")
        return 1

def type_check(value):
    if isinstance(value, int):
        return "int"
    elif isinstance(value, str):
        return "str"
    elif isinstance(value, float):
        return "flt"        
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
        elif var_type == "flt":
            return float(var_val)
        elif var_type == "bool":
            return bool(var_val)
        else:
            return "\033[90mUndefined\033[0m"
    else:
        return "\033[90mUndefined\033[0m"


def varlist(void):
        print("\033[93mAll Initialized Variables:\033[0m\n")
        max_key_length = max(len(str(key)) for key in variables)
        max_type_length = max(len(str(variables[key]['type'])) for key in variables)
        max_value_length = max(len(str(variables[key]['value'])) for key in variables)
        max_cat_length = max(len(str(variables[key]['cat'])) for key in variables)
        format_string = f"{{:<{max_key_length}}}    {{:<{max_cat_length}}}    {{:<{max_type_length}}}     {{:<{max_value_length}}}    "
        print(format_string.format("Variable","IsModify",  "Type", "Value"))
        print(format_string.format("________","______", "____", "_____\n"))
        show_val = ""
        show_mod = ""
        for key in variables:
            if len(str(variables[key]["value"])) > 10:
                show_val = f"{variables[key]['value'][:10]}..."
            else:
                show_val = f"{variables[key]['value']}"
            if str(variables[key]['cat']) == "preset":
                show_mod = "False"
            else:
                show_mod = "True"
            print(format_string.format(
                str(key), 
                str(show_mod),
                str(variables[key]['type']), 
                str(show_val)
            ))
        return 0
def varcheck(void):
    if void[0] in variables:
        print("\033[93mVariable Information:\033[0m\n")
        key_length = max(len(void[0]), len("Variable"))
        type_length = max(len(str(variables[void[0]]['type'])), len("Type"))
        value_length = max(len(str(variables[void[0]]['value'])), len("Value"))
        cat_length = max(len(str(variables[void[0]]['cat'])), len("isModify"))
        cat_val = ""
        if variables[void[0]]['cat'] == "preset":
            cat_val = "False"
        else:
            cat_val = "True"


    
        header_format = f"{{:<{key_length}}}    {{:<{cat_length}}}    {{:<{type_length}}}     {{:<{value_length}}}    "
        value_format = f"{{:<{key_length}}}    {{:<{cat_length}}}    {{:<{type_length}}}     {{:<{value_length}}}    "
    
        print(header_format.format("Variable", "isModify","Type", "Value"))
        print(header_format.format("________", "______", "____", "_____\n"))
    
        print(value_format.format(
            void[0], 
            cat_val,
            variables[void[0]]['type'], 
            variables[void[0]]['value']
        ))
        return 0
    else:
        print(f"\033[91merror: \033[0mvariable \033[91m'{void[0]}'\033[0m not found")
        return 1

def quick_commands(user_input):
    help = """
    Welcome To ArcLang \033[92m0.1\033[0m
    
    ArcLang is a basic interpretor built in Python3 for a custom build language.
    for help with how to write code, please visit the README.md by typing '!readme'

    Basic Usage:
        interpretor commands always start with an exclamation mark, with the keyword no space.
            "!help"

        variables can be defined with the keyword "set"
            "set x = 10;int"
                or
            "const x = 10;int"
                or
            "let x;int"


        variables are accessed with a question mark, with the variable name no space.
            example: "?x"

        lines can be output with the keyword "stdout"
            example: "stdout hello world"

        lines can be input with the keyword "stdin"
            example: "stdin myVar;int please add your age"

        ...for more indepth help please visit the README.md by typing '!readme'
        """

    if user_input == "!help":
        print(help)
    elif user_input == "!readme":
        a = subprocess.run(
                ["curl", "https://raw.githubusercontent.com/sjapanwala/ArcLang/refs/heads/main/README.md"],
                capture_output=True,  # Capture output
                text=True             # Ensure output is returned as a string)
            )
        print(a.stdout)  # This prints the content of the file



def do_math(tokens):
    operator_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
        '//': operator.floordiv,
        '==': operator.eq,
        '!=': operator.ne,
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
    }

    # Step 1: Process parentheses (if any)
    while '(' in tokens:
        # Find the innermost parentheses
        first = tokens.index('(')
        last = len(tokens) - 1 - list(reversed(tokens)).index(')')
        
        # Evaluate the expression inside the parentheses
        sub_tokens = tokens[first + 1:last]
        result = do_math(sub_tokens)  # Recursive call for nested expressions
        
        # Replace the parentheses with the result
        tokens[first] = result[0]
        del tokens[first + 1:last + 1]

    # Step 2: Process operators (left-to-right for simplicity)
    i = 0
    while i < len(tokens):
        if tokens[i] in operator_map:
            # Perform the operation and replace the operands and operator
            result = operator_map[tokens[i]](int(tokens[i - 1]), int(tokens[i + 1]))
            tokens[i - 1:i + 2] = [result]
            i -= 1  # Adjust index to account for reduced list size
        else:
            i += 1

    return tokens

# -- everything before is the actual working sections of the interpretor -- #
# -- everything after this line is the interpretor commands -- #

def set(tokens):
    """
    set x = "hello world"
    set y = 10;int

    values can be categorized as (str,int,flt,bool,arr) by adding a semicolon after the value
    but if no value types are added, it will be auto typed. the set command is used to define variables
    that can be changed; meaning they are mutable

    expected input:
        tokens (arr) -> ["set","x","=","10;int"]
    return value (int): this is the error code
        if successful:
            return 0
        else:
            return 1
    """
    allowed_types = ["str","int","flt","bool","arr"]
    if "=" not in tokens:
        print("\033[91merror: \033[0mplease add expected params")
        return 0
    else:
        eq_place = tokens.index("=")
        if not tokens[eq_place+1]:
            print("\033[91merror: \033[0mplease add expected params")
            return 1
        if not tokens[eq_place-1]:
            print("\033[91merror: \033[0mplease add expected params")
            return 1
        var_key = tokens[eq_place-1]
        if var_key in variables:
            if variables[var_key]["cat"] == "preset":
                print("\033[91merror: \033[0mvariable cannot be rewritten")
                return 1
        var_valueraw = tokens[eq_place+1]
        
        # Check if there is a semicolon and process accordingly
        if isinstance(var_valueraw, int):
            var_val = var_valueraw
            var_type = type_check(var_val)

        elif var_valueraw.find(";") > -1:
            semi_idx = var_valueraw.find(";")
            var_val = var_valueraw[:semi_idx]
            var_type = var_valueraw[semi_idx+1:]
        else:
            var_val = var_valueraw
            var_type = type_check(var_val)

        if var_type not in allowed_types:
            print("\033[91merror: \033[0minvalid type")
            return 1

        cat_val = "assigned"

        variables[var_key] = {
            "cat": cat_val,
            "type": var_type,
            "value": var_val
        }
        return 0

def const(tokens):
    """
    const x = "hello world"
    const y = 10;int

    values can be categorized as (str,int,flt,bool,arr) by adding a semicolon after the value
    but if no value types are added, it will be auto typed. the const command is used to define variables
    that cannot be changed; meaning they are not mutable

    expected input:
        tokens (arr) -> ["const","x","=","10;int"]
    return value (int): this is the error code
        if successful:
            return 0
        else:
            return 1
    """
    allowed_types = ["str","int","flt","bool","arr"]
    if "=" not in tokens:
        return 0
    else:
        eq_place = tokens.index("=")
        var_key = tokens[eq_place-1]
        if var_key in variables:
            if variables[var_key]["cat"] == "preset":
                print("\033[91merror: \033[0mvariable cannot be rewritten")
                return 1
        if not tokens[eq_place+1]:
            print("\033[91merror: \033[0mplease add expected params")
            return 1
        var_valueraw = tokens[eq_place+1]
        
        if isinstance(var_valueraw, int):
            var_val = var_valueraw
            var_type = type_check(var_val)
        elif var_valueraw.find(";") > -1:
            semi_idx = var_valueraw.find(";")
            var_val = var_valueraw[:semi_idx]
            var_type = var_valueraw[semi_idx+1:]
        else:
            var_val = var_valueraw
            var_type = type_check(var_val)

        if var_type not in allowed_types:
            print("\033[91merror: \033[0minvalid type")
            return 1

        cat_val = "preset"

        variables[var_key] = {
            "cat": cat_val,
            "type": var_type,
            "value": var_val
        }
        return 0

def let(tokens):
    """
    create a varible without assigning a value, these values are mutable, but they can be turned into consts later
    a let variable cannot be defined for a variable that already exists

    like this,
    let x;int

    expected input:
        tokens (arr) -> ["let","x;type"]
    return value (int): this is the error code
        if successful:
            return 0
        else:
            return 1
    """
    if len(tokens) < 1:
        print("\033[91merror: \033[0mplease add expected params")
        return 1
    var_key_raw = tokens[0]
    if var_key_raw.find(";") == -1:
        print("\033[91merror: \033[0mplease add expected params")
        return 1
    semi_idx = var_key_raw.find(";")
    var_key = var_key_raw[:semi_idx]
    if var_key in variables:
        print("\033[91merror: \033[0mvariable already has value")
        return 1
    var_type = var_key_raw[semi_idx+1:]
    cat_val = "assigned"
    variables[var_key] = {
        "cat": cat_val,
        "type": var_type,
        "value": "undefined"
    }
    return 0 


    
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
    except:
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
        if var_key in variables:
            if variables[var_key]["cat"] == "preset":
                print("\033[91merror: \033[0mvariable cannot be rewritten")
                return 1
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
            "value": var_val,
            "cat" : "assigned"
        }

        return 0

    except Exception as e:
        print(f"\033[91merror: \033[0m{str(e)}")
        return 1

def clear(void):
    try:
        os.system("clear")
        return 0
    except:
        return 1


def main():
    if len(sys.argv) > 1:
        open_file(sys.argv[1])
    else:
        try:
            print("""
    Welcome To ArcLang \033[92mv1.12/2024\033[0m
    for help please type "!help", or !readme.
    to exit session press ctrl+c or type "exit"
    Created by: \033[94msjapanwala\033[0m
            """)
            returncode = 0
            while True:
                command = ""
                while command.lower() != "exit":
                    if returncode != 0:
                        rc = "\033[91m!\033[0m"
                    else:
                        rc = "\033[92m!\033[0m"
                    command = input(f"\n\033[33mArcLang {rc}\033[0m> ")
                    tokens = tokenization(command)
                    returncode = func_caller(tokens)
        except KeyboardInterrupt:
            print("\rArcLang Session Ended; Goodbye")
            exit(1)
if __name__ == "__main__":
    main()
