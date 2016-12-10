library(plyr)
dat = sheet_list[[1]]
cols = c(3:12)
dat[,cols] = apply(dat[,cols],2,function(x) as.numeric(as.character(x)))
dat$meanHigh = rowMeans(dat[,c(3,5,7,9,11)])
dat$meanLow = rowMeans(dat[,c(4,6,8,10,12)])
dat$meanRank = rowMeans(dat[,c(13,14)])
dat = dat[order(dat$meanRank),]
dat$Rank = seq(1,length(dat$X))
dat = dat[,-1]
dat = dat[,c(length(dat),1:length(dat)-1)]

