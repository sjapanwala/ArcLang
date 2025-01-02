Welcome To Arc Tutor, Here We Will Help You Learn ArcLang Programming Language.

What is Arclang?
  ArcLang is an interpretor based language, runs during realtime and isnt compiled.
  ArcLang can be ran inside the terminal, 
  or write a file with the file extention of ".al" and pass it as an argument to run it.\

  Licences Under MIT:
  Copyright (c) 2024 Saaim Japanwala

Commands:

      IC  |  !help      shows the help menu
      IC  |  !teach     shows this menu
      FC  |  varlist    lists all the variables
      FC  |  varcheck   check the existance of a variable
      FC  |  funclist   shows all registered functions
      FC  |  set        sets a variable;mutable
      FC  |  const      sets a variable;immutable
      FC  |  let        sets a undefined variable;mutable
      FC  |  stdout     prints to console
      FC  |  stdin      takes an input from the console; into a var
      FC  |  clear      clears the console
      FC  |  exit       exits the program
      FC  |  func       defines a function
      FC  |  fi         is the equal to `if`
      FC  |  elsefi     is the equal to `else if`
      FC  |  default    is the equal to `else`
      FC  |  //         adds comments
      FC  | numceil     rounds float numbers with provided sig digs
      FC  | repeat      loops down to an iteration
      FC  | rand        provides a random value (min,max)




Pre Defined Vars:

  ?pi           |   Pi Value       |   3.14
  ?eu           |   Eulars Value   |   2.72
  ?errorlevel   |   Return Value   |   0/1
  ?uname        |   Username       |   ?uname
  ?version      |   Version Name   |   ?version
  ?iteration    |   Loops Iter Val |   starts 0
  ?rand         |   Random Val     |   1-100

Status Codes:

  0   |   Neutral
  1   |   Ambiguous Error
  2   |   Avoidance
  3   |   Type Error
  4   |   Syntax Error


Lessons: 

    How To Write ArcLang:


    Lesson 1: Defining a variable

    - variables can be defined in ways that tend to the usage you need.
    different variable keywords are responsible for diffderent attributes.

    1. set
    - set is the original variable keyword and is used for mutable variables.
    - you can assign a variable type for this, if no type is assigned,
    it will default to a string.
    - no quotes are required since, we use types and symbols to diffrenciate

    with this example below, we have created some variables for a user

    ```alang
    set name = user;str
    set age = 37;int
    set isMale = true;bool
    set classes = ["CS","Math","Physics"];arr
    ```

    2. const
    - consts are the immutable versions of 'set'
    - once a variable is defined using 'const' it cannot be changed in runtime
    - follows the same rules as 'set', except its immutable

    ```alang
    const name = user;str
    const age = 37;int
    const isMale = true;bool
    const classes = ["CS","Math","Physics"];arr
    ```

    3. let
    - let is the undefined variable keyword
    - let is used for mutable variables
    - let is used for variables that are not defined yet; that will be expecting a value
    - let does not have an auto type detect
    - a type needs to be assigned for this variable to be used correctly or else it will error

    ```alang
    let name;str
    let age;int
    let isMale;bool
    let classes;arr
    ```

    Lesson 2: Interacting with the user through the console

    1. stdout
    - stdout is used to print to the console
    - stdout can be used to print any type of variable or string that is defined
    - does not require a type
    - aggregates everything so no need for quotes

    - to print variables, you need to add the question mark symbol at the start

    ```alang
    ?name # will print the value of name
    ````

    ```alang
    stdout ?name
    stdout ?age
    stdout ?isMale
    stdout ?classes
    ```

    2. stdin
    - stdin is used to take an input from the console
    - stdin defined a variable that the input on the console will store
    - requires a type to be assigned, will be the expected types

    follow this format
    ```alang
    stdin {variablename};{type} {prompt}
    ```

    the prompt will be aggregated so no need for quotes

    ```alang
    stdin userAge;int what is your age?
    ```

    Lesson 3: Math and logic

    - mathematical operators can be used in Arclang to evalute logic and math
    - all operations and logic is evaluated from left to right (no bedmas)
    - all logic is ecaluated inside parenthesis

    - to set a variable to be the output of a math expression, types arent required
    ```alang
    set sum = (2 + 2)
    const PiE = ( 3.14 * 2.17 )
    set isEven = (6 % 2)
    ```

    Lesson 4: if else and ifelse statements

    - these statements are here to handle logic
    - `fi`      -> is the equal to `if`
    - `elsefi`  -> is the equal to `else if`
    - `default` -> is the equal to `else`

    ```alang
    fi ( ?x % 2 == 0 ) stdout ?x is even
    elsefi ( ?x % 2 == 1 ) stdout ?x is odd
    default stdout ?x is not a number
    ```

    Lesson 5: Functions

    - functions are to speed repeptative tasks
    - functions are defined like so
    - function args need to be defined with the prefix $ -> reserves for func vars
    - if a return type if not void; it needs to return values or else it wont run

    ```alang
    func;{returntype} {funcname} {params} {
      // code here


      return {value} // this will return the value that was defined earlier in header
      end 0          // this will end the function with a return code (0/1; or custom)
    }
    ```

    Function are called by adding an @ symbol at the start

    ```alang
    @{funcname} {args}
    ```

    variables can store values that functions return from the function call
    return codes are auto stored in the errorcode register
    if no errorcode is returned, it will default to 1

    this is a simple addition function

    ```alang
    func;int add $void {        // this is the header; return an int; no params
      stdin a;int First Number  // this is the first input
      stdin b;int Second Number // this is the second input

      return (a + b)            // this is the return value
      end 0                     // returning an ec of 0
    }
    ```

    ```alang
    set sum = @add
    
    [CONSOLE]
    First Number: 1
    Second Number: 2

    stdout ?sum

    3

    ```
    Lesson 6: Iteration Loops

    using the `repeat` function, we can use loops.
    ```alang
    repeat 5 {
      stdout Hello!
    }
    ```
    this will repeat 5 times!

   


