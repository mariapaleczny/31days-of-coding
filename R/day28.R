
digit_adder = function(n){
  ans = ""
  for(i in as.numeric(strsplit(as.character(n),"")[[1]])){
    ans = paste(ans, i+1, sep ="")
  }
  print(as.numeric(ans))
}


digit_adder(998)