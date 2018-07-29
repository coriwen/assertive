import time
import json
import requests
import numpy as np
import pandas as pd
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
   username='9950b10e-9b5c-43e3-8e59-9f6850c4fd80',
   password='6X0dExNNFiuj',
   url='https://gateway.watsonplatform.net/tone-analyzer/api',
   version='2016-05-19')

emotion = []
score = []

def analyzeTone(text1):
  json_output = tone_analyzer.tone(text1, content_type='text/plain')
  for i in json_output['document_tone']['tone_categories']:
      for j in i['tones']:
            if j['score'] > 0.5:
                print (j['tone_name'], j['score']) 
                emotion.append(j['tone_name'])
                score.append(j['score'])

  df = pd.DataFrame({"Tones":emotion, "Score":score})
  df.set_index('Tones', inplace=True)
  df['Score'] = df['Score'].apply(lambda x: x*100)
  df = df.round(2)
  df = df.nlargest(4, 'Score')
  #series = df[df.columns[0]]
  #dic = series.to_dict()
  #json_output = json.dumps(dic)
  #return json_output
  scores1 = df.Score.tolist()
  tones1 = df.index.tolist()

  return scores1, tones1

