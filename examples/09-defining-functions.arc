stdout You Cant See Anything! Please View The Source Code in A Text Editor
// defining functions is used with keyworkd "func"
// follow this format,

// func;{returntype} {func_name} ${variable/void};{var_type} {
// function content
// {if returntype != void; needs return}
// }

// this is a function that adds two values

func;int addition $a;int $b;int {
  return ( $a + $b )
}

// the return type for this function is an intiger
// name the function "addition"
// we define 2 arguements "$a" and "$b" both need to be int
// since we have an int return type, we HAVE to have a return line

func;void hello! $void {
  stdout Hello ?uname !
  end 0
}

// replaced return type and variable with void
// void will make them have "no type"
// so no return type is required
// "end" in optional, returns an error code 


