# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 01:10:32 2019

@author: dusti_000
"""

import base64
import json
import os
import ssl

import http.client as httplib  # Python 3

#CONVERT 
headers = {"Content-type": "application/json",
           "X-Access-Token": "thvESYNGod6s3d6NXXzkkPQ2fwpVhCzVFdNA"}
conn = httplib.HTTPSConnection("dev.sighthoundapi.com", 
       context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

# To use a hosted image uncomment the following line and update the URL
#image_data = "http://example.com/path/to/hosted/image.jpg"
# To use a local file uncomment the following line and update the path
allList = []
imgDirectory = r'./car_photos/'
def readImage(imageLink, connection):
    count = 0
    carListFinal = []
    image_data = base64.b64encode(open(imageLink, "rb").read()).decode()
    conn = connection
    params = json.dumps({"image": image_data})
    conn.request("POST", "/v1/recognition?objectType=vehicle,licenseplate", params, headers)
    response = conn.getresponse()
    result = response.read()
    #print("Detection Results = " + str(result))

    my_bytes_value = result
    # Decode UTF-8 bytes to Unicode, and convert single quotes 
    # to double quotes to make it valid JSON
    my_json = my_bytes_value.decode('utf8').replace("'", '"')
    #print(my_json)
    #print('- ' * 20)


    # Load the JSON to a Python list & dump it back out as formatted JSON
    data = json.loads(my_json)
    s = json.dumps(data, indent=3, sort_keys=True)
    json_data = data["objects"] # your list with json objects (dicts)

    """
    print(s)
    
    print("YOOOOOOOOOOOOOOOOOOO " + str(len(json_data)))
    print("OHHHHHHHHHHHHHHHHHHH " + str(json_data[0]))
    print("TYPEEEEEEEEEEEEEEEEE " + str(type(json_data[0])))
    print("GETTTTTTTTTTTTTTTTTT " + str(json_data[0].get("objectId")))
    print("KEYYYYYYYYYYYYYYYYYY " + str(json_data[0].keys()))
    print("KEYYYYYYYYYYYYYYYYY2 " + str(   (json_data[0].get("vehicleAnnotation")).keys() ))
    """
    while count < len(json_data):
        carList = []
        try:
            car_name = json_data[count]["vehicleAnnotation"]["attributes"]["system"]["make"]["name"]
        except:
            car_name = "Unidentify Car Name"
        try:
            car_model = json_data[count]["vehicleAnnotation"]["attributes"]["system"]["model"]["name"]
        except:
            car_model = "Unidentify Car Model"
        try:
            car_plate = json_data[count]["vehicleAnnotation"]["licenseplate"]["attributes"]["system"]["string"]["name"]
        except:
            car_plate = "Unidentify Car Plate"
        
        
        


        carList.extend((car_name, car_model, car_plate))
        allList.append(carList)

        print("List: " + str(count) + str(carList))
        print("List: " + str(count) + str(allList))
        count = count + 1


    
    


            
        #print (item["vehicleAnnotation"]["attributes"]["system"]["make"]["name"])
    print('- ' * 20)
    #print(allList)

#link = "./car_photos/aa.jpg"
#readImage(link, conn)


def execute(directory):
    links = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            links.append(os.path.join(directory, filename))
            
        else:
            continue
    print(links)
    for link in links:
        readImage(link, conn)
        
    print("FINAL RESULT: " + str(allList))
execute(imgDirectory)
