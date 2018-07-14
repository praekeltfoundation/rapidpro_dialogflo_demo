import dialogflow
from flo_detect_intent import detect_intent_texts


class RP_JSON:
    """A JSON object detailing how RapidPro should respond"""

    def __init__(self, df_response):
        """Initialise a new NLU_response with correct fields"""

        # TODO handle empty df_response - handle on response_handler side
        
        # Initalize the object
        self.query_result = df_response.query_result
        self.parameters = "No Parameters"
        self.fulfillment_text = "No Fulfillment Text"

        self.set_intent()

        print("intent: " + self.intent)
        print("params: " + self.parameters)
        print("fulfillment: " + self.fulfillment_text)

    def set_intent(self):
        df_intent = self.query_result.intent.display_name
        df_action = self.query_result.action
        
        # Is this Small Talk
        if (df_action.startswith("smalltalk")):
            intents = df_action.split(".")
            # Is this a confirmation? 
            if (intents[1] == 'confirmation'):
                if (intents[2] == 'yes'):
                    self.intent = 'yes'
                else:
                    self.intent = 'no'
            else:
                self.intent = 'smalltalk' 
                self.fulfillment_text = self.query_result.fulfillment_text
                print("*" * 20)
                print(self.fulfillment_text)

        # Is this a Default Fall back ?
        elif (df_intent == "Default Fallback Intent"):
            self.intent = 'unidentified_intent'

        # This is an agent defined intent
        else:
            self.intent = df_intent
            self.set_parameters()

    def set_parameters(self):
        # Handle the case where the intent is to talk
        # about STDs.
        if (self.intent == 'STD'):
            names = self.query_result.parameters['std_id']
            params = []
            for name in names:
                params.append(name)
                
        self.params = params
