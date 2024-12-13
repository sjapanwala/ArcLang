## Welcome To **ARC LANG 101**
- Arc Lang is a hobby language made by *Saaim Japanwala*
- An interpretor based lanage built in Python


### Get Started With ArcLang
You can either run the interpretor in `Console` mode by just typing `alang` or run a script with the ext `.al` by adding it as an arg
> [!IMPORTANT]
> Please follow these guidlines to write code that works 

- All keywords are case senstive and follow lowercase standards
- All code needs to be seperated by spaces, for it to be tokenized

### 1. Writing "Hello World"
in ArcLang, we dont have simple print statements, but we use the keyword `stdout`. this will print what ever will be provided in the tokens after. Since ArcLang does not use quotes to ID strings, stdout will aggregate everything that comes after.
```txt
CONSOLE INPUT  | !> stdout Hello World
CONSOLE OUTPUT | STDOUT Hello World
```

### 2. Defining Variables
ArcLang is type based, so everytime a variable is defined, a type is super important. Currently we have `strings` `intigers` `floats` `boolean` `arrays`

the code names for these are as followed,

| Type | ArcLang Code | 
|----------|----------|
| String | str | 
| Intiger | int |
| Float | flt |
| Boolean| bool |
| Arrays (lists) | arr |

to define a variable, we use the keyword `set` followed by the variable name, and equal sign, the variable value, along with the type. (if a type is not assigned, it will default to a string)

in this example, i define a variable called "location" and i seperate its value with an eq sign, after defining its value as "canada", I add a semicolon to seperate the value with its type
```txt
set location = canada;str
```
```txt
set x = 15;int          !> STDOUT 15
set y = 10;str          !> STDOUT "10"
set f = [1,2,3];arr     !> STDOUT [1,2,3]
```

### Accessing Variables
since ArcLang is not a quote based language, variables are accessed when the keyword `?` is placed at the start of the variable name with no space in between

```[]
CONSOLE INPUT  | stdout ?location
CONSOLE OUTPUT | STDOUT canada
```

### 3. Taking Inputs
Recieving inputs in ArcLang follows a simple yet concise pattern. Taking inputs also requires you define an expected type.

we take inputs with the keyword `stdin` similiar to `stdout`.

the token after the keyword is the name of the variable, also seperated with a semi colon. For stdin a type is required or else it will return an error; it will not default to string. after that what ever you type will be aggregated to be the prompt
```txt
CONSOLE INPUT  | stdin age;int What Is Your Age?
CONSOLE OUTPUT | STDOUT What Is Your Age?
```
what ever gets inputted by the end user, will be stored as a variable to be accessed later on with the same variable accessing keyword `?`

### 4. Doing Sum Math
Doing mathematical equations in ArcLang is possible by padding your equations in parenthesis `()`

```txt
( 1000 * 1 )  = 1000
```