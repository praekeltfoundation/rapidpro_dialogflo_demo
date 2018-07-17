import uuid
from flask import Flask, request, make_response, jsonify
from flo_detect_intent import detect_intent_texts
import rp_json

app = Flask(__name__)


def get_df_response(message):
    """ Connect to the Dialogflow agent and get the agent's response """
    agent_id = 'littlesisv3'
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

    # TODO Handle an empty input in RapidPro
    if unexpected_input is None:
        print("user input is empty")
        return "user input is empty"
    
    print("User input: " + unexpected_input)

    # Pass unexpectd_input to Dialogflow 
    df_response = get_df_response(unexpected_input)
    print(df_response)

    rp_response = rp_json.RP_JSON(df_response)

    print(rp_response)

    return make_response(jsonify({'intent': rp_response.intent, 
                                  'fulfillment': rp_response.fulfillment_text,
                                  'parameters': rp_response.parameters,
                                  'user_query': rp_response.query_text}))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
