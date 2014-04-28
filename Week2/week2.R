histogram_calc <- function(filename,bin=10){
  data <- read.table(filename)
  col <- data$V1
  mi <- min(col)
  ma <- max(col)
  histo <- hist(col, breaks=seq(mi,ma,(ma-mi)/bin))
  return(histo$counts)  
}