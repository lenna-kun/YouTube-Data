# -*- coding: utf-8 -*-

import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.discovery import build
from apiclient.errors import HttpError
import pickle
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']
CLIENT_SECRETS_FILE = 'FILE NAME HERE!!!'
YOUTUBE_DATA_API_KEY = 'API KEY HERE!!!'
CHANNEL_ID = 'CHANNEL ID HERE!!!'

def get_services():
    credentials=None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build("youtube", "v3", developerKey=YOUTUBE_DATA_API_KEY), build("youtubeAnalytics", "v2", credentials = credentials)

def get_videos(service):
    videos = []
    nextPagetoken = None
    nextpagetoken = None
    while True:
        if nextPagetoken != None:
            nextpagetoken = nextPagetoken

        search_response = service.search().list(
            part = "snippet",
            channelId = CHANNEL_ID,
            maxResults = 50,
            order = "date",
            pageToken = nextpagetoken
        ).execute()
    
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append([search_result["id"]["videoId"]])

        try:
            nextPagetoken =  search_response["nextPageToken"]
        except:
            break

    for video in videos:
        video_response = service.videos().list(
            part = 'snippet,statistics',
            id = video
        ).execute()

        for video_result in video_response.get("items", []):
            if video_result["kind"] == "youtube#video":
                video.extend([video_result["snippet"]["title"], video_result["statistics"]["viewCount"], video_result["snippet"]["publishedAt"]])
    return videos

def execute_api_request(client_library_function, **kwargs):
    return client_library_function(
        **kwargs
    ).execute()

if __name__ == '__main__':
    services = get_services()
    videos = get_videos(services[0])

    for video in videos:
        startDate = video[3].split("T")[0]
        year, month, day = [int(i) for i in startDate.split("-")]
        if month == 2:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                endDate = f"{year}-02-29"
            else:
                endDate = f"{year}-02-28"
        elif month == 4 or month == 6 or month == 9:
            endDate = f"{year}-{month:0>2}-30"
        else:
            endDate = f"{year}-{month:0>2}-31"

        if day == 1:
            if month == 1:
                startDate = f"{year-1}-12-31"
            elif month == 3:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    startDate = f"{year}-02-29"
                else:
                    startDate = f"{year}-02-28"
            elif month == 5 or month == 7 or month == 10:
                startDate = f"{year}-{month-1:0>2}-30"
            else:
                startDate = f"{year}-{month-1:0>2}-31"
        else:
            startDate = f"{year}-{month:0>2}-{day-1:0>2}"

        result = execute_api_request(
            services[1].reports().query,
            ids=f"channel=={CHANNEL_ID}",
            startDate=startDate,
            endDate=endDate,
            filters=f"video=={video[0]}",
            metrics="views"
        )
        video.append(result["rows"][0][0])
    
    videos_report = pd.DataFrame(videos, columns=['ID', 'Title', 'Views', 'PublishedAt', 'FirstMonthViews'])
    videos_report.to_csv("videos_report.csv", index=None)