import re



def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" # emoticons
                           u"\U0001F300-\U0001F5FF" # symbols & pictographs
                           u"\U0001F680-\U0001F6FF" # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', string)


# unit testing
tweet_sample_w_emojis = '''A Couple Morning Plays With One        🔥 📈 Running Over 60% 📈 🔥'''

print(f'Original tweet with emojis: \t\t\t{tweet_sample_w_emojis}')
print(f'Tweet after using remove_emoji function: \t{remove_emoji(tweet_sample_w_emojis)}')




def remove_hyperlinks_twitter_marks (tweet):
    # it will remove the old style retweet text "RT"
    tweet2 = re.sub(r'^RT[\s]+', '', tweet)

    # it will remove hyperlinks
    tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet2)

    # it will remove hashtags. We have to be careful here not to remove 
    # the whole hashtag because text of hashtags contains huge information. 
    # only removing the hash # sign from the word
    tweet2 = re.sub(r'#', '', tweet2)

    # it will remove single numeric terms in the tweet. 
    tweet2 = re.sub(r'[0-9]', '', tweet2)
    return tweet2

# unit testing 

tweet_sample_w_links = 'Stats for the day have arrived. 1 new follower and NO unfollowers :) via http://t.co/0s8GQYOeus.'
print()
print(f'Original Tweet with hyperlinks and twitter marks: {tweet_sample_w_links}')
print(f'Tweet after removing hyperlinks twitter marks: {remove_hyperlinks_twitter_marks(tweet_sample_w_links)}')



