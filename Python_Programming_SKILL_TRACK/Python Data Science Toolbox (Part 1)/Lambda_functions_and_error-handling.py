import pandas as pd 
from functools import reduce 
#Writing a lambda function you already know

echo_word = (lambda word1, echo: word1 * echo)
result = echo_word('hey', 5)
print(result)

#Map() and lambda functions
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item +'!!!', spells)
# Convert shout_spells to a list:
shout_spells_list = list(shout_spells)
print(shout_spells_list)

#Filter() and lambda functions

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda a: len(a) > 6, fellowship)
result_list = list(result)
print(result_list)

#Reduce() and lambda functions


stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result = reduce(lambda item1,item2 : item1 + item2 , stark)
print(result)

#Error handling with try-except 

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    echo_word = ''
    shout_words = ''

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = echo*word1

        # Concatenate '!!!' to echo_word: shout_words
        shout_words =  echo_word +'!!!' 
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    
    return shout_words

shout_echo("particle", echo="accelerator")

#Error handling by raising an error

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0 :
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

shout_echo("particle", echo=-1)

#Bringing it all together (1)

tweets_df = pd.read_csv('tweets.csv')
# Select retweets from the Twitter DataFrame
result = filter(lambda x : x[0:2]== 'RT', tweets_df['text'])

# Create list from filter object result: 
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

#Bringing it all together (2)

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:

            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        'The DataFrame does not have a ' + col_name + ' column.'

result1 = count_entries(tweets_df, 'lang')
print(result1)

#Bringing it all together (3)

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

result1 = count_entries(tweets_df , 'lang')
print(result1)
