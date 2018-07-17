import app.gsheets_reader.gsheets_reader as gsheets_reader


class RP_JSON:
    """A JSON object detailing the JSON object to be sent
       back to RapidPro.

       RP_JSON {
           "query_result": the query result object returned by Dialogflow
           "query_text": the user query text 
           "intent": the expression upon which to split the RapidPro flow 
           "parameters": the infomration given by a user (if relevant)
           "fulfillment_text": the fulfuillment text from the Dialogflow agent"""

    def __init__(self, df_response):
        """Initialise a new RP_JSON object"""

        # Initalize the object
        self.query_result = df_response.query_result
        self.query_text = df_response.query_result.query_text
        self.parameters = "No Parameters"
        self.fulfillment_text = "No Fulfillment Text"
        self.set_intent()

    def set_intent(self):
        df_intent = self.query_result.intent.display_name
        df_action = self.query_result.action
        
        # Is this Small Talk?
        if (df_action.startswith("smalltalk")):
            intents = df_action.split(".")
            # Is this a confirmation? 
            if (intents[1] == 'confirmation'):
                if (intents[2] == 'yes') or (intents[2] == 'ready'):
                    self.intent = 'yes'
                else:
                    self.intent = 'no'
            # Otherwise
            else:
                self.intent = 'smalltalk' 
                self.fulfillment_text = self.query_result.fulfillment_text
                print("*" * 20)
                print(self.fulfillment_text)

        # Is this a Default Fall back ?
        elif (df_intent == "agent.default.fallback"):
            self.intent = "unidentified_intent"
            self.fulfillment_text = self.query_result.fulfillment_text
        
        # Is this a Default Welcome Intent ?
        elif (df_intent == "agent.default.welcome") or (df_intent == "Default Welcome Intent"):
            self.intent = "welcome_intent"
            self.fulfillment_text = self.query_result.fulfillment_text 

        # This is an Agent Defined intent
        else:
            self.intent = df_intent
            self.set_parameters()

    def set_parameters(self):
        intents = self.intent.split(".")
        # Handle case: Definition
        if (intents[2] == "define"):
            self.intent = "Definition"
            self.parameters = self.query_result.parameters['term']
            self.fulfillment_text = gsheets_reader.get_definition(str(self.parameters))
        
        # Handle case: Indentify theme
        if (intents[1] == "theme"):
            self.intent = intents[2]
            self.fulfillment_text = self.query_result.fulfillment_text 

