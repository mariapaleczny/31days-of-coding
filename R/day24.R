is_geometric = function(x){
  if(length(x)<2){ return ( TRUE ) }
  divided=c()
  for(i in 2:length(x)){
    divided = c(divided, x[i]/x[i-1])
  }
  return ( length(unique(divided)) == 1 )
}

print(is_geometric(c(2,3,5))) #FALSE
print(is_geometric(c(2,4,8))) #TRUE
print(is_geometric(0))     #TRUE

