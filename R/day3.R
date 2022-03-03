reverse_string = function(s){
  reversed = ""
  for (i in strsplit(s, split = "")[[1]]){
    reversed = paste(i, reversed, sep ="")
  }
  print(reversed)
  }

reverse_string("I did, did I?...")