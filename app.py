from __future__ import print_function
import json
import logging
import sys
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

response_tmpl = {
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "",
    },
    "shouldEndSession": True
  }
}


def hello_world(name=None)::
    next_train_response = response_tmpl
    text_response = "The next train from {} to {} is soon".format(fr, to)
    next_train_response['response']['outputSpeech']['text'] = text_response
    return next_train_response

def lambda_handler (event, context):
    logger.info('got event{}'.format(event))
    if event['request']['type'] == "IntentRequest":
        if event['request']['intent']['name'] == "HelloWorld":
			if event['request']['intent']['slots']['Name']['value'] != None:
				return hello_world(event['request']['intent']['slots']['Name']['value'])
			else:
			    return hello_world()
        elif event['request']['type'] == "SessionEndedRequest":
        resp = response_tmpl
        return resp
    else:
        resp = response_tmpl
        response_tmpl["shouldEndSession"] = False
        return response_tmpl

