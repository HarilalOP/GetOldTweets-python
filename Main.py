import sys
import json
from datetime import date, timedelta
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():
	def getJson(t):
		data = {}
		data['Tweetid'] = t.id
		data['Permalink'] = repr(t.permalink)
		data['formatted_date'] = t.formatted_date
		data['Userid'] = t.author_id
		data['Username'] = repr(t.username)
		data['Text'] = repr(t.text)
		data['Retweets'] = t.retweets
		data['Favorites'] = t.favorites
		data['Mentions'] = t.mentions
		data['Hashtags'] = repr(t.hashtags)
		data['Geo'] = t.geo
		return data

	def printTweet(descr, t):
		print(descr)
		print("permalink: %s" % t.permalink)
		print("Userid: %s" % t.author_id)
		print("Username: %s" % t.username)
		print("Text: %s" % t.text)
		print("Retweets: %d" % t.retweets)
		print("Favorites: %s" % t.favorites)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)
		print("Geo: %s\n" % t.geo)

	# Example 1 - Get tweets by username
	tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)



	# Example 2 - Get tweets by query search
	d1 = date(2018, 5, 11)  # start date
	d2 = date(2018, 5, 12)  # end date

	delta = d2 - d1  # timedelta

	file = 'tweets_bo.json'

	for i in range(0, delta.days + 1, 2):
		date_one = str(d1 + timedelta(i))
		date_two = str(d1 + timedelta(i + 1))
		print('fetching tweets from %s to %s'%(date_one, date_two))
		tweetCriteria = got.manager.TweetCriteria().setQuerySearch('barackobama').setSince(date_one).setUntil(date_two)
		tweets = got.manager.TweetManager.getTweets(tweetCriteria)

		for tweet in tweets:
			data = getJson(tweet)
			with open(file, 'a') as json_file:
				json.dump(data, json_file)
				json_file.write('\n')

	printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)

	# Example 3 - Get tweets by username and bound dates
	tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

if __name__ == '__main__':
	main()