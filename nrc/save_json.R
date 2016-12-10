library(jsonlite)
json = toJSON(ranked_list,pretty = TRUE,matrix = 'rowmajor')
cat(json,file='data_tables.json')
