# python-website-title-scraper
Uses beautiful soup to scrape website titles from a list of websites in a csv.

The original dataset was the UCI News Popularity Dataset. It contains links of news articles, for which I scraped the titles.

<title> tags are what's being scraped. If you want to change the HTML tag target, change line 10 ["titles"]. It can support multiple tags e.g.["h1", "h2", "h3"].

lists.csv is a UTF-8 CSV, which does not work for the code. You will receive the error "No connection adapters were found for '%s'" % url."

links_2.csv is a normal csv with all the website links.

links_3.csv is the csv where all the scraped titles will be added to so my links_3.csv file obviously already has scraped content.

This was the first step of the clickbait project.
