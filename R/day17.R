calculate_factorial = function(n){
  if (n%%1!=0 || n<0){
    stop("Not a non-negative integer.")
  }else if (n==0 || n==1){
    return ( 1 )
  }else{
    ans=1
    for(i in 2:n){
      ans = ans * i
    }
    return ( ans )
  }
}


> calculate_factorial(5)==120
[1] TRUE

