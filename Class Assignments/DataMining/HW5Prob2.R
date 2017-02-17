library(Mclust)
nuoqi <- read.csv("nuoqi.csv")


nuoqi_clustZ <- data.frame(lapply(nuoqi[,1:5], scale, scale=T))

fit = kmeans(nuoqi_clustZ, 5, 100, 100)

# sizes
fit$size
# 144, 236, 164, 143, 307

# cluster means
fit$centers

# rmse
summary.kmeans = function(fit)
{
  p = ncol(fit$centers)
  k = nrow(fit$centers)
  n = sum(fit$size)
  sse = sum(fit$withinss)
  xbar = t(fit$centers)%*%fit$size/n
  ssb = sum(fit$size*(fit$centers - rep(1,k) %*% t(xbar))^2)
  print(data.frame(
    n=c(fit$size, n),
    Pct=(round(c(fit$size, n)/n,2)),
    round(rbind(fit$centers, t(xbar)), 2),
    RMSE = round(sqrt(c(fit$withinss/(p*fit$size-1), sse/(p*(n-k)))), 4)
  ))
  cat("SSE = ", sse, "; SSB = ", ssb, "\n")
  cat("R-Squared = ", ssb/(ssb+sse), "\n")
  cat("Pseudo F = ", (ssb/(k-1))/(sse/(n-k)), "\n\n");
  invisible(list(sse=sse, ssb=ssb, Rsqr=ssb/(ssb+sse), F=(ssb/(k-1))/(sse/(n-k))))
}
summary.kmeans(fit)

##
# so the ipsatization stuff leads me to believe that maybe we dont want to standardize
##

# doing ipsatization
nuoqi$impressI = nuoqi$impress - nuoqi$xbar
nuoqi$selfexpressI = nuoqi$selfexpress - nuoqi$xbar
nuoqi$functionalI = nuoqi$functional - nuoqi$xbar
nuoqi$crossI = nuoqi$cross - nuoqi$xbar
nuoqi$fashethusI = nuoqi$fashethus - nuoqi$xbar


# standardizing the ipstazideds versions
nuoqi_IZ <- data.frame(lapply(nuoqi[,10:14], scale, scale=T))
fit2 = kmeans(nuoqi_IZ, 5, 100, 100)

# sizes
fit2$size
# 311 207 147 161 168

# cluster means
fit2$centers

# rmse
summary.kmeans = function(fit)
{
  p = ncol(fit$centers)
  k = nrow(fit$centers)
  n = sum(fit$size)
  sse = sum(fit$withinss)
  xbar = t(fit$centers)%*%fit$size/n
  ssb = sum(fit$size*(fit$centers - rep(1,k) %*% t(xbar))^2)
  print(data.frame(
    n=c(fit$size, n),
    Pct=(round(c(fit$size, n)/n,2)),
    round(rbind(fit$centers, t(xbar)), 2),
    RMSE = round(sqrt(c(fit$withinss/(p*fit$size-1), sse/(p*(n-k)))), 4)
  ))
  cat("SSE = ", sse, "; SSB = ", ssb, "\n")
  cat("R-Squared = ", ssb/(ssb+sse), "\n")
  cat("Pseudo F = ", (ssb/(k-1))/(sse/(n-k)), "\n\n");
  invisible(list(sse=sse, ssb=ssb, Rsqr=ssb/(ssb+sse), F=(ssb/(k-1))/(sse/(n-k))))
}
summary.kmeans(fit2)

# honestly the rmse went up, so I would actually say that there was no improvement

# ipstazied
wss <- (nrow(nuoqi_IZ)-1)*sum(apply(nuoqi_IZ,2,var))
for (i in 2:6) wss[i] <- sum(kmeans(nuoqi_IZ,
                                     centers=i)$withinss)
plot(1:6, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")

# judging from within group sum of squared, would go with either 5 or 6


# raw 
wss <- (nrow(nuoqi_clustZ)-1)*sum(apply(nuoqi_clustZ,2,var))
for (i in 2:6) wss[i] <- sum(kmeans(nuoqi_clustZ,
                                    centers=i)$withinss)
plot(1:6, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")
# on the raw, definitely probably take 3, and it does much better
# raw number wise as well

fit3 = Mclust(nuoqi_IZ, G=6, modelNames = "VII")
plot(fit3)

fit4 = Mclust(nuoqi_clustZ, G=3)
plot(fit4)

