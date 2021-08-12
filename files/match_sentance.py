from flask import Flask, request, jsonify
import requests
import json
from fuzzywuzzy import fuzz
from pandas import json_normalize
import re

msg = "Which are the top 3 departments with maximum budget"
k= "#"
msg_striped = re.sub(r'\d', k, msg)
print(msg_striped)


query = str(msg)

API = 'https://api.wit.ai/message?v=20210806&q='

URL = API + query

head = {"Authorization": 'Bearer JG6DLERPGOUL3OTATUE7XZY47D7S73IS'}

r = requests.get(url=URL, headers=head)
print(r.json())
k =r.json()


if k['intents'] ==[]:
    keyword = "unknown"
    print("k = ",keyword)


elif k['intents'][0]['name'] == 'budget_analytics':      
    
    entity_value = []
    entity_name_list = []
    temp_result = {}    
    entity_list = r.json()['entities']
    # For saving names and values
    for i in entity_list:
        
        all_entities = r.json()['entities'][i]
        for entity in all_entities:
            
            if entity['name']=="sorting2":
                temp_result[entity['name']]=entity['role']
                limit_body = entity['body']
                limit=re.findall(r'\d+', limit_body)
                temp_result['limit']=limit[0]
            elif entity['name']=="measure":
                entity_value.append(entity['value'])
                entity_name_list.append(entity['name'])
                keyword=entity['value']
                temp_result[entity['name']]=entity['value']
                if entity['role']=="utilization_calculation":
                    temp_result['calculation']='percentage'
                
            else:            
                entity_value.append(entity['value'])
                entity_name_list.append(entity['name'])
                keyword=entity['value']
                temp_result[entity['name']]=entity['value']
        
        result =temp_result
        if "calculation" in result.keys():
            pass
        else:
            result['calculation']="sum"
        
        if  "measure" in result.keys():
            if result['measure'] in ['lessthan_100','greaterthan_100']:
                result['filter']=result['measure']
                result['measure1']='actual_amount'
                result['measure2']='budget_amount'
                del result['measure']
            else:
                result['measure1']='actual_amount'
                result['measure2']='budget_amount'
                del result['measure']
        if "dimension" in result.keys():
            pass
        else:
            if "measure1" in result.keys():
                
                result['dimension']=result['measure1']
    print('#####################')        
    print(result)