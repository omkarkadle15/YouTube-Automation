import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            credentials = flow.run_local_server(port=8080)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    
    return build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, file_path, title, description, category, keywords, privacyStatus='private'):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': keywords,
            'categoryId': category
        },
        'status': {
            'privacyStatus': privacyStatus
        }
    }

    media = MediaFileUpload(file_path, resumable=True)
    
    try:
        request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        response = request.execute()
        print(f'Video uploaded successfully! Video ID: {response["id"]}')
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred:\n{e.content}')

def main():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    youtube = get_authenticated_service()
    
    file_path = 'PATH_TO_YOUR_.mp4_FILE'
    title = 'TITLE_OF_YOUR_VIDEO'
    description = 'DESCRIPTION'
    category = '22'  # See https://developers.google.com/youtube/v3/docs/videoCategories/list
    keywords = ['keyword1', 'keyword2']
    
    upload_video(youtube, file_path, title, description, category, keywords)

if __name__ == '__main__':
    main()