import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

scope = ['https://spreadsheets.google.com/feeds']
creds = sac.from_json_keyfile_name('client_secret.json', scope)

sheet = client.open('NSF Progress Spreadsheet').sheet1

all_data = sheet.get_all_records()
print(all_data)

