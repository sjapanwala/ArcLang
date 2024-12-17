func;int add $void {
  stdin a;int first number:
  stdin b;int second number:

  set x = ( ?a + ?b )
  return ?x
  end 1
}


set result = @add
stdout -------------- 
stdout RESULT = ?result
stdout -------------- 

