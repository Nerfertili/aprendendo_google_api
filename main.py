# primeiro teste arquivo igual 00108780000198
# segundo teste arquivo R2 ja existente 00535340000117

from __future__ import print_function
import httplib2
import os
import json
from apiclient import discovery
import oauth2client
from oauth2client import tools, file, client
import functions
import re

functions.base_functions.
#constants for login
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Drive API Python Quickstart'

drive_status =  functions.base_functions(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = drive_status.get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('drive', 'v2', http=http)

#teste com cnpjs
legal_person = '00535340000117'
now_date = '02/10/2020'.replace('/','_')
print(now_date)
#constants
root = 'root'

def find_existed_file(service,root,legal_person,now_date):
    root_files = drive_status.list_files_in_folder(service,root,f"title='{legal_person}'")[0]
    print(root_files)
    zero_tres_file = drive_status.list_files_in_folder(service,root_files,"title='03. Controle de Mensagens'")[0]
    print(zero_tres_file)
    now_date_file = drive_status.list_files_in_folder(service,zero_tres_file,f"title contains '{now_date}'")
    print(now_date_file)
    if len(now_date_file) > 1:
        print('was present more than one file with the date checking Rn')
        date_file_name = []
        for id in now_date_file:
            name = service.files().get(fileId=id).execute()['title']
            date_file_name.append(name)
        # now_date+"_R"+Numero
        dic_of_name_numbers = {}
        for data in date_file_name:
            number_date = re.match(f"{now_date}_R(\d)",data).group(0)
            dic_of_name_numbers[data] = number_date
        numbers_array = []
        for key in date_file_name:
            numbers_array.append(dic_of_name_numbers[key])
        numbers_array.sort()
        biggest_value = numbers_array[(len(numbers_array))-1]
        for value in date_file_name:
            if dic_of_name_numbers[value] == biggest_value:
                recent_file = value
        renamed_file = recent_file
        return renamed_file

    else:
        renamed_file = drive_status.rename_file(service,now_date_file[0],now_date+'_R1')

    return renamed_file['title']

if __name__ == '__main__':
    teste = find_existed_file(service,root,legal_person,now_date)
    print(teste)