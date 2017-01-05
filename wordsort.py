# Read in the txt file
# nb adding this to github 
import argparse # argparse module makes it easy to write user-friendly command-line interfaces.

#ALT METHOD filename = sys.argv[1]
#with open(filename, "r") as sourcefile:
parser = argparse.ArgumentParser() # first step when using argparse is to create a parser object, e.g., "parser" in this case
# argparse is a complete argument processing library. The parser class is ArgumentParser. The constructor can take various/several arguments
parser.add_argument('filename') # tell the parser what arguments to expect when the program runs
args = parser.parse_args() # args is a string
with open(args.filename) as sourcefile: # Use sourcefile to refer to the file object
  # do stuff here
    suffixstr = args.filename[-4:]  # the last 4 chars of gettysburg.txt e.g., ".txt"
    prefixstr = args.filename[0:-4] # the chars before .txt
    outputfilename = prefixstr + "-count" + suffixstr # use this to create the output filename form the input filename
    print("The sort will be saved in a file called " + '"' + outputfilename + '"')
    #if ("{}".format(suffixstr)) != ".txt":
     # print("you won't have got this far so how will you handle it\n")

    #if mystr != ".txt":                    # run a test based on it to ensure user specified a .txt file
        # handle it
        #print("you have to specify a .txt file as an argument\n")
    data = sourcefile.read()
    data = data.lower() # make everything lower case
    for ch in '"''!@#$%^&*()-_=+,<.>/?;:[{]}~`\|': # replace punctuation with whitespace
        data = data.replace(ch," ")
# do something with the data eg count the words, count unique words, list words in freq order

wordDict = {} # create empty dictionary

for word in data.split():
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] = wordDict[word] + 1



commonest = sorted(wordDict.items(), key = lambda x:(x[1],x[0]), reverse = True)
for word, freq in commonest:
    print ("%-13s %d" % (word, freq))  # The special operator % lets you create formatted output. It takes two operands: a formatted string and a value.


# Python lists have a built-in sort() method that modifies the list in-placs and a sorted() built-in function that builds a new sorted list from an iterable
# the sorted() function returns a list, even if that is not the type that was passed in
# the iterable can be a dictionary. A dictionary is actually a mapping rather than a list - so, an unordered set of key:value pairs. Each key is unique within the dictionary
# the iterable here is all of the the items contained in the dictionary wordDict, you iterate through the (word:no of occurrences of the word, key:value pairs) in wordDict
# the second parameter in the sorted function, the key parameter, should not be confused with the key in the key:value pairs in the dictionary, they are different things
# in the sorted function, the key (in this example) specifies (another) function (a lambda) to be called on each key:value mapping prior to making the sorting comparison
# x is all of the key:value mappings in wordDict, and x[1] just tells the sorted function to sort on the second element in each pair, e.g., the value, rather than x[0] the key
# if the values are the same then x[0] tellts the sorted function to sort on the first element in each pair, e.g., the word, alphabetically, but this is reversed by reverse = True
# i.e., pass a function that looks up the value associated with a key... to sort just the keys, based on their associated values, that's what lambda is doing here
# lambda's are anonymous functions. Function parameter(s) are specified before the colon. The function expression is specified after the colon. what is expressed is what is returned
# reverse = True returns largest to smallest order
# Commonest is the sorted list of words, sorted from most common to least common, extracted from wordDict


# write results
with open(outputfilename, "w") as outputfile:
    args = ("Total words: ", len(data.split()), " Unique words: ", len(commonest)) # str.split() without any arguments splits on runs of whitespace characters:
    summary = ("{} {} {} {}".format(*args))
    print(summary, '   >>> saved to ' + outputfilename)
    outputfile.write(summary)
    for word, freq in commonest:
      outputfile.write("\n\n%-13s %d \n" % (word, freq))


#sourcefile.close()
#outputfile.close()
