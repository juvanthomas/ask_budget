from flask import Flask, request
import requests
import re
import subprocess

# ~ logic of the program starts here

app = Flask(__name__)


@app.route("/")
def hello():

    return "##########      Welcome to  Ask Budget 3.0!    ###############"

@app.route("/commit",methods=['POST'])
def commit():
    
    subprocess.run(["git","pull"])

    return Response(status=200)


@app.route("/ask", methods=['POST'])
def sms_reply():
    msg = request.json["text"]  # postman
    query = str(msg)
    try:
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
                        
                        
                    else:            
                        entity_value.append(entity['value'])
                        entity_name_list.append(entity['name'])
                        keyword=entity['value']
                        temp_result[entity['name']]=entity['value']
                        
        response =temp_result

    except:

        response = "nothing"

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)
