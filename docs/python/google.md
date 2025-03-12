---
title: Google APIs
parent: Python notes
layout: default
nav_order: 6
---

## PyDrive2 (Google Drive)

### Authentication with service account

Install pydrive2 via pip.

```
pip install pydrive2
```

You will need to register with Google Cloud to create a service account. This is like an additional Google Account but instead of being linked to a person, it is for use by programs and applications.

* Visit [https://console.cloud.google.com/](https://console.cloud.google.com/)
* Open the `APIs & Services` window
* Enable `Google Drive API`
* Open the `Credentials` window
* Download the service account key file to a secure location. This file is the equivilant to the password of the account. Whoever or whatever program that has access to it, can operate the service account.

```python
# Sourced from https://github.com/iterative/PyDrive2/issues/21#issuecomment-929186260
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/drive"]
gauth = GoogleAuth()
gauth.auth_method = 'service'
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
drive = GoogleDrive(gauth)

about = drive.GetAbout()

print('Current user name:{}'.format(about['name']))
print('Root folder ID:{}'.format(about['rootFolderId']))
print('Total quota (bytes):{}'.format(about['quotaBytesTotal']))
print('Used quota (bytes):{}'.format(about['quotaBytesUsed']))

file_list = drive.ListFile().GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
```

Rate limits apply. Per 60 seconds per user: 12,000 queries.

## Gspread (Google Sheets)

### Install and setup Gspread

Install gspread via pip.

```
pip install gspread
```

You will need to register with Google Cloud to create a service account. This is like an additional Google Account but instead of being linked to a person, it is for use by programs and applications.

* Visit [https://console.cloud.google.com/](https://console.cloud.google.com/)
* Open the `APIs & Services` window
* Enable `Google Sheets API` and `Google Drive API`
* Open the `Credentials` window
* Download the service account key file to a secure location. This file is the equivilant to the password of the account. Whoever or whatever program that has access to it, can operate the service account.

Setup variables with the key authorisation information needed for using gspread. Example:

```py
SERVICE_ACCOUNT_FILE = 'service_account.json'
SOURCE_ID = '1a2b3c4d5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w'
SHEET = "Sheet 1"
```

* The `SOURCE_ID` is the alpha-numeric code in the URL that uniquely identifies your particular Google Sheet.
* The `SHEET` is which sheet or tab, within the relevant Google Sheet, you wish to access.

### Establish connection with Google Sheet

The easiest, most common method, is to just load credentials from an external service account file.

```py
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
```

You can use a _dictionary_ that contains the data within the service account as well. This might be useful if you store your service account in a database or other mechanism.

```py
# Create a dictionary with the content of the service account
with open(SHEETS_SERVICE_ACCOUNT, "r", encoding="utf-8") as f:
    service_account_data = f.read()
# Use the dictionary object to connect
gc = gspread.service_account_from_dict(json.loads(service_account_data))
```

### Read from Google Sheet

Example 1

```py
# Fetch data from Google Sheet
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
sheet = gc.open_by_key(SOURCE_ID)
records = sheet.worksheet(SHEET).get_all_records()
# Create a Pandas data frame with all the records from the spreadsheet
df = pd.DataFrame(records)
# Save the Pandas data frame to a local Excel file
df.to_excel("my data.xlsx", index=False)
```

Example 2

```py
# Fetch data from Google Sheet
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
source = gc.open_by_key(SHEETS_ID)
records = source.worksheet(SHEETS).get_all_records()

# Iterate over the data
print(f"Retreived {len(records)} records.")
for i,record in enumerate(records):
    email = record["email"]     # Google Sheet column name
    name = record["name"]       # Google Sheet column name
    print(f"Person {name} has email address {email}.")
```

### Write to Google Sheet

```py
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
source = gc.open_by_key(SHEETS_ID)
sheet = source.worksheet(SHEETS)
records = sheet.get_all_records()

for i, row in enumerate(records):
    if row.get("name") == "Jane Doe":
        # Update row i+2 and column 11 with value provided
        sheet.update_cell(i + 2, 11, "jane.doe@gmail.com")  
```

* Note: The `i+2` is because of 0-indexing and that the first row of the Google Sheet are your column headers. This means the first record that will be iterated over will be row i+2 in the Google Sheet.

### More info

* [https://docs.gspread.org/en/v6.1.3/user-guide.html](https://docs.gspread.org/en/v6.1.3/user-guide.html)
