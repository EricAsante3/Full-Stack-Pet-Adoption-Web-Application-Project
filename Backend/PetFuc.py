from flask import Flask, json, request, jsonify


def Get_Random_Pet():
    randomint = "9" # APi generates random interger that represents a PET ID
    # Api accesses database and return information in data base
    #Retrun information such as profile picture on the pet accosiated with the random ID 
    return jsonify({"id": randomint,"name":"sam","sex":"male","Age":"8", "location":"Connecticwut", "Breed": "Pug"}) # Return dog information

