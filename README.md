# rapidpro_dialogflow_demo
Exploring Dialogflow as an NLU component to a RapidPro chatbot flow.

**This was an internship project by Emer Butler**

**Aim:** A proof of concept for Dialogflow as a suitable and simple NLP component
to Messenger, Whatsapp, Viber or Telegram bots. 

**Outcome:** I built a simple flask app `glue.py` to function as a webhook. A
RapidPro flow calls the webhook, passing the text of an unknown response. 

`glue.py` passes this message to a Dialogflow agent. The agent identifies the intent of the incoming message and returns a json object detailing the intent, entities and (where applicable) a suitable response.

You can read more about this project [here](https://paper.dropbox.com/doc/Glue-and-how-to-use-it--AHbMrNIpIxvq7TLF01UEgE2~AQ-5dlXKLzNJEpAVZjCDi6lT).

**Additional Feature:** I have also explored storing bot responses in Google Sheets and written a python script to fetch information from Google Sheets to be sent back as responses from the bot. In large scale use, however, this might pose performance issues and some sort of sql database might be better.   

## Installation



## Working instance

