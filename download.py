



from flask import Flask#
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload
import io

app = Flask(__name__)

# define path variables
credentials_file_path = './credentials/credentials.json'
clientsecret_file_path = './credentials/client_secret.json'

# define API scope
SCOPE = 'https://www.googleapis.com/auth/drive'

# define store
store = file.Storage(credentials_file_path)
credentials = store.get()
# get access token
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(clientsecret_file_path, SCOPE)
    credentials = tools.run_flow(flow, store)


from apiclient import discovery, errors
from httplib2 import Http                                                                                                                                               from oauth2client import client, file, tools                                                                                                                                                                                                                                                                                                    
# define API service
http = credentials.authorize(Http())
drive = discovery.build('drive', 'v3', http=http)

@app.route('/download', methods=['GET'])
# define a function to retrieve all files
def retrieve_all_files():
    results = []
    page_token = None