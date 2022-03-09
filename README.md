# python-website-title-scraper
This code uses BeautifulSoup to scrape website titles from a list of websites links in a csv. 
<br>!This code does not replace special characters and may throw a data error! �Specials may also appear in the scraped dataset.

The original dataset was the UCI News Popularity Dataset. It contains links to news articles, of which I scraped the titles.
<br>
<title> tags are what's being scraped. If you want to change the HTML tag target, change line 10 ["titles"]. It can support multiple tags e.g. ["h1", "h2", "h3"].
<br><br>
lists.csv is a UTF-8 CSV, which does not work for the code. You will receive the error "No connection adapters were found for '%s'" % url." Just open the csv and save as a new normal csv. This is the complete list of links though. links_2.csv only contains part of the original dataset's links. The original (normal csv) list will throw special character errors with my code, so I ran in chunks [1].
<br><br>
links_2.csv is a normal csv with relevant website links. It should contain the list of links to be used by the code.
<br><br>
links_3.csv is the csv where all the scraped titles will be added to so my links_3.csv file obviously already has scraped content. Data is added to the csv by appending so it won't overwrite the content that's already in the csv. The output is written into one row where each title is a new column. If you want it to be one column, you can transpose it in excel (For code, maybe try pandas transpose()?).
<br><br>
final_titles is the list of news articles titles from the UCI News Popularity Dataset.
<br><br>
This was the first step of my group data analysis project (name: clickbait popularity project).
  
 
  
  
<br><br><br>
[1] If you run the original dataset, it will throw an error at line 9080: 'UnicodeEncodeError: 'gbk' codec can't encode character '\xe4' in position 28: illegal multibyte sequence.' This is due to a "ä" character in the title. I just manually copied the title into the final excel. It took me 5140 seconds to run 9080 lines of the News Popularity Dataset before it threw an error. I didn't want to run it again so I just copied all the outputted scraped titles, text replaced the HTML tags[2], and pasted it into an excel.
<br>EDIT: errors: 9080 "ä", 11373 "ö", 11409 "ä", 11588 "ö", 17036 '\xa0', 18122 '\xa0', 19937 '\xa0', 23152 '\xf1'
<br>EDIT: I didn't realize there are so few special characters not accepted by this code. Might be an easy fix by writing code to replace the '\xe4','\xa0', etc. (try .decode('iso-8859-1') or .encode('utf-8')?)
  
[2] The final csv will have HTML tags around the titles. I tried .replace and .get_text(), but they were giving errors; the errors were most likely due to the title being saved as a class 'bs4.element.ResultSet.' I didn't need a complete polished result in one go so I took a shortcut. Fastest way is to just run it through a text replacing website e.g. http://www.unit-conversion.info/texttools/replace-text/. Run it twice as you have to remove the beginning and closing tag separately.

[3] For large datasets like I had: if the code throws an error, just copy all the outputs, text replace it, and paste it in an excel. Just manually retrive the title that threw an error. There's no need to waste time running it again.
