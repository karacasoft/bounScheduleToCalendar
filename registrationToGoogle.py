#!/usr/bin/env python

from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from googleapiclient.http import BatchHttpRequest
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file

import os, httplib2
from datetime import datetime, timedelta

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'BOUN Registration to Calendar'

SCHOOL_END_DATE = "20170120"

slots = []
slotEndTimes = []
slot_date = datetime.strptime("19 09 2016 09:00:00", "%d %m %Y %H:%M:%S")
slot_end_date = datetime.strptime("19 09 2016 09:50:00", "%d %m %Y %H:%M:%S")

for i in range(0, 14):
    extended_slot_date = slot_date + timedelta(hours = i)
    slots.append(extended_slot_date)
    slotEndTimes.append(extended_slot_date + timedelta(minutes = 50))

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

def parseColumns(row):
    entries = []
    cols = row.find_all("td")
    i = 0
    for col in cols:
        if len(col.contents) > 1:
            if (len(entries) > 0) and (entries[-1]["name"] == col.contents[0].strip()):
                entries[-1]["end"] = i
                pass
            else:
                lesson = {
                    "name" : col.contents[0].strip(),
                    "slot" : i,
                    "end" : i,
                    "place" : col.contents[1].get_text()
                }
                entries.append(lesson)
            #print str(i) + ". Slot : " + col.contents[0].strip() + " at " + col.contents[1].get_text()
        i = i + 1
    return entries

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def createCalendar(service):
    """
    Creates a calendar on Google Calendar.
    Returns its id.
    """
    calendarInfo = {
        "summary" : "Boun Dersler",
        "description" : "This calendar was generated automatically by KaracaSoft\'s Registration to Google Calendar project."
    }

    creationResult = service.calendars().insert(fields="id", body=calendarInfo).execute()
    calendarId = creationResult.get("id")
    return calendarId



def fillCalendar(cId, service, rows):
    batch = service.new_batch_http_request()

    for i in xrange(1, len(rows)):
        row = rows[i]
        entries = parseColumns(row)

        for entry in entries:
            #print (slots[entry["slot"]] + timedelta(days=(i-1))).isoformat()
            if entry["name"] == "":
                #conflict var
                continue
            else:
                eventDetails = {
                    "summary" : entry["name"],
                    "location" : entry["place"],
                    "start" : {
                        "dateTime" : (slots[entry["slot"] - 1] + timedelta(days=(i-1))).isoformat(),
                        "timeZone" : "Asia/Istanbul"
                    },
                    "end" : {
                        "dateTime" : (slotEndTimes[entry["end"] - 1] + timedelta(days=(i-1))).isoformat(),
                        "timeZone" : "Asia/Istanbul"
                    },
                    "recurrence" : [
                        "RRULE:FREQ=WEEKLY;UNTIL=" + SCHOOL_END_DATE
                    ]
                }
                service.events().insert(calendarId=cId, body=eventDetails).execute()
                print "Entry processed"
    

regFile = open("registrationPage.htm", "r")
regPage = regFile.read()

soup = BeautifulSoup(regPage, "html.parser")

tables = soup.find_all("table")

schedule = tables[1]

rows = schedule.find_all("tr")


credentials = get_credentials()
http = credentials.authorize(httplib2.Http())

service = build("calendar", "v3", http=http)

cId = createCalendar(service)
fillCalendar(cId, service, rows)










