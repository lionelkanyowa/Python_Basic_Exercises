# Q.8: The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long')

length_of_tweet = len(tweet + 5)

# When running this code we get a TypeError, and the reasoning is that we can only concatenate strings
# not integers. We are trying to concatenate an integer in line 8. Rememebr we cannot concatenate a string and
# and an integer, this raises a TypeError.