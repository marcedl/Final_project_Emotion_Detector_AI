import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json = myobj, headers = header)
    formated_response = json.loads(response.text)
    if formated_response ['emotionPredictions'] is not None:
        emotions = formated_response ['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)
        #max_emotion_score = emotions[max_emotion]
        formated_dict_emotions = {
                                'anger': anger,
                                'disgust': disgust,
                                'fear': fear,
                                'joy': joy,
                                'sadness': sadness,
                                'dominant_emotion': max_emotion
                                }
        return formated_dict_emotions