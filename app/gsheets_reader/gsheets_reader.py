import pygsheets
import pandas


def get_gsheet():
    """ Connect to the Google sheet with LittleSis definitions """

    gsheet_client = pygsheets.authorize(service_file='gsheets_creds.json')

    # Get the appropriate Spreadsheet and worksheet
    SPREADSHEET = gsheet_client.open('LittleSis_Spreadsheet')
    WORKSHEET = SPREADSHEET.worksheet_by_title('definitions')

    # Turn the sheet into a pandas dataframe object 
    data_sheet = WORKSHEET.get_as_df()
    data_sheet = data_sheet.set_index("TERM", drop="True")
    return data_sheet


def get_definition(term):
    """ Access the google sheet and return the definition for the term.
        If the term does not exist in the sheet, an error message is returned """

    data_sheet = None
    definition = None    
    term = term.upper()

    data_sheet = get_gsheet()    
    try:
        definition = data_sheet.loc[term]['DEFINITION']
    except Exception as e:
        definition = "Unfortunately I don't have the term " + term + " in my dictionary"
    return definition
