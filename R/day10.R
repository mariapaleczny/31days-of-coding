random_name = function(){
  vowels = c("a", "e", "i", "o", "u", "y")
  endings = c("szard","tr","sław", "drzej", "mierz", "liusz", "teusz", "weł")
  print(paste(sample(LETTERS, 1), sample(vowels, 1), sample(endings, 1), sep=""))
}

random_name()