
# problem 1

geneData <- read.csv('gene.csv')

fit = prcomp(geneData[,1:1000], scale = T)
summary(fit)

# 11 % of variation is accounted for by the first two compontents

plot(fit$x[,1:2], col = geneData$sick + 1)  # why do you have to add +1?
# the first prinicpal component is all you need to seperate sickness


fit$x[,1]



# problem 2
newsData <- read.csv('news2.csv')

fit2 = prcomp(newsData[,2:42], scale = T)
plot(fit2)
fit2$x

# the elbow is after the third principal component
library(psych)
fit3 = principal(newsData, rotate='none', scores=F, nfactor= 3)
fit3$loadings

# it seems to be the first principal component is the heavily fox 
# leaning contingent, possibly republicans. While the second component
# is the CNN and MSNBC contingent, likely the liberals, while the
# third is the seperation of cnn watchers and msnbc watchers, 
# whatever the difference between those is. Dunno about fox not showing
# up tho? does that mean 0?

# 4

R = matrix(c(
  1, .4919, .2636, .4653, -.2277, .0652,
  .4919, 1, .3127, .3506, -.1917, .2045,
  .2635, .3127, 1, .4108, .0647, .2493,
  .4653, .3506, .4108, 1, -.2249, .2293,
  -.2277, -.1917, .0647, -.2249, 1, -.2144,
  .0652, .2045, .2493, .2293, -.2144, 1),
  byrow=T, ncol=6)


# walleye does not, and the cent family is only positively corr, not
# really significant tho

# pca on first 4
fit4 = prcomp(R[1:4,1:4])
summary(fit4)
fit4$rotation

# pca on all 6
fit5 = prcomp(R)
plot(fit5)
summary(fit5)
# 77.8%

fit5$rotation
# its the non centriod or whatever family


# 5
X=matrix(c(1:4, 1,4,9,16), nrow=4)
x1 <- t(X) %*% X
x2 <- X %*% t(X)
x1
x2

eigen(x1)
eigen(x2)

# just zero after the first two. Theyre the same thing. 