import twint

custom_query = ""
hashtags = {}

with open('K_followers.csv', 'r') as input:
    # we can ignore the first row
    input.readline()
    line = input.readline()
    while line:
        user = line.split(',')[1]
        hashtags.update({user: {}})
        custom_query += "from:{} OR ".format(user)
        line = input.readline()
    custom_query = custom_query[:-4]

c = twint.Config()
c.Custom_query = custom_query
c.Store_object = True
c.Store_csv = True
c.Output = "tweets.csv"

# we want to hide the output, there will be a lot of tweets and the terminal might crash
c.Hide_output = True

twint.run.Search(c)

tweets = twint.output.tweets_object

# now we have all the tweets, let's elaborate the data

# first iterate over the tweets
for t in tweets:
    # then iterate over the hashtags of that single tweet
    for h in t.hashtags:
        # increment the count if the hashtag already exists, otherwise initialize it to 1
        try:
            hashtags[t.username][h] += 1
        except KeyError:
            hashtags[t.username].update({h: 1})

# now save the data
with open('hashtags.csv', 'w') as output:
    output.write('username,hashtag,count\n')
    for user in hashtags:
        for h in hashtags[user]:
            output.write('{},{},{}\n'.format(user, h, hashtags[user][h]))