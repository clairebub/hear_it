import freesound, sys,os

#client_id="OlKsdVwj3ujtrh4CV28c"
api_key="vCDuQcIUiKMqZGYsrsKEaGveWz84kgyp0GOW7n50"

client = freesound.FreesoundClient()
client.set_token(api_key,"token")

results = client.text_search(query="dubstep",fields="id,name,previews")

for sound in results:
    sound.retrieve_preview(".",sound.name+".mp3")
    print(sound.name)
