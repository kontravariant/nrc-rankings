require(gdata)
xls_file = 'nrc_dat.xlsx'
names = sheetNames(xls_file)
sheet_list = list()
for(x in 1:1) {
  sheet_list[[x]] = read.xls(xls_file, sheet=x)
}

