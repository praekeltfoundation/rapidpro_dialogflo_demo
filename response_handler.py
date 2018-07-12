import uuid
from flask import Flask, request, make_response, jsonify
from app.flo_detect_intent import detect_intent_texts
import dialogflow

app = Flask(__name__)


def debug_print(symbol, message):
    print(symbol * 20)
    print(message)
    print(symbol * 20)


@app.route('/', methods=['GET'])
def handle_unknown_response():
    """ Handles the unknown user response with DialogFlow
        The response is recieved from RapidPro as a query string
        and passed to DialogFlow as a JSON object.
        @return: either a SmallTalk Response or intent is returned."""
    
    agent_id = 'littlesis-a5948'

    # Get response
    user_response = request.args.get('unknown_response')

    # Handle an empty response
    if user_response is None:
        print("No unknown_response provided")
        return "No unknown_response provided"

    # Get response from DialogFlow
    ai_response = detect_intent_texts(agent_id, str(uuid.uuid4()),
                  [user_response], 'en-US')
    
    # Extract parameter values
    fulfillment_text = ai_response.query_result.fulfillment_text
    action = ai_response.query_result.action
    parameters = []

    if ((ai_response.query_result.action).startswith('smalltalk')):
        intent = "SmallTalk"
    elif ((ai_response.query_result.action).startswith('input')):
        intent = ai_response.query_result.intent.display_name
    else:
        intent = ai_response.query_result.intent.display_name
        for p in ai_response.query_result.parameters[intent]:
            parameters.append(p)
    
    intent_confidence = ai_response.query_result.intent_detection_confidence
    
    # Store the paramater list as a string
    parameter_list = (",".join([str(x) for x in parameters]))

    ## DEBUG: Print parameter values 
    print("=" * 20)
    print("Query Text: " + ai_response.query_result.query_text)
    print("Intent: " + intent)
    print("Confidence: " + str(intent_confidence))
    print("Parameters:" + str(parameters))
    print("Fulfillment text: " + fulfillment_text)
    print("=" * 20)

    # Return AI response
    return make_response(jsonify({'text': fulfillment_text, 'intent': intent,
                                  'confidence': intent_confidence, 'parameters': parameters}))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
