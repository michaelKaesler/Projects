library(caret)
library(rpart)
library(readxl)
library(ALEPlot)
set.seed(1234)

df <- read_excel('HW2_data.xls')

df$response <- log10(df$cost)

df_new <- df[3:11]

# A)
# choose cp as small as you can, corresponds to largest tree to grow
# this is also using 10fold cross val
control <- rpart.control(minbucket = 5, cp = 0.00001, xval = 10, maxsurrogate = 0,
                         usesurrogate = 0)


out <- rpart(response~., data = df_new, method = 'anova', control = control)

plotcp(out)
# above is plot of CV deviance vs tree size//complexity parameter
# since cv error goes up at end, it was grown large enough

# to get the best cp value, 
bestcp <- out$cptable[which.min(out$cptable[,"xerror"]),"CP"]
bestcp
# to see how many nodes that cp is, do the below, and see how many nodes
# your best cp equals (here it is 18)
printcp(out)

# B)
# now, to fit the final best model, need to prune, determine how good it is
out1 <- prune(out, cp=0.00314)
plot(out1);text(out1)

y <- df_new$response
yhat <- as.numeric(predict(out1))
e <- y - yhat
c(sd(y), sd(e))
1 - var(e)/var(y) #note, this gives us the training r^2
# could be due to overfitting, need to assess the cv sse
printcp(out1)


# so the 10fold cv 1-r2 is the last entry's xerror, so 0.4. So, the
# r2 = 1- 0.4 = .6
# now alledgedly, wed have to do this 20 replicates manually


# C)
# which variables appear to have the most influence on the cost
out1$variable.importance
# this can also be gauged by inspection of the plot of the tree,
# where more important variables are higher up on the tree

# D)
# construct residual plot to asses any remaining linearity
plot(yhat, e)
# note, he also does the residuals vs the most important predictor, interesting

