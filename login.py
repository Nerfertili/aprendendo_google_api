
from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

class login:
    def Login_bgs(self):

        SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata'
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
        return DRIVE
