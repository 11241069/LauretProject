import os
import json as simplejson
from apiclient.discovery import build
from flask import Flask,render_template, request,json

app = Flask(__name__)


@app.route('/')
def findchannel():
    return render_template('index.html')

@app.route('/FindVideosChannelGet', methods=['GET'])
def FindVideosChannelGet():
    
    API_KEY = "AIzaSyBeE-EenFUhqKpSB2YpPyZIvEZhc9rAHb8" 
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"


    author = 'LaureateChannel'

    foundAll = False
    ind = 1
    videos = []
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                        YOUTUBE_API_VERSION,
                        developerKey=API_KEY)
    channels_response = youtube.channels().list(
                forUsername="LaureateChannel",
                part='snippet,contentDetails'
          ).execute()

    for channel in channels_response['items']:
      uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']
      channel_name = channel['snippet']['title']

    next_page_token = ''
    number=0;
    while next_page_token is not None:
        playlistitems_response = youtube.playlistItems().list(
            playlistId=uploads_list_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for playlist_item in playlistitems_response['items']:
            
            videos.append({'id':number,'title':playlist_item['snippet']['title'],'description':playlist_item['snippet']['description']})
            number+=1;
        next_page_token = playlistitems_response.get('nextPageToken')
        print(next_page_token)
        
        
    return json.dumps(videos);
@app.route('/FindVideosChannel', methods=['POST'])
def FindVideosChannel():
    user =  request.form['searchname'];
    API_KEY = "AIzaSyBeE-EenFUhqKpSB2YpPyZIvEZhc9rAHb8" 
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"


    author = 'LaureateChannel'

    foundAll = False
    ind = 1
    videos = []
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                        YOUTUBE_API_VERSION,
                        developerKey=API_KEY)
    channels_response = youtube.channels().list(
                forUsername="LaureateChannel",
                part='snippet,contentDetails'
          ).execute()

    for channel in channels_response['items']:
      uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']
      channel_name = channel['snippet']['title']

    next_page_token = ''
    number=0;
    while next_page_token is not None:
        playlistitems_response = youtube.playlistItems().list(
            playlistId=uploads_list_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for playlist_item in playlistitems_response['items']:
            if playlist_item['snippet']['title']==user:
                videos.append({'id':number,'title':playlist_item['snippet']['title'],'description':playlist_item['snippet']['description']})
            if ''==user:
                videos.append({'id':number,'title':playlist_item['snippet']['title'],'description':playlist_item['snippet']['description']})
            number+=1;
        
        next_page_token = playlistitems_response.get('nextPageToken')
        print(next_page_token)
        
    return json.dumps(videos);
if __name__=="__main__":
    app.run()
