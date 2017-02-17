# Question 1
X = matrix(c(1,3,5,0,1, 2,4,4,2,3, 3,5,3,4,5), nrow=5)

tXX <- t(X) %*% X;tXX
XtX <- X %*% t(X);XtX
eigen(tXX)
eigen(XtX)

eigen(tXX)$vectors %*% diag(eigen(tXX)$values) %*% t(eigen(tXX)$vectors)
tXX

svd(X)

svd_X <- svd(X)$u %*% diag(svd(X)$d) %*% t(svd(X)$v)

singular.values <- svd(X)$d
singular.values[2:3] <- 0

Xhat <- svd(X)$u %*% diag(singular.values) %*% t(svd(X)$v)
sum(Xhat^2) # same as sum(singular.values^2)

sum((svd_X-Xhat)^2) # similar to the square of the value that got zeroed

sum(singular.values^2)/sum(svd(X)$d^2)

# Question 2
theater <- read.csv("theater.csv")
theater[,c(3,5,7,10)] <- NULL
library(psych)
alpha(theater[,1:10], check.keys=T)
alpha(theater[,c(1,3:10)], check.keys=T) # drop dislike
alpha(theater[,c(1,3:7,9:10)], check.keys=T) # drop dislike and noteduc

pca <- principal(theater[,1:10])
pca$values # only one eigenvalue greater than 1
pca$loadings # smallest loadings are dislike and noteduc

pca_purify <- principal(theater[,c(1,3:7,9:10)])
pca_purify$values
pca_purify$loadings

theater$irritate2 <- 8-theater$irritate
theater$bad2 <- 8-theater$bad
theater$cannotappreciate2 <- 8-theater$cannotappreciate
theater$attitude <- apply(theater[,c(1,3,6,7,9,17:19)],1,mean)

theater$dinnerplay <- apply(theater[,11:12],1,sum)
theater$dinnerplay <- log(theater$dinnerplay+1)
cor(theater$attitude, theater$dinnerplay, use="pairwise.complete.obs")

music <- read.csv("music.csv")
questions <- c("V28","V29","V30","V31","V32","V33","V34","V43","V46","V47","V50","V52")
alpha(music[,questions])
fit <- principal(music[,questions])
fit$values # only one eigenvalue is greater than 1