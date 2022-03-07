#returns integer(0) if there is no uppercase
capital_indexes = function(s){
  which(toupper(strsplit(s, split = "")[[1]])==strsplit(s, split = "")[[1]])
}

capital_indexes("BLAblabLa")