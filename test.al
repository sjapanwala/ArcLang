func;void main $a;int {
  fi ( $a == 0 ) stdout done
  set y = $a
  let x;int
  set x = ( ?y - 1 )
  stdout ?x
}

@main 1
