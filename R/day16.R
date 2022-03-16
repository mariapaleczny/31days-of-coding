source("day3.R")
is_palindrome = function(word){
  return ( reverse_string(word) == word )
}

print(is_palindrome("kajak"))
print(is_palindrome("kaja"))