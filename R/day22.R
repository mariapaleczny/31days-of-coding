perfectly_balanced = function(word){
  w = as.list(strsplit(word, "")[[1]])
  return ( length(w[w=="x"])==length(w[w=="y"]) )
}

print(perfectly_balanced("xxyy"))
print(perfectly_balanced("xyx"))


