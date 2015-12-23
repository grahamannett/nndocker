from apiclient.discovery import build

import json
import urllib.request
import urllib.parse
import urllib.error
import configparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
# with open('../credentials', 'r') as file:
#     DEVELOPER_KEY = file.readline()
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
# FREEBASE_SEARCH_URL = "https://www.googleapis.com/freebase/v1/search?%s"

config = configparser.ConfigParser()


class RelatedVids(object):

    def __init__(self, url):
        self.url = url
        self.related_vids = []

    def get_topic_id(options):
        # Retrieve a list of Freebase topics associated with the provided query
        # term.
        freebase_params = dict(query=options.query, key=DEVELOPER_KEY)
        freebase_url = FREEBASE_SEARCH_URL % urllib.parse.urlencode(
            freebase_params)
        freebase_response = json.loads(
            urllib.request.urlopen(freebase_url).read())

        if len(freebase_response["result"]) == 0:
            exit("No matching terms were found in Freebase.")

        # Display the list of matching Freebase topics.
        mids = []
        index = 1
        print("The following topics were found:")
        for result in freebase_response["result"]:
            mids.append(result["mid"])
            # print("  %2d. %s (%s)" % (index, result.get("name", "Unknown"),
            #                           result.get("notable", {}).get(
            #     "name", "Unknown")))
            index += 1

        # Display a prompt for the user to select topic and return the topic ID
        # of the selected topic.
        mid = None
        while mid is None:
            index = input("Enter a topic number to find related YouTube %s: " %
                          options.type)
            try:
                mid = mids[int(index) - 1]
            except ValueError:
                pass
        return mid

    def youtube_search(mid, options):
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)

        # Call the search.list method to retrieve results associated with the
        # specified Freebase topic.
        search_response = youtube.search().list(
            topicId=mid,
            type=options.type,
            part="id,snippet",
            maxResults=options.max_results
        ).execute()

        # Print the title and ID of each matching resource.
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                print("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["videoId"]))
            elif search_result["id"]["kind"] == "youtube#channel":
                print("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
            elif search_result["id"]["kind"] == "youtube#playlist":
                print("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["playlistId"]))
