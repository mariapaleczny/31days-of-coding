move_zero = function(x){
  return ( c(x[x!=0],x[x==0]) )
}

print(move_zero(c(1,2,3)))
print(move_zero(c(0,1,0,2)))


