import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

data= "On 28 July 1920, Jorabagan was scheduled to play against Mohun Bagan in the Coochbehar Cup. Jorabagan sent out their starting eleven but with the notable exclusion of defender Sailesh Bose, who was dropped from the squad for undisclosed reasons. The then vice-president of Jorabagan, Suresh Chandra Chaudhuri, asked in vain for Bose to be included in the line-up. When his request was not welcomed, Chaudhuri left the club along with Raja Manmatha Nath Chaudhuri, Ramesh Chandra Sen, and Aurobinda Ghosh. They formed East Bengal as a Sports and Cultural Association in the neighbourhood of Jorabagan on 1 August 1920."

minL=20
maxL=50

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
    "inputs":data,
    "parameters":{"min_length":minL, "max_length":maxL},
})


print(output)