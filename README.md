# popular_audiobook_topics
Determines the most popular topics within Amazon's top 100 "Best Sellers in Audible Books & Originals."

 pull_100 performs the initial scrape of the titles into books.csv.
 analyze.py analyzes the titles and stores results in analysis.csv.

# TO DO
 transition from csv to sql
 include genre data
 be more semantically selective
 find database hosting, scale up to top 10,000
 figure out display
 figure out how to update - sql - "https://www.sqlshack.com/getting-started-with-data-tier-applications-in-visual-studio/"

 figure out why it takes so long to run

 eventually use bisect on stopwords too - only if stopwords list gets big enough - also, it would be cheating to cherry-pick my values for stopwords based on what was in the titles - or would it?

 analyze genre together or apart from word frequency? - together is more work (more parsing), but it might be easier if i am using database; only if needed
