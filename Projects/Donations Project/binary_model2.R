# can choose to use either 'donation_data_clean.csv' or 'data_clean_manip.csv' for what i've added

df <- read.csv('data_clean_manip.csv')
df$month2 <- as.factor(df$month2)
df$month1 <- as.factor(df$month1)
df$don_state <- as.factor(df$don_state)

str(df)
summary(df)



# creating a response variable for the model
df$Response <- ifelse( df$TARGDOL == 0, 0, 1)
df$Response <- as.factor(df$Response)

# making cndol2 and cndol3 0 if na
df$CNDOL2[is.na(df$CNDOL2)] <- 0
df$CNDOL3[is.na(df$CNDOL3)] <- 0


# splitting into test ratio of 2:1 with every 3rd obs in test set
every_third <- seq(3, 99198, 3)
dfTrain <- df[-every_third,]
dfTest <- df[every_third,]

str(dfTrain)

# create model (with taking out conlarg and conmonf first, due to corr)
#this model is the best I have right now, AUC 0.705
#model <- glm(Response ~ CNDOL1 + CNDOL2 + CNDOL3 + CNCOD1 + CNTRLIF + CONTRFST +  
#              CNTMLIF + CNMON1 + CNMONL + CNMONF + CNCOD1:CNDOL1 + CNTMLIF:CNDOL1,
#             data = dfTrain, family = binomial)

# new best model AUC:.7117
#model <- glm(Response ~ CNDOL1 + CNDOL2 + CNCOD1 + CNTRLIF + CONTRFST +  
#               CNTMLIF + CNMON1 + CNMONL + CNMONF + don_state,
#             data = dfTrain, family = binomial)

model <- glm(Response ~ CNDOL1 + CNDOL2 + CNDOL3 + SLCOD1 + CNCOD1 + CNTRLIF + CONTRFST +  
               CNTMLIF + CNMON1 + CNMONL + CNMONF + don_state + avgCON,
             data = dfTrain, family = binomial)
summary(model)

pred <- predict(model, type = 'response', newdata = dfTest)

#confusion matrix
table(dfTest$Response, pred > 0.5)


#ROCR Curve   ##### in this version switching to pROC
library(pROC)
plot.roc(dfTest$Response, pred)

# add the predicted probability it will be a donation to the df, and export to csv
dfTest$probability <- pred

write.csv(dfTest, 'dfTest_prob.csv')
