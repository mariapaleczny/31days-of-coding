reverse_string = function(s){
  reversed = ""
  for (i in strsplit(s, split = "")[[1]]){
    reversed = paste(i, reversed, sep ="")
  }
  return ( reversed )
  }

#print(reverse_string("I did, did I?..."))