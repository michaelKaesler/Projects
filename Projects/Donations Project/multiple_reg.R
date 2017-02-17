# can choose to use either 'donation_data_clean.csv' or 'data_clean_manip.csv' for what i've added

df <- read.csv('data_clean_manip.csv')
dfTest_prob <- read.csv('dfTest_prob.csv')
df$month1 <- as.factor(df$month1)
df$month2 <- as.factor(df$month2)
df$don_state <- as.factor(df$don_state)
dfTest_prob$month1 <- as.factor(dfTest_prob$month1)
dfTest_prob$month2 <- as.factor(dfTest_prob$month2)
dfTest_prob$don_state <- as.factor(dfTest_prob$don_state)
str(df)
summary(df)



# creating a response variable for the model    Prob dont need this either
#df$Response <- ifelse( df$TARGDOL == 0, 0, 1)

# making cndol2 and cndol3 0 if na
df$CNDOL2[is.na(df$CNDOL2)] <- 0
df$CNDOL3[is.na(df$CNDOL3)] <- 0

dfTest_prob$CNDOL2[is.na(dfTest_prob$CNDOL2)] <- 0
dfTest_prob$CNDOL2[is.na(dfTest_prob$CNDOL2)] <- 0

# new var
df$avgCON <- df$CNTRLIF/df$CNTMLIF

# subset where targdol is > 0, for both training and testing data
#dfTrainTarg <- dfTrain[ which(dfTrain$TARGDOL > 0),]
#dfTestTarg <- dfTest [ which(dfTest$TARGDOL > 0),]
dfTarg <- df[ which(df$TARGDOL > 0),]

# making training and testing for the multiple

every_third <- seq(3, 99198, 3)
dfTrain <- df[-every_third,]
dfTest <- df[every_third,]
dfTargTrain <- dfTrain[ which(dfTrain$TARGDOL > 0),]
dfTargTest <- dfTest[ which(dfTest$TARGDOL > 0),]

str(dfTrainTarg)
summary(dfTrainTarg)
summary(dfTarg)

# get base model working (using same one as logistic for now)
#model <- lm(TARGDOL ~ CNDOL1 + CNDOL2 + CNDOL3 + CNCOD1 + CNTRLIF + CONTRFST + 
#               CNTMLIF + CNMON1 + CNMONL + month1, data = dfTarg)   + CNCOD1:CNDOL1 + CNTMLIF:CNDOL1
# THIS IS THE BEST MODEL SO FAR: 10412
#model <- lm(TARGDOL ~ CNDOL1 + CNDOL2 + CNDOL3 + CNCOD1 + CNTRLIF + CONTRFST + CONLARG +
#              CNTMLIF + CNMON1 + CNMONL + CNCOD1:CNDOL1  + CNTMLIF:CNDOL1 +
#              month1 + CNDOL1:month1 + CNDOL2:month1, data = dfTarg)

# however even though its lowering total, we could add them b/c they increase r^2
# taking below out is adding to thing
# + CNTMLIF:CNDOL2 + CNTMLIF:CNDOL3 + CNCOD1:CNDOL1 CNTRLIF + 

model <- lm(TARGDOL ~ CNDOL1 + CNDOL2 + CNDOL3 + CNCOD1  
            + CONTRFST + CONLARG +
              CNTMLIF + CNMON1 + CNMONL + CNMON1:CNDOL1
            + avgCON,data = dfTargTrain)
summary(model)

plot(model, which = 1)

# doing stepwise
library(MASS)
stepper <- stepAIC(model, direction = 'both')
summary(stepper)


dfTest_prob1 <- dfTest_prob[1:33061,]
pred1 <- predict(model)
mean((pred1 - dfTargTrain$TARGDOL)^2)
pred <- predict(model, newdata = dfTest_prob1)
pred
mean((dfTest_prob1$TARGDOL - pred)^2)
str(dfTest_prob)


dfTest_prob_eval <- dfTest_prob1
dfTest_prob_eval$predictions <- pred

expected_donations <- dfTest_prob_eval$probability * dfTest_prob_eval$predictions
dfTest_prob_eval$ETARG <- expected_donations
mean((dfTest_prob_eval$ETARG - pred) ^2)

#ordering by expected_donations (there must be better way of doing this)
dfOrdered <- dfTest_prob_eval[order(-dfTest_prob_eval$ETARG),]

dfTop <- dfOrdered[1:1000,]
sum(dfTop$TARGDOL)

