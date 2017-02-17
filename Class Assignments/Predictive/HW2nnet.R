library(readxl)
library(nnet)
library(caret)
library(ALEPlot)
set.seed(1234)
df <- read_excel('HW2_data.xls')

response <- log10(df$cost)

scaled.df <- scale(df[3:10])
df_scale <- as.data.frame(scaled.df)
df_scale$response <- response

# A)

fitControl <- trainControl(method = 'repeatedcv', number = 10, repeats = 20)

model <- train(response ~., df_scale, method = 'nnet', linout = T, trace = F, trControl = fitControl,
               # parameter grid
               tuneGrid = expand.grid(.size=c(1,3,5,7,10,15,20,30), .decay=c(0,0.1,0.2,0.01,0.001)))
model
# RMSE used to select the optimal model
# that model was of size 3 and decay 0.2


# B) now, fit the final best model and discuss how good it is

out <- nnet(response~., df_scale, linout=T, skip=F, size=3, decay = 0.2, maxit=1000,
            trace = F)

yhat <- as.numeric(predict(out))
y <- df_scale$response
e<- y-yhat
c(sd(y),sd(e))
1-var(e)/var(y) # equals .715

# so r^2 is about 71.5% for nn model, which is better than the linear regression.
# but this could be bc of over fitting, need to asses the CV SSe for the model

Kind <- function(n,K) {  #n is sample size; K is number of parts; returns K-length list of indices for each part
  m<-floor(n/K)  #approximate size of each part
  r<-n-m*K  
  I<-sample(n,n)  #random reordering of the indices
  Ind<-list()  #will be list of indices for all K parts
  length(Ind)<-K
  for (k in 1:K) {
    if (k <= r) kpart <- ((m+1)*(k-1)+1):((m+1)*k)  
    else kpart<-((m+1)*r+m*(k-r-1)+1):((m+1)*r+m*(k-r))
    Ind[[k]] <- I[kpart]  #indices for kth part of data
  }
  Ind
}

##Now use the same CV partition to compare Neural Net and linear reg models###
Ind<-Kind(n=nrow(df_scale),10)
K<-length(Ind)
y1<-df_scale$response
yhat1<-y1
for (k in 1:K) {
  out<-nnet(response~.,df_scale[-Ind[[k]],],linout=T,skip=T,size=3,decay=0.02,maxit=1000,trace=F)
  yhat[Ind[[k]]]<-as.numeric(predict(out,df_scale[Ind[[k]],]))
}
e1 = sum((y-yhat)^2)
e1

###### THE ABOVE IS CODE TO DO CV to get cv sse after training dat model doe



# C)
# which variables appear to have the most influence on the cost, and what are their effects
yhat <- function(X.model, newdata) as.numeric(predict(X.model, newdata))
par(mfrow=c(3,3))
for (j in 1:8) { ALEPlot(df_scale[,1:8], model, pred.fun = yhat, J=j, K=50, NA.plot=TRUE)
  rug(df_scale[,j])}

# looking at the main effects plot, it seems that based on the scales, that x_3 (intvn) has
# the greatest effect, as it ranges from -0.5 all the way to 1.5. The next biggest is
# x_7 (comorb) it ranges from -0.2 all the way to 1.

# for some 2nd order interaction
par(mfrow=c(2,2))
ALEPlot(df_scale[,1:8], model, pred.fun = yhat, J=c(3,7), K=50, NA.plot=TRUE)
ALEPlot(df_scale[,1:8], model, pred.fun = yhat, J=c(1,7), K=50, NA.plot=TRUE)

# also tried looking at some interactions, but not as big as the main effects plots

# D) look at residual plot to assess any remaining nonlinearity
par(mfrow=c(1,1))
e <- df_scale[[9]] - pred
plot(pred, e)
# honestly, that resid plot looks pretty good to me, not much unexplained nonlinearity