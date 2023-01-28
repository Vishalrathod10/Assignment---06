import json
dict_data = {
    "karnataka" : "Banglore",
    "telangana" : "Hyderabad",
    "maharashtra" : "Mumbai",
    "rajastan" : "Jaipur",
    "jharkhand" : "Ranchi",
    "west bengal" : "Kolkata",
    "panjab" : "chandigarh"
}

file1 = open("C:\\New folder\\PYTHON\\Assignments\\Assignment_06\\_2_states.json","w")
json.dump(dict_data,file1)


