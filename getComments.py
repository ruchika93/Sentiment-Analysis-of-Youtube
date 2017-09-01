#!/usr/bin/python

#key:  AIzaSyA4t3iO_ObJTneR4gbH4XwHRxam7c8a5bQ 
# Usage example:
# python comment_threads.py --channelid='<channel_id>' --videoid='<video_id>' --text='<text>'

import httplib2
import os
import sys
import csv
import json

from apiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains

# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Developers Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = "jgjfdghdj"
"""WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
https://console.developers.google.com

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname('client_secrets.json'),
                                   CLIENT_SECRETS_FILE))

# Authorize the request and store authorization credentials.
def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  # Trusted testers can download this discovery document from the developers page
  # and it should be in the same directory with the code.
  with open("youtube-v3-discoverydocument.json", "r") as f:
    doc = f.read()
    return build_from_document(doc, http=credentials.authorize(httplib2.Http()))


# Call the API's commentThreads.list method to list the existing comments.
def get_comments(youtube, video_id, channel_id):
  results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    channelId=channel_id,
    maxResults = 100,
    textFormat="plainText"
  ).execute()
  print video_id
  filename = "fetchedComments/RF_years/"+video_id.strip()+".json"
  print filename
  tempComments =[]
  for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    tempComment = dict(author = comment["snippet"]["authorDisplayName"],likes = comment["snippet"]["likeCount"],publishedAt=comment["snippet"]["publishedAt"],text = comment["snippet"]["textDisplay"].encode('utf-8').strip())
    tempComments.append(tempComment)

  with open(filename,"w") as fp:
    json.dump(tempComments, fp)
  print tempComments
  return results["items"]


if __name__ == "__main__":
  # The "channelid" option specifies the YouTube channel ID that uniquely
  # identifies the channel for which the comment will be inserted.
  argparser.add_argument("--channelid",
    help="Required; ID for channel for which the comment will be inserted.")
  # The "videoid" option specifies the YouTube video ID that uniquely
  # identifies the video for which the comment will be inserted.
  argparser.add_argument("--videoid",
    help="Required; ID for video for which the comment will be inserted.")
  # The "text" option specifies the text that will be used as comment.
  argparser.add_argument("--text", help="Required; text that will be used as comment.")
  args = argparser.parse_args()

  file = open("video_ids/Roger Federer over the years_Video_ids.txt","r")
  for line in file:
    vidId = line

    youtube = get_authenticated_service(args)

    try:
      video_comments = get_comments(youtube, vidId, None)
    
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

