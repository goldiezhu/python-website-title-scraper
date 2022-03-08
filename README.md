# python-website-title-scraper
Uses beautiful soup to scrape website titles from a list of websites links in a csv.

The original dataset was the UCI News Popularity Dataset. It contains links to news articles, of which I scraped the titles.
<br>
<title> tags are what's being scraped. If you want to change the HTML tag target, change line 10 ["titles"]. It can support multiple tags e.g. ["h1", "h2", "h3"].
<br><br>
lists.csv is a UTF-8 CSV, which does not work for the code. You will receive the error "No connection adapters were found for '%s'" % url." Just open the csv and save as a new normal csv.
<br><br>
links_2.csv is a normal csv with all the website links.
<br><br>
links_3.csv is the csv where all the scraped titles will be added to so my links_3.csv file obviously already has scraped content.
<br><br>
This was the first step of my group data analysis project (name: clickbait popularity project).
