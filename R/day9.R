mid = function(word){
  len = nchar(word)
  if (len %% 2 == 1){
    print(substr(word, ceiling(len/2), ceiling(len/2)))
  } else {
    print("")
  }
}

mid("tesTing")