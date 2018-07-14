import uuid
from flask import Flask, request, make_response, jsonify
from flo_detect_intent import detect_intent_texts
import dialogflow
import rapidpro_response

app = Flask(__name__)

def get_df_response(message):
  #  agent_id = 'littlesis-a5948'
    agent_id = 'littlesisv2'
    df_response = detect_intent_texts(agent_id, str(uuid.uuid4()),
                  [message], 'en-US')
    return df_response


@app.route('/', methods=['GET'])
def handle_unknown_response():
    """ Handles the unknown user response with DialogFlow
        The response is recieved from RapidPro as a query string
        and passed to DialogFlow as a JSON object.
        @return: either a SmallTalk Response or intent is returned."""

    # Get unexpected user input
    
    unexpected_input = request.args.get('unknown_response')
    print("User input: " + unexpected_input)

    # TODO Handle an empty input in RapidPro
    if unexpected_input is None:
        print("user input is empty")
        return "user input is empty"

    # Pass unexpectd_input to Dialogflow 
    df_response = get_df_response(unexpected_input)
    print(df_response)
    
#    return make_response(jsonify({'text': fulfillment_text, 'intent': intent, 
                      #            'confidence': intent_confidence, 'parameters': parameters}))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
