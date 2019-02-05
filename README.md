# Description
In response to challenge given by Clearcode I have created two files with solutions of each exercise
* CSV/csv_reader.py
* WEB/WebCrawler.py

# CSV Report Processing
In order to proper operation location of .csv file must be the same as csv_reader.py

### Variables/Lists
* filename - *name of .csv file (input)*
* Data - *list of stored data from csv file*
* DateFormat - *changed format of datetime*
* Subs - *list of subdivisions taken from pycountry library*
* ShortSubs - *list of three letter country codes taken from pycountry library*
* CTR - *number of clicks changed from string to integer (multiplied by 10)*

### Exceptions
* FileNotFoundError .csv file does not exit or it is located in another directory
* ValueError incompatible date format month/day/year
* '%' symbol exist verification in CTR column

# Web Crawler 
You can run server with RunServer.py
