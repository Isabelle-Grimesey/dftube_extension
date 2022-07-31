# note - right now this is set for books.csv to have only title on each line
# writes data to wordlist.csv
# improvements (only if it's slow):
    # make dataframe->csv sorted in descending order
    # make titles searchable by keyword - would this be needed if people can use amazon?
    # remove all words with occurences < 1?
    # recognize proper nouns
    # fix porterstem's tendency to convert from y to i
    # speed improvement
        # is stopwords_list being sorted and intelligently searched behind the scenes?
        # if not, could I sort it and have the for x in a list comprehension do intelligent searching for me?
            #https://stackoverflow.com/questions/35988/c-like-structures-in-python
            #https://www.tutorialspoint.com/python-inserting-item-in-sorted-list-maintaining-order
        # how can I record runtime? I would like to see what 'improvements' have the biggest effect

# references:
    #https://medium.com/@siglimumuni/natural-language-processing-in-python-exploring-word-frequencies-with-nltk-918f33c1e4c3
    #https://www.quora.com/How-can-I-display-the-output-of-NLTKs-FreqDist-function-in-a-table-format
    #https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03


#import re
import nltk
# for tokenizing words
#nltk.download('punkt') # only have to run once
from nltk import word_tokenize
# for removing meaningless words - list is hard-coded from nltk (download took too long lol)
stopwords_list = ['of', 'that', 'one', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "i t's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'tha t', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'havi ng', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'o f', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'abov e', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'onc e', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'so me', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'just', 'don', "don't", 'should', "should've", 'now', 'd', '11', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'could n', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'shouldn', "should n't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
# for stemming words
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.probability import FreqDist # for counting and organizing by frequency
from matplotlib import pyplot as plt # for plotting common words to get a better idea of relative frequency
import pandas as pd # for storing results as a .csv file


input = open("books.txt", "r")
titles = input.read()
#tokenize titles into words
words_raw = word_tokenize(titles)
words = []

# clean up wordset from words_raw into words
for word in words_raw:
    if word.isalpha() and word.lower() not in stopwords_list: # it is not punctuation and it is a meaningful word
        words.append(ps.stem(word.lower())) # append lowercase version and stemmed word version so we don't end up with multiple versions of the same word, diluting its true frequency

#find the frequency of words
fdist = FreqDist(words)

# #print the 10 most common words
# print(fdist.most_common(100))

# get the most x common words, where x is number of words
# sorted_words = sorted(list(fdist.items()), )
print(fdist.most_common())
# fdist.most_common(len(fdist.items())) # look first for a default or all parameter, then directly for a size attribute - you don't want to return the whole list
# assuming most_common list is sorted by frequency, try selecting all words of a given frequency, then cut from the list
# else, binary search (bisect), most_common list (it should be sorted), checking the frequency of each word

# output fdist to a file
# pd.DataFrame(, columns = ["Word","Frequency"]).to_csv('wordlist.csv')



# #plot the 10 most common words
# fdist.plot(10)
# plt.show()
input.close()

#-----------------------------------------------------
# from dataclasses import dataclass
# @dataclass
# class Word_Occ:
#     word: str
#     num_occurences: int

# # the reason for my decision to have two separate lists for the same data is to reduce computation, even though it doubles storage.
# # i will `wordlist_by_word` sorted as I go so that searching it takes less time.
# # i will sort `wordlist_by_num_occ` afterwards since number of occurences change throughout the counting process.
# wordlist_by_word = []
# wordlist_by_num_occ = []
# import bisect
# with open("bookstest.csv", "r") as input:
#         title = input.readline()
#         while (title!=""):
#             words = word_tokenize(title)
#             for word in words: # for all tokens in this title
#                 if word.isalpha(): # remove punctuation
#                     word = ps.stem(word.lower()) # make lowercase and stem
#                     if word not in stopwords_list: # remove meaningless words
#                         in_list= False
#                         i = bisect.bisect_left(wordlist_by_word, word) # locates insertion point for word in sorted wordlist; would be inserted to the left of any duplicates
#                         if i < len(wordlist_by_word)-1 and wordlist_by_word[i+1]==word:
#                             wordlist_by_num_occ[i+1].num_occurences += 1
#                         else:
#                             # this is the first occurence of this word across all analyzed titles
#                             wordlist_by_word.insert(i, word) # note we are counting total occurences of a word; not the number of titles that a word appears in; they should be roughly the same, unless there happens to be a bestseller that's jammed its title with the same keyword again and again, which is unlikely. Besides, such titles would indicate particularly heavy popularity of the topic.
#                             wordlist_by_num_occ.insert(i, Word_Occ(word, 1))
#             title = input.readline()

# # wordlist is now full with number of occurences for each word
# # sort wordlist by number of occurences
# wordlist_by_num_occ = sorted(wordlist_by_num_occ, key=lambda x: x.num_occurences, reverse=True)
# # output to csv
# with open("analysis.csv", "w") as output:
#     for word in wordlist_by_num_occ:
#         output.write(str(word.num_occurences) + "," + word.word)

# with open("words_alphabetized.csv", "w") as output:
#     for word in wordlist_by_word:
#         output.write(word)
    


#print(titles)
# wordlist = open("wordlist.csv", "w")
# wordlist.close()

# for title in titles:
#     words = [title.split(" ")]
#     print(words)

# for each title
#   for each word
#       if meaningful
            # take base form
            # if base form in set
                # increment value
            #else
                    #add to set a dict (key = word, value = 1)

# sort set by num_occurences, in descending order
# print it to a file

# extending analysis
    # do whether or not single wordset is uninformative
        # genre
        # increase number of books
    # do only if single wordset is informative
        # double wordset, etc - until no longer informative