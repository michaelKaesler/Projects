library(boot)
library(readxl)

hw_data <- read_excel('HW1_data.xls')

Ytransform <- 1/(hw_data$y)
Xtransform <- 1/(hw_data$x)


df <- data.frame(Ytransform,Xtransform)


fit_inital <- lm(Ytransform ~ Xtransform, df )
summary(fit_inital)

gam0 <- 1/(fit_inital$coefficients[1])
gam1 <- fit_inital$coefficients[2]/fit_inital$coefficients[1]

hw_fit <- function(Z,i,theta0){
  Zboot <- Z[i,]
  y<-Zboot[[1]];x1<-Zboot[[2]]
  fn <- function(p){yhat<-(p[1]*x1)/(p[2]+x1); sum((y-yhat)^2)}
  out<-nlm(fn,p=theta0)
  theta<-out$estimate
}

hw_boot <- boot(hw_data,hw_fit,R=20000, theta0=c(gam0,gam1))

# a) plot bootstrapped histograms of gam0 and gam1, and 
# calcualte the corresponding standard erros

CovTheta <- cov(hw_boot$t)
SE<- sqrt(diag(CovTheta))
hw_boot
CovTheta
SE

# plotting for fist param
plot(hw_boot, index=1)
# plotting for second param
plot(hw_boot, index = 2)


# b) calcualte 'crude' twosided 95 CI's

# for first param
boot.ci(hw_boot,c=.95,index = 1, type = 'norm')
# for second param
boot.ci(hw_boot,c=.95,index = 2, type = 'norm')

# c) calcualte reflected twosided 95 CI's

# for first param
boot.ci(hw_boot,c=.95,index = 1, type = 'basic')

# for second param
boot.ci(hw_boot,c=.95,index = 2, type = 'basic')

# d)
# the ones for reflected are slightly higher than normal's
# for the first parameter, and a little wider for the second,
# but they are pretty close


