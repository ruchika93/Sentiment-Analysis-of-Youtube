#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

##NOTE : The output of the program is a Video_ids.txt file which has the video_ids.
##By default only 50 video_ids fit in any response.



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey="<YOUR DEVELOPER KEY HERE>")

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  search_videos = []
  
  # Merge video ids
  
  for search_result in search_response.get("items", []):
    search_videos.append(search_result["id"]["videoId"])

  video_ids = "\n".join(search_videos)
  #print video_ids   #Ruchika

  file_write = open('video_ids/'+options.q+'_Video_ids.txt','w')
  file_write.write(video_ids)
  file_write.close()

  # # Call the videos.list method to retrieve location details for each video.
  # video_response = youtube.videos().list(
  #   id=video_ids,
  #   part='snippet, recordingDetails'
  # ).execute()

  # videos = []

  # # Add each result to the list, and then display the list of matching videos.
  # for video_result in video_response.get("items", []):
  #   videos.append("%s" % (video_result["snippet"]["title"]))
                              

  # #print "Videos:\n", "\n".join(videos), "\n"


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Roger Federer over the years")
  argparser.add_argument("--max-results", help="Max results", default=50)
  args = argparser.parse_args()
  # print args
  # print "\n"
  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
