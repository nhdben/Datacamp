import pandas as pd

# Write a simple function
def shout():
    """Print a string with three exclamation marks"""
    shout_word= 'congratulations'+ '!!!'
    print(shout_word)
# Call shout
shout()
#Single-parameter functions

def shout(word):
    """Print a string with three exclamation marks"""
    shout_word =word + '!!!'
    print( shout_word)
shout('congratulations2')
#Functions that return single values

def shout(word):
    """Return a string with three exclamation marks"""
    shout_word = word + '!!!'
    return(shout_word)
yell=shout('congratulations3')
print(yell)
# Functions with multiple parameters
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    new_shout = shout1 + shout2
    return new_shout
yell = shout('congratulations', 'you')
print(yell)
#A brief introduction to tuples
nums=(3, 4, 6)
num1, num2, num3 = nums
even_nums = (2, num2, num3)
#Functions that return multiple values
def shout_all(word1, word2):
    """Return a tuple of strings"""
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    shout_words = (shout1, shout2)
    return shout_words

yell1, yell2 = shout_all('congratulations', 'you')
print(yell1)
print(yell2) 
#Bringing it all together (1)

df = pd.read_csv('tweets.csv')
langs_count = {}
col = df['lang']
for entry in col:
    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
print(langs_count)
#Bringing it all together (2)
tweets_df = pd.read_csv('tweets.csv')
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    langs_count = {}
    col = df[col_name]
    
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count
result = count_entries(tweets_df,'lang')
print(result)

