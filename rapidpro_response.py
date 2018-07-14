import dialogflow
from flo_detect_intent import detect_intent_texts


class rp_response:
    """A JSON object detailing how RapidPro should respond"""

    def __init__(self, df_response):
        """Initialise a new NLU_response with correct fields"""

        # TODO handle empty df_response
        
        # Initalize the object
        self.query_result = df_response.query_result
        self.parameters = ""
        self.fulfillment_text = ""

        self.set_intent()

        print(self.intent)
        print(self.parameters)
        print(self.fulfillment_text)

    def set_intent(self):

        intent = self.query_result.intent.display_name
        action = self.query_result.action

        
        # Is this Small Talk?
        if (intent.startswith("smalltalk")):
            intents = intent.split(".")
            if (intents[1] == 'confirmation'):
                if (intents[2] == 'yes'):
                    self.intent = 'yes'
                else:
                    self.intent = 'no'
            else:
                self.intent = 'smalltalk' 
                self.parameters = ""
        # Is this a Default Fall back ?
        elif (intent == "Default Fallback Intent"):
            self.intent = 'unidentified_intent'
            self.parameters = ""
        # This is an agent defined intent
        else:
            self.intent = intent
            self.set_parameters(intent)

    def set_parameters(self, intent):

        # Handle the case where the intent is to talk
        # about STDs.
        if intent == 'STD':
            names = self.query_result.parameters['std_id']
            params = []
            for name in names:
                params.append(name)

            self.params = params