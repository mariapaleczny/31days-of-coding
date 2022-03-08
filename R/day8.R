womensday = function(){
  name=readline(prompt="Enter name: ")
  len = nchar(name)
  if (substr(name, len, len) == 'a'){ 
    print(paste("Happy Women's Day, ",name,"!", sep=""))
  } else {
    print("Ok.")
  }
}