#The keyword global
import pandas as pd
team = "teen titans"
def change_team():
    """Change the value of the global variable team."""
    global team 
    team = "justice league"
print(team)
change_team()
print(team)
#Nested Functions I

def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    return (inner(word1),inner(word2),inner(word3))
print(three_shouts('a', 'b', 'c'))
#Nested Functions II

def echo(n):
    """Return the inner_echo function."""

    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    return inner_echo

twice = echo(2)

thrice = echo(3)

print(twice('hello'), thrice('hello'))

#The keyword nonlocal and nested functions

def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    echo_word = word*2
    
    print(echo_word)
    
    def shout():
        """Alter a variable in the enclosing scope"""
        
        nonlocal echo_word
        
        echo_word = echo_word + '!!!'
    
    shout()
    
    print(echo_word)

echo_shout('is it working? ')

#Functions with one default argument

def shout_echo(word1, echo =1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    echo_word = echo*word1

    shout_word = echo_word + '!!!'

    return shout_word

no_echo = shout_echo('Hey')

with_echo = shout_echo('Hey', 5)

print(no_echo)
print(with_echo)

#Functions with multiple default arguments

def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    
    echo_word = word1 * echo

    if intense is True:
        echo_word_new =echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'

    return echo_word_new

with_big_echo = shout_echo("Hey",5,True)

big_no_echo = shout_echo("Hey",intense=True)

print(with_big_echo)
print(big_no_echo)

#Functions with variable-length arguments (*args) 

def gibberish(*args):
    """Concatenate strings in *args together."""

    hodgepodge = ''

    for word in args:
        hodgepodge += word

    return hodgepodge

        # Call gibberish() with one string: one_word
one_word = gibberish("luke")

        # Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

print(one_word)
print(many_words)

#Functions with variable-length keyword arguments (**kwargs)

def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

report_status(name="luke", affiliation="jedi", status="missing")
report_status(name="anakin", affiliation="sith lord", status="deceased")

#Bringing it all together (1)

tweets_df = pd.read_csv('tweets.csv')

def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

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

result1 = count_entries(tweets_df)
result2 = count_entries(tweets_df,col_name='source' )

print(result1)
print(result2)

#Bringing it all together (2)
def count_entries(df,*args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
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
    return cols_count

result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'lang' , 'source')
print(result1)
print(result2)




