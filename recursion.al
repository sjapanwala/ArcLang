func;int main $a;int {
  fi ( $a > 0 ) stdout hello world
  fi ( $a < 0 ) exit
  set x = @decre $a
  return @main ?x
}


func;int decre $a;int {
  return ( $a - 1 )
}

set y = @main 15

stdout ?y

