import requests
import json

def emotion_detector(text_to_analyse):
      url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
      header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
      myobj= { "raw_document": { "text": text_to_analyse } }
      response = requests.post(url, json = myobj, headers=header)
      #formatted_response = json.loads(response.text)
      #emotion = formatted_response['emotionPredictions']['emotion']
      #return {'emotion': emotion}
      formatted_response = response.json()
      predictions = formatted_response['emotionPredictions']
      first_prediction = predictions[0]
      emotion = first_prediction['emotion']
      emotions = {
        'anger': emotion.get('anger', 0),
        'disgust': emotion.get('disgust', 0),
        'fear': emotion.get('fear', 0),
        'joy': emotion.get('joy', 0),
        'sadness': emotion.get('sadness', 0)
        }
    
       # Find the dominant emotion
      dominant_emotion = max(emotions, key=emotions.get)
    
      return {
                'dominant_emotion': dominant_emotion,
                'dominant_score': emotions[dominant_emotion],
                'all_emotions': emotions
            }

#first run this command in terminal
#python3.11
#from  emotion_detection import emotion_detector
#emotion_detector("i am feeling good")

#from Emotion_Detection.emotion_detection import emotion_detector
#>>> emotion_detector("i am feeling good")


