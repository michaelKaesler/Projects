library(psych)
alldiet <- read.csv("alldiet.csv")


showcols <- 4:204
alldiet[,showcols] <- log(alldiet[,showcols] + 1) # logging due to heavy right tails
summary(alldiet)
showcols1 <- c(4:153, 155:204)

names(alldiet) <- paste(1:204,names(alldiet))

all.fit <- principal(alldiet[,showcols1], rotate = 'none')
all.fit$values # 32 eigenvalues greater than 1
plot(all.fit$values)
abline(h=1)

# judging from that scree plot, I'm going to go with 10 factors. Which is nice, since it
# is the same number of factors as just the news alone

all.fit1 <- principal(alldiet[,showcols1], nfactors = 10, rotate = 'varimax')
all.fit1$loadings
# note, do to mass amounts of vars, not taking anything below .5 (or .495) (or .47)
# also note, 10 factors could be leaving some solid groups out, maybe like 13 would be better
f1 <- c(9,18,25,26,42,43,58,61,62,70,86,90,92,93,94,134,156,160,165,184,198,203)
f2 <- c(36,48,54,75,84,99,107,108,109,123,133,145,148,175,178,192)
f3 <- c(155,171,173,179,180,185,186,189,193,194)
f4 <- c(8,50,52,55,59,63,68,73,76,91,104,118,127,177)
f5 <- c(20,21,22,23,24,31,32,67,159,166,168)
f6 <- c(56,74,79,81,87,96,102,117,131,135)
f7 <- c(35,44,72,80,82,83,88,106,176)
f8 <- c(5,27,28,33,34,51,66,85,95,120,137,161)
f9 <- c(7,10,11,12,13,15,14,16,153)
f10 <- c(30,37,139,140,141,142,143,144,146,147,151,149)

drop <- c(195,116,122,182,170,29)

psych::alpha(alldiet[,f1])
psych::alpha(alldiet[,f2])
psych::alpha(alldiet[,f3])
psych::alpha(alldiet[,f4])
psych::alpha(alldiet[,f5]) # drop 31 CNNcnn and 32 CNNAndersonCooper
psych::alpha(alldiet[,f6]) # drop 131 HotBench
psych::alpha(alldiet[,f7]) # drop 106 FleaMarketFlip
psych::alpha(alldiet[,f8])
psych::alpha(alldiet[,f9]) # drop 10 Enews
psych::alpha(alldiet[,f10])

drop <- c(drop, 31, 131, 106, 10)

f5 <- c(20,21,22,23,24,67,159,166,168)
f6 <- c(56,74,79,81,87,96,102,117,135)
f7 <- c(35,44,72,80,82,83,88,176)
f9 <- c(7,11,12,13,15,14,16,153)

keep <- c(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)

names(alldiet)[f1] # Gameshows, talkshows, daytime tv, abc202 abcworldnews
names(alldiet)[f2] # 'dont have a good word for it, but def same type of stuff' outdoors types too
names(alldiet)[f3] # G shows, non sports
names(alldiet)[f4] # sitcoms
names(alldiet)[f5] # fox news/ political 
names(alldiet)[f6] # gun enthusiasts
names(alldiet)[f7] # House people
names(alldiet)[f8] # cbs shows
names(alldiet)[f9] # children
names(alldiet)[f10] # sports and 60 minutes



