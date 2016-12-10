for(i in 1:62) {
  sheet_name = print(paste('./csv/',names[i],'.csv',sep = ""))
  write.csv(sheet_list[i],file = sheet_name)
}
