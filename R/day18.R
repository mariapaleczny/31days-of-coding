all_equal_one = function(l){
  return ( length(unique(l)) == 1 )
}

all_equal = function(l){
  first = l[1]
    for(i in 2:length(l)){
      if (l[i]!=first){
        return ( FALSE )
      }
    return ( TRUE )
  }
}

all_equal_one(c(1,1,1))
all_equal(c(1,1,1))
all_equal_one(c("a","b"))
all_equal(c("a","b"))

