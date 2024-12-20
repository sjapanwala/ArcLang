func;void eccheck $void {
  fi ( ?errorcode == 0 ) stdout \033[92mWorking Well 👍
  default stdout Somethings Wrong 👎
}

@eccheck
