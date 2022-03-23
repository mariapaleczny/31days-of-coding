is_ugly = function(x){
  for(i in c(2,3,5)){
    while(x%%i==0){x=x/i}
  }
  return ( x == 1 )
}

print(is_ugly(15))
print(is_ugly(17))

