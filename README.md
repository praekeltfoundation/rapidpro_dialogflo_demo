# RapidPro Dialogflow Demo
## Exploring Dialogflow as an NLU component to a RapidPro chatbot flow.

### This was an internship project by Emer Butler

**Aim:** A proof of concept for Dialogflow as a suitable and simple NLP component
to Messenger, Whatsapp, Viber or Telegram bots. 

**Outcome:** I built a simple Flask app `response_handler.py` to function as a webhook. A RapidPro flow calls the webhook, passing the text of an unknown response along as a query parameter. The Flask app routes the text to DialogFlow, which does intent detection and parameter extraction. The response from Dialogflow is then returned to the RapidPro flow.

You can read more about this project [here](https://paper.dropbox.com/doc/Glue-and-how-to-use-it--AHbMrNIpIxvq7TLF01UEgE2~AQ-5dlXKLzNJEpAVZjCDi6lT).

**Additional Feature:** As showcased in the RapidPro flow [demo/definitions](url_for_definition_flow_here), I have also explored storing bot responses in Google Sheets. In large scale use, this will pose performance issues and a more suitable, traditional database solution should be investigated. However, the idea I was trying to showcase is how easy we can make it for non-technical staff to add to the chatbots knowledge base.

## Prerequisites 
### Software
The following software should be installed before attempting installation:
* `python3`
* `pip`
* `pipenv` (can be installed with `sudo pip install pipenv`)

### Credentials
We need access to two sets of credentials to make this application work nice and smoothly:
1) Service account file to access the Dialogflow API
2) Service account file to access the Google Sheets / Google Drive API

Firstly, we will acquire the service account file for the Dialogflow API. First, open your newly created Agent in the Dialogflow Console and take a note of the Google Project ID.

## Installation
Start by cloning the repository and installing the dependencies.

```bash
# Clone the repository
$ git clone https://github.com/praekeltfoundation/rapidpro_dialogflow_demo.git

# Move into the cloned repository
$ cd rapidpro_dialogflow_demo

# Install dependencies using pipenv
$ pipenv install
```

Now activate the virtual environment, and start the Flask app:

```bash
# Activate the virtual environment
$ pipenv shell

# Run the Flask app (using the built-in development server)
$ python response_handler.py
```

## Docker 
If you need to run this application inside a Docker container, a `Dockerfile` has been provided. Needless to say, Docker must be installed (more information can be found in the [documentation](/link_to_docker_install_docs))

```bash
# Make sure you are in the root of the 
# repository before running this command!
$ docker image build . -t littlesis
```

This will build the Docker image, and we can now run it using the following incantation:

```bash
# Forward web traffic on our port 8080 to Flask application
# listening on port 8080 in the container.
$ docker run -it -p 8080:8080 littlesis
```

