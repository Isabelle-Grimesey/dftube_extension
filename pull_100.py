# Pulls info for Amazon's top 100 "Best Sellers in Audible Books & Originals" into parallel lists.
# Stores results by BSR (bestseller rank) in csv.
# csv file name: books.csv
# csv headers: bsr, title, genre, url to product listing (consider inserting info into generic url format instead of storing all of them)
# since I have a list of top 10k, ordered, i do not need crawling nor bsr
# i might need bsr if i want it as a parameter of popularity - for top 10k, it doesn't matter since they are all profitable

# to do top 10,000 titles, this would take about 100 minutes (assuming linear scaling)
# this would especially be a problem when it comes to updating - it will still take a long time, even if it is not writing everything.
# a database might be faster

# references: https://docs.python-guide.org/scenarios/scrape/
#             https://lxml.de/lxmlhtml.html#html-element-methods


from lxml import html
import requests


f = open("books.csv", "w")
# 50 displayed per page; for top 10k you will need to visit top 200 sites
url_format = 'https://www.amazon.com/Best-Sellers-Audible-Books-Originals/zgbs/audible/ref=zg_bs_pg_2?_encoding=UTF8&pg='
for i in range(0, 2):
    # open url of the (i*50 + 1)th to the (i+1)*50th bestsellers, get html and parse into tree
    page = requests.get('https://www.amazon.com/Best-Sellers-Audible-Books-Originals/zgbs/audible/ref=zg_bs_pg_2?_encoding=UTF8&pg='+str(i+1))
    while page.status_code != 200:
        page = requests.get('https://www.amazon.com/Best-Sellers-Audible-Books-Originals/zgbs/audible/ref=zg_bs_pg_2?_encoding=UTF8&pg='+str(i+1))
    tree = html.fromstring(page.content)

    # find and write titles from potential title list
    contains_titles = tree.xpath('//div[@class]')
    #j = 0;
    for title in contains_titles:
        if "p13n-sc-truncate" in title.classes or "p13n-sc-line-clamp-1" in title.classes:
            #f.write(str((i*50 + 1)+j) + "," + title.text_content().strip() + "\n")
            f.write(title.text_content().strip() + "\n")
            #j=j+1

f.close()

# page = requests.get('https://www.amazon.com/Best-Sellers-Audible-Audiobooks/zgbs/audible')
# while page.status_code != 200:
#     page = requests.get('https://www.amazon.com/Best-Sellers-Audible-Audiobooks/zgbs/audible')
#     # currently I am getting 503s over half of the time, and the rest of the time i get 200s
# # `wget`` is about as reliable at producing 200s, `links`` is more reliable but it doesn't look like you can get html from it; it makes a binary file.
# tree = html.fromstring(page.content)

# SCRAPE BSR (BESTSELLERS RANK)
#alternative - keep indexing of other scraped values, use these as bsr since it will go through in order
#bsrs = tree.xpath('//span[@class="zg-badge-text"]/text()')
# convert bsr from string to int - might help with storage / runtime
#bsrs = [int(i[1:]) for i in bsrs]

# DEBUGGING
# from inspect element, i obtained name "zg-bdg-text", which the parser did not pickup. However, it did find "zg-badge-text".
# # what class names does parser pick up on for span objects?
# bsrs = tree.xpath('//span[@class]')
# classes = []
# # for each element of bsrs, use .classes on it, and look through the returned set to find classnames, insert class name to list if it is not already in list 
# for bsr in bsrs:
#     for classy in bsr.classes:
#         if classy not in classes:
#             classes.append(classy)
# print(classes)

# OTHER DEBUGGING
# try viewing sourcecode to see if there are any restrictions on attribute values
# try using regex in xpath
# try using csspath instead of xpath - which one is more robust? Which one is most likely to change if the website is updated?
# try using beautiful soup or scrapy

# TEMPORARY WORKAROUND - I will find all span elements and filter out the bsrs based on formatting
# bsrs = tree.xpath('//span[@class]')
# regex = re.compile(r'^#[0-9]+$')
# bsrs = [int(i[1:]) for i in bsrs if regex.search(i)]
# print(bsrs)

# SCRAPE TITLES
# inspect element says the classtype of titles is "_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y"
# debugging shows 2 similar classes: "p13n-sc-truncate" and "p13n-sc-line-clamp-1", but neither of them return anything
# these classes show up in the sets of classes for each element, so why can't we find any elements of this class?
# does xpath class= refer only to one class from the set of classes that describes an element?

# doesn't work
# titles = tree.xpath('//div[@class="p13n-sc-truncate"]')
# print(titles)
# titles = tree.xpath('//div[@class="p13n-sc-line-clamp-1"]')
# print(titles)

# SCRAPE GENRES
# do this after you do lexical analysis.
