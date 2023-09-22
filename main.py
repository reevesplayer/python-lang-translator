import requests
import ast
from playsound import playsound
from gtts import gTTS

url = "https://nlp-translation.p.rapidapi.com/v1/translate"

translate_from = input("From: ")
translate_to = input("To: ")
text = input("Text: ")

querystring = {
    "text": "text",
    "to":"translate_to",
    "from":"translate_from"
}

headers = {
	"X-RapidAPI-Key": "ff02358607msh00daa86d39ad724p166681jsn6079219a953a",
	"X-RapidAPI-Host": "nlp-translation.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

dict_response = ast.literal_eval(response.text)

traslated_text = dict_response['translated_text']

print(dict_response['translated_text'])
