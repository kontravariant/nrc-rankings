# nrc-rankings
###National Research Council Graduate Rankings web page

I was curious to find any other graduate program ranking besides US News. I came across data from the National Resrource Council, hosted by www.chronicle.com. But this data was poorly displayed and the options (fields of study) were jumbled up in a plain text list.

I set out to scrape, munge and redisplay this data in a more attractive manner.
####I acomplished the following:
* Download all 60-odd pages of tables, parse that html and pack all the data into lists with proper titles (get.py, parse.py)
* Write all tables into excel sheets (munge.py)
* Load all the sheets into R data frames and create means of the ranking categories to produce a deterministic overall ranking for each field of study (the R scripts). The final data was output as a JSON object (array of arrays).
* Create a basic HTML page with [DataTables](https://datatables.net/) jQuery plug-in to display data
* Add javascript to dynamically draw the DataTable based on the dropdown selection, which is dynamically filled from the top-level array names in the JSON object.

####To-do List:
- Properly format the dropdown selections with the full names as listed by the Chronicle.
  - This must be done upstream of not only the website, but the R script, since the excel sheet names are where these are truncated.
  - The trick will be passing this in a way that is easily obtainable by R (perhaps the top-left cell of every excel?).
    - Or these names can be approximated by parsing out the text in parentheses for the first Institution in each list.
- Perhaps look at comparisons of these rankings with US News or alternate sources/data. Or combine the rankings?
  - Look at endowment, population, location, faculty salaries, placements, etc.
