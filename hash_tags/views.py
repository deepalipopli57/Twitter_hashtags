from django.shortcuts import render
from twython import Twython

from twitter_hashtags.local_settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

#api for fetch 10 most used hashtags for word "top in the given twitter credentials
def twitter_hashtags(request):
    user = Twython(app_key=CONSUMER_KEY,
                  app_secret=CONSUMER_SECRET,
                  oauth_token=ACCESS_TOKEN,
                  oauth_token_secret=ACCESS_TOKEN_SECRET
                  )
    # word - Tag which we want to search from twitter account
    search_results = user.search(q="#top", count=10)
    statuses = search_results['statuses']
    tags = [hashtag['text']
                for status in statuses
                for hashtag in status['entities']['hashtags']][0:10]
    return render(request, 'tags.html', {'data': tags})


