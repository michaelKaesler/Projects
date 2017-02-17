tradeshow <- read.csv("tradeshow.csv")

ts_clust <- tradeshow[,1:3]

Zts_clust <- data.frame(lapply(ts_clust, scale, scale=T))

# kmeans on the three variables
fit = kmeans(Zts_clust, 3, 100, 100)
names(fit)
library(mclust)

# sizes
fit$size
# 155, 117, 173

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


fit2 = Mclust(Zts_clust, G=3, modelNames = "VII")
names(fit2)
fit2$parameters$pro
fit2$parameters$mean


# actually, by looking at just the means, they kind of do tell the same story,
# its just that the cluster numbers are a little switched
# in kmeans, cluster one is cluster three in gauss
# cluster 2 is cluster one in gauss
# cluster 3 is cluster 2 in gauss

summary(fit2)
# gauss sizes are 1:63 2:177 3:205
# kmeans sizes are 1:155 2:117 3:173

# so the story is not the same when it comes to cluster size


fit2$parameter$variance$sigmasq
# gauss sd are 1:.862 2:.590 3:.683
summary.kmeans(fit)
# kmeans sd are 1:.728 2:.795 3:.709

# D? I have no clue what he means by how many variance parameters estimated in total


fit3 = Mclust(Zts_clust, G=3)
fit3$parameters$mean
fit2$parameters$mean

# compared to the VII, without it just has a little higher 'peaks' in the means,
# but overall tell a similar story

plot(fit3) # choose option 2
summary(fit3)
# the summary command says it picked the EEE model
# the class conditional distributions are "ellipsoidal"

# again, variance params?


# I prefer the VII, it seems more 'subdued' judging by the means