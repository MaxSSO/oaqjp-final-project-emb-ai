import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return None
        
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=body, headers=headers)
    json_response = json.loads(response.text)

    emotion = json_response['emotionPredictions'][0]['emotion']
    max_score = 0
    dominant_emotion = 'none'

    for k in emotion.keys():
        emotion_score = emotion[k]
        if emotion_score > max_score:
            dominant_emotion = k
            max_score = emotion_score

    emotion['dominant_emotion'] = dominant_emotion

    return emotion
