# 1) Go to GCP > APIs & Services > Credentials >  
#    Create Credentials > Manage Seervice Accounts > 
#    Make a new service account 
# 2) Share your spreadsheet with the Service Account: gsheetsaccess@littlesis-a5948.iam.gserviceaccount.com
# 3) Run the quickstart, it will inform you that you need to go here to active the Drive API: https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=3226912007
# 4) Run again, this time it will work :) 

import pygsheets
import pandas

def get_gsheet():
    """ Connect to the Google sheet where sheet is 
        the name of the google sheet to be accessed
    """
    print("*" * 20 + "\n get_gsheet entered")
    gc = pygsheets.authorize(service_file='gsheets_creds.json')

    # Get the appropriate Spreadsheet and worksheet
    SPREADSHEET = gc.open('LittleSis_Spreadsheet')
    WORKSHEET = SPREADSHEET.worksheet_by_title('definitions')

    # Turn the sheet into a pandas dataframe object 
    df = WORKSHEET.get_as_df()
    print("** TERM")
    df = df.set_index("TERM", drop="True")
    return df

def get_cell_data(term, key, df):
    ''' Get the value in the cell at 
        name (row name) and key (column name)
        from the sheet (name of the sheet)'''
    term = term.upper()
    key = key.upper()
    value = df.loc[term][key]
    return value

def get_definition(term):
    ''' Access the google sheet and return the
        key value for the term
        
        term - term to be defined
        key - definition to return
        sheet - name of google sheet to read'''
    value = None
    df = None
    try:
        df = get_gsheet()    
    except:
        print("Sheet could not be fetched")
        print("*** gsheet fetched")
        

    try:
        value = get_cell_data(term, 'Definition', df)
    except Exception as e: 
        print("Value could not be extracted")
        print("Error: " + str(e))
    return value 
