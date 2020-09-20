import requests
import json
import pandas as pd
from datetime import datetime, timedelta


payload = "{\n    \"email\": \"youremail\",\n    \"password\": \"yourpassword\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'generate your token'
}

url = ""
urls = [url.format(page) for page in range(1, 10)]
all_data =[]
for url in urls:
    res = requests.request("GET", url, headers=headers, data = payload)
    content = res.content
    jsonobj = json.loads(content) 
    data = jsonobj["data"]
    
    for index,value in enumerate(data):
        dct ={
            "customer_name" : value["customer_name"],
            "customer_phone" : value["customer_phone"],
            "product_name" : value["products"][0]["name"],
            "channel_name" : value["channel_name"],
            "status" : value["status"],
            "delivered_date" : value["shipments"][0]["delivered_date"]
            }
        all_data.append(dct)
df=pd.DataFrame(all_data)
start_date="2020-06-18"
start_date = start_date.strftime("%Y-%m-%d, %H:%M:%S")
end_date = "2020-06-20"
end_date = end_date.strftime("%Y-%m-%d, %H:%M:%S")
df=df[(df["channel_name"]=="AMAZON_IN") & (df["status"]=="DELIVERED") & (df['delivered_date'] > start_date) & (df['delivered_date'] <= end_date) ]
    

