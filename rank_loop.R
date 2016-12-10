library(plyr)
ranked_list = list()
load('sheets.RData')
load('names.RData')
for(i in 1:62)  {
  dat = sheet_list[[i]]
  cols = c(3:12)
  dat[,cols] = apply(dat[,cols],2,function(x) as.numeric(as.character(x)))
  dat$meanHigh = rowMeans(dat[,c(3,5,7,9,11)])
  dat$meanLow = rowMeans(dat[,c(4,6,8,10,12)])
  dat$meanRank = rowMeans(dat[,c(13,14)])
  dat = dat[order(dat$meanRank),]
  dat$Rank = seq(1,length(dat$X))
  dat = dat[,-1]
  dat = dat[,c(length(dat),1:length(dat)-1)]
  headers = c(
    'Rank',
    'Institution (Program)',
    'S-Rank High',
    'S-Rank Low',
    'Research High',
    'Research Low',
    'Students High',
    'Students Low',
    'Diversity High',
    'Diversity Low',
    'R-Rank High',
    'R-Rank Low',
    'Mean-High',
    'Mean-Low',
    'Mean-Rank'
  )
  colnames(dat) = headers
  name_field = dat[[2]]
  fl = list(NA)
  for(word in name_field) {
    field = gsub(".*\\((.*)\\).*", "\\1", paste(word))
    fl = append(fl,field[1])
  }
  fl = unlist(fl)
  field = names(which(table(fl) == max(table(fl))))
  ranked_list[[paste(field)]] = dat
}
