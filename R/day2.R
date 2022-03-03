switch_case = function(s){
  out = ""
  for (i in strsplit(s, split = "")[[1]]){
    if (toupper(i) == i){out=paste(out, tolower(i), sep="")}
    else if (tolower(i) == i){out=paste(out, toupper(i), sep="")}
    else out=paste(out, toupper(i), sep="")
  }
  print(out)
}

switch_case("hELLO! hOW ARE you?")