from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def creds_generator():
    creds = None
    if os.path.exists('../resources/token.json'):
        creds = Credentials.from_authorized_user_file('../resources/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../resources/credentials.json', SCOPES)
            creds = flow.run_local_server(port=9091)
        # Save the credentials for the next run
        with open('../resources/token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def post_new_event(list_events):
    for event in list_events:
        try:
            service = build('calendar', 'v3', credentials=creds_generator())
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
        except HttpError as error:
            print('An error occurred: %s' % error)


def get_today_events(date):
    try:
        service = build('calendar', 'v3', credentials=creds_generator())

        # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() # 'Z' indicates UTC time
        time_min = date.to_pydatetime().isoformat() + "-04:00"
        max_time = (date.to_pydatetime() + datetime.timedelta(hours=23,minutes=59,seconds=59)).isoformat() + "-04:00"

        print(time_min)
        print(time_min)
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=time_min,
                                              timeMax=max_time, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        print(events_result)
        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    get_today_events()
