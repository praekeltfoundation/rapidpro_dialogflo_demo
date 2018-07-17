import logging
import pygsheets
import pandas


def get_gsheet():
    """ Connect to the Google sheet with LittleSis definitions """

    gc = pygsheets.authorize(service_file='gsheets_creds.json')

    # Get the appropriate Spreadsheet and worksheet
    SPREADSHEET = gc.open('LittleSis_Spreadsheet')
    WORKSHEET = SPREADSHEET.worksheet_by_title('definitions')

    # Turn the sheet into a pandas dataframe object 
    df = WORKSHEET.get_as_df()
    df = df.set_index("TERM", drop="True")
    return df


def get_definition(term):
    """ Access the google sheet and return the definition for the term.
        If the term does not exist in the sheet, an error message is returned """

    df = None
    definition = None    
    term = term.upper()

    df = get_gsheet()    
    try:
        definition = df.loc[term]['DEFINITION']
    except Exception as e:
        definition = "Unfortunately I don't have the term " + term + " in my dictionary"
    return definition
