library(dslabs)
data(murders)

levels(murders$region)

mat <- matrix(1:255 , 51, 5)
mat[12, ]

class(murders$region)

print("hi", quote = FALSE)

y <- c(67879, 789798, 7818)

for(x in y){
  if(x < 37700){
    print("this is in hte basic tax bracker")
  }else if(x < 125140){
    print("this is in the higher tax bracket")
  }else{
    print("this person is in the highest tax bracket")
  }
}