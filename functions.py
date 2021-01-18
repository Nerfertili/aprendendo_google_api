from __future__ import print_function
import os
import oauth2client
from oauth2client import client, tools, file
try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class base_functions:
    def __init__(self,SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME ):
        self.SCOPES             = SCOPES
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE
        self.APPLICATION_NAME   = APPLICATION_NAME

    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'credentials.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials


    def rename_file(self,service, file_id, new_title):
        try:
            file = {'title': new_title}
            updated_file = service.files().patch(
                fileId=file_id,
                body=file,
                fields='title').execute()
            return updated_file
        except:
            print('An error occurred')
            return None


    def list_files_in_folder(self, service, folder_id, query):
        files = []

        while True:
            try:
                #print(query)
                children = service.children().list(folderId=folder_id, q = query).execute()
                #print(children)
                #print("\n"*3)
                for child in children.get('items', []):
                    #print(child)
                    files.append(child['id'])
                page_token = children.get('nextPageToken')
                if not page_token:
                    break
            except:
                print('An error occurred')
                break
        return files