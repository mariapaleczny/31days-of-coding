gerund_infinitive = function(verb){
  len = nchar(verb)
  if (substr(verb, len-2, len) != 'ing'){ 
    stop('Not a gerund.')
  } else {
    print(paste("to",substr(verb, 1, len-3),sep=" "))
  }
}

gerund_infinitive("going")