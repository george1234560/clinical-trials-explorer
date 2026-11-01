import requests
import json

def download_trials(condition_name):
    studies =[]
    token = None
    while True:
        response = requests.get("https://clinicaltrials.gov/api/v2/studies", params={"pageSize" :1000,"countTotal" : "true","query.cond" : condition_name,"pageToken" : token})
        data = response.json()
        studies.extend(data["studies"])
        token = data.get("nextPageToken")
        if token == None:
            break
    
    print(len(studies))
    create_file(condition_name,studies)
    return studies

def create_file(condition_name,studies):
    file_name = f"{condition_name}.json"
    with open(f"../data/raw/{file_name}","w") as f:
        json.dump(studies,f)