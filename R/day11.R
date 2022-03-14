is_anagram= function(word1, word2){
  v1 = sort(strsplit(tolower(word1), split = "")[[1]])
  v2 = sort(strsplit(tolower(word2), split = "")[[1]])
  if (identical(v1, v2)) {
    return ( TRUE )
  }else{
    return ( FALSE )
  }
}


print(is_anagram("The Morse code", "Here come dots"))
print(is_anagram("nie", "tak"))