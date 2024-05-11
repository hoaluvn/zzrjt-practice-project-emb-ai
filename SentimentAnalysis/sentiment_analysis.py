"""
    Wattson.AI package
"""
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """ Access Watson.AI """
    # pylint: disable=line-too-long
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    # pylint: disable=missing-timeout
    response = requests.post(url, json = myobj, headers=headers)
    myjson = json.loads(response.text)
    if response.status_code == 200:
        label = myjson['documentSentiment']['label']
        score = myjson['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
