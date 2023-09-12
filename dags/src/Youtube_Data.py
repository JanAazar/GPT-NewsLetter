# from googleapiclient.discovery import build
# from auth import youtube_api_key as API_KEY

# youtube = build('youtube', 'v3', developerKey=API_KEY)

# # Specify the parameters for the API request
# request = youtube.search().list(
#     part='id',
#     type='channel',
#     q='CNBC Telivision'  # Replace with the name or keyword of the YouTube channel
# )

# # Execute the API request and retrieve the response
# response = request.execute()

# # Extract the channel ID from the API response
# channel_id = response['items'][0]['id']['channelId']

# # print(f'Channel ID: {channel_id}')

# def get_channel_videos(channel_id):
#     videos = []
#     video_ids = []
#     next_page_token = None
#     while True:
#         response = youtube.search().list(
#             part='id,snippet',  # Include snippet in part parameter
#             type='video',
#             channelId=channel_id,
#             maxResults=50,  # Adjust this value as needed
#             pageToken=next_page_token,
#             publishedAfter='2023-07-23T00:00:00Z'  # Adjust this value as needed
#         ).execute()
#         videos += response['items']
#         video_titles = [item['snippet']['title'] for item in response['items']]
#         video_ids += [item['id']['videoId'] for item in response['items']]
#         video_urls = ["https://www.youtube.com/watch?v=" + video for video in video_ids]
#         next_page_token = response.get('nextPageToken')
#         if not next_page_token:
#             break
#     return video_urls,video_titles

# urls,titles = get_channel_videos(channel_id)
# result = list(zip(urls,titles))
# print(result)
# # print(len(result))





