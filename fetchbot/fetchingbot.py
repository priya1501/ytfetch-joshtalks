from .models import Videos
from ytfetch_joshtalks import settings
from datetime import datetime, timedelta

# Google API client is required to connect YouTube Data API v3
from googleapiclient.discovery import build
from apiclient.errors import HttpError

#Function to fetch videos from YouTube API
def getnewposts():

    # Fetching keys from settings file
    apikeys = settings.API_KEYS
    current_time = datetime.now()

    # Since we need to get the posts which were posted 1minute from current_time
    req_time = current_time - timedelta(minutes=1) 

    # Flag variable ensures the successful fetching of the videos.
    flag = False
    for apikey in apikeys:
        try:

            # Using the documentation provided here : https://developers.google.com/youtube/v3/quickstart/python
            # Calling YouTube API
            youtube = build("youtube", "v3", developerKey=apikey)

            # The predefined query is 'football' here, calling an instance of the same
            req = youtube.search().list(q="football", part="snippet", order="date",
                                        maxResults=50, publishedAfter=(req_time.replace(microsecond=0).isoformat()+'Z'))
            response = req.execute()

            flag = True
            for obj in response['items']:
                title = obj['snippet']['title']
                description = obj['snippet']['description']
                publishingDateTime = obj['snippet']['publishedAt']
                thumbnailsUrls = obj['snippet']['thumbnails']['default']['url']
                channelTitle = obj['snippet']['channelTitle']

                # Saving details in the DB model
                Videos.objects.create(title=title, description=description,
                                      publishingDateTime=publishingDateTime, thumbnailsUrls=thumbnailsUrls,
                                      channelTitle=channelTitle)

        # If the quota for an API key is not exceeded keep on using the same key
        except HttpError as er:
            err_code = er.resp.status
            if not(err_code == 400 or err_code == 403):
                break

        if flag:
            break
