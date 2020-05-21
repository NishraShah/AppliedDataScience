data("iris")
str(iris)
# str stands for structure. Shows the structure of dataset. 
# We want to classify new flowers based on this given data: Classification problem

table(iris$Species)
# So, we see we have 50 samples for each of the species
# Species is our target

head(iris)
# First, We have to mix up the dataset.. Mix rows!

set.seed(9850)
gp <- runif(nrow(iris))

iris <- iris[order(gp),]
str(iris)
# Normalize the features on same scale

summary(iris) #we see different range

normalize <- function(x){ return( (x-min(x))/(max(x)-min(x)))}

iris_n <- as.data.frame(lapply(iris[,c(1,2,3,4)], normalize))
summary(iris_n)

iris_train <- iris_n[1:129, ]
iris_test <- iris_n[130:150, ]

#Training target feature.. isolating the Species coloumn from load iris variable

iris_train_target <- iris[1:129,5]

iris_test_target <- iris[130:150,5]

require(class)

m1 <- knn(train=iris_train,test=iris_test,cl=iris_train_target,k=13)
m1

table(iris_test_target,m1)
#we can use knn when we have the target as categorical or nominal variable








 
