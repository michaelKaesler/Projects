library(caret)
library(rpart)
library(readxl)
library(ALEPlot)
set.seed(1234)

df <- read_excel('HW2_data.xls', sheet = 2)
summary(df)
str(df)

df$type <- as.factor(df$type)
str(df)


# A) use 10fold cros val to find best nnet model for classifying class type

scaled.df <- scale(df[2:10])
df_scale <- as.data.frame(scaled.df)
df_scale$type <- df$type

fitControl <- trainControl(method = 'repeatedcv', number = 10)

model <- train(type ~., df_scale, method = 'nnet', linout = F, trace = F, trControl = fitControl,
               # parameter grid
               tuneGrid = expand.grid(.size=c(1,3,5,7,10,15,20,30), .decay=c(0,0.1,0.2,0.01,0.05)))
model
# final values used were model size = 20, decay = 0.05, with accuracy .735
# using these parameters, the final fitted model is
out <- nnet(type~., df_scale, linout=F,skip=F,size=20,decay=0.5,maxit=1000,trace=F)
y<-df_scale$type
phat <-predict(out,df_scale)
phat
ind<-apply(phat,1,which.max)
ind
yhat<-as.factor(levels(y)[ind])
MISCLASS=sum(y != yhat)/length(y)
sum(y != yhat)/length(y)

# essentially do the above to calculate the misclass rate over the whole dataset
# doesn't work because the # of levels are off, since the model doesn't predict
# any of one of the categories, there are other ways

# now if we do it a different way
yhat1 <- predict(out,type='class')
misclass1 <- sum(y != yhat1)/length(y)
misclass1

# that works


# B) use 10fold cros val to find best tree model for classifiying class type

control <- rpart.control(minbucket = 5, cp = 0.00001, xval = 10, maxsurrogate = 0,
                         usesurrogate = 0)

# note, rpart is only capable of tuning the cp paramater
rpartGrid <- expand.grid(cp = c(0.0001, 0.001, 0.01))

outTr <- rpart(type ~., df[2:11], control = control)
plotcp(outTr)
# that plot is a plot of cv relative misclass rate vs tree size/complexity param
# CV error goes up at the end, hence the tree was grown large enough

# now get cp with minimal deviance
bestcp <- outTr$cptable[which.min(outTr$cptable[,"xerror"]),"CP"]
bestcp
out1 <- prune(outTr, cp=0.0145)
plot(out1); text(out1, digits=3)
printcp(out1)

yTr <- df$type
pred <- predict(out1, type = 'class')
misclassTr <- sum(yTr != pred)/length(yTr)
misclassTr # note, this equaled 0.229

# so, the training misclass rate is 22.9%
# note, the cv error reported by printcp() function is the relative misclass rate(to
# the root node)
# so the cv misclass rate is root node error * the last xerror
# so 0.6 * 0.5 (why mine doesn't do decimals is retarted)
# that is just one replicate of CV, you can do it manually 20 times and average them
# to get the 20 replicate one



# C) fit a multinomial model and discuss the results 
# using the standardized data used in part A

# note, always use scaled data in the multinomial/binomial/linear regressions!!!

outMu <- multinom(type~., df_scale, trace = F)
summary(outMu)

predMu <- predict(outMu, type = 'class')
sum(y != predMu)/length(y)

#D)
# The neural net performed the best, the decision tree the second best, and the multinomial
# regression the worst. The multinomial performing the worst is unsurprising, and the nnet being better
# than the tree is not that suprising either. However that it is only that much better is. Also, given the 
# use case of predicting glass type, in this siutation (forensics), only the pure prediction matters. However
# if it were another use case, I would reccomend the tree since it is just a slight drop in accuracy
# but provides much more interpretability. 