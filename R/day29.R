additive_persistence = function(n){
  ans = 0
  while(nchar(n) > 1){
    n = sum(as.numeric(strsplit(format(n, scientific = FALSE),"")[[1]]))
    ans = ans + 1
  }
  return ( ans )
}


additive_persistence(1) == 0    #TRUE
additive_persistence(12) == 1   #TRUE
additive_persistence(1234) == 2 #TRUE
additive_persistence(199) == 3  #TRUE