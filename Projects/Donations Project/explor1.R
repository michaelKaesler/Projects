df <- read.csv('donation_data_clean.csv')
dfTest_prob <- read.csv('dfTest_prob.csv')
df$month1 <- as.factor(df$month1)
dfTest_prob$month1 <- as.factor(dfTest_prob$month1)
df$Response <- ifelse( df$TARGDOL == 0, 0, 1)
df$Response <- as.factor(df$Response)

str(df)
summary(df)


# making cndol2 and cndol3 0 if na
df$CNDOL2[is.na(df$CNDOL2)] <- 0
df$CNDOL3[is.na(df$CNDOL3)] <- 0

dfTarg <- df[ which(df$TARGDOL > 0),]


hist(df$CNDOL1, breaks = 1000, xlim = c(0,100))
summary(df$CNDOL1)


str(df)

# tables for logistic
tab2 <- table(df$CNCOD1, df$Response)
prop.table(tab2, 1)
table(df$SLCOD1, df$Response)
table(df$STATCODE, df$Response)
summary(df$TARGDOL)
quantile(dfTarg$TARGDOL, probs = seq(0, 1, 0.1))

dfTarg <- df[ which(df$TARGDOL > 0),]
BM <- df[ which(df$TARGDOL > 20),]
quantile(BM$TARGDOL, probs = seq(0, 1, 0.05))

dfOrdered <- df[order(-df$TARGDOL),]
dfTop <- dfOrdered[1:1000,]
sum(dfTop$TARGDOL)
# total we can get is 34,000 (obvi wont get close bc multiplying by probs)

table(BM$STATCODE, BM$Response)

df$Response <- ifelse( df$TARGDOL == 0, 0, 1)

df$BM <- ifelse(df$TARGDOL == 0, 0, ifelse(df$TARGDOL < 20, 1, 2))

tab1 <- table(df$STATCODE, df$Response)
prop.table(tab1, 1)
