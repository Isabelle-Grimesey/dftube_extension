# scrape and compare against books.csv
    #option 1: if rank has changed title, update the rank in books.csv
    #option 2: ranks may have interchanged titles without leaving set; in this case analysis would not change but books.csv would change
        # what i need is a set rather than a list
        # scrape new set, compare to old set, update analysis according to discrepancies, then add and remove elements to old set until it is new set

# only write a line to the csv if it is new