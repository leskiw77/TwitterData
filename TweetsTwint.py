import twint

c = twint.Config()
c.Username = "twitter"

c.Limit = 10


c.Store_object = True

twint.run.Search(c)
twint.output.tweets_object


twint.run.Search(c)


# tweets_as_objects = twint.output.tweets_object
# tweet = tweets_as_objects[1]
print (dir(twint.output.Tweets()))
