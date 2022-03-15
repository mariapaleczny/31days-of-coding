add_dots = function(word){
  print(paste(strsplit(word, split = "")[[1]], collapse = "."))
}

add_dots("test")