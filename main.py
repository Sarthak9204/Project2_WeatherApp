import requests
import json
import os
welcome = "Hi User enter your city name"
cmd0 = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{welcome}')"
os.system(cmd0)
city = input("Enter your city name :- ")
url = f"https://api.weatherapi.com/v1/current.json?key=8f73337f5673486680835317232408&q={city}"
ws = requests.get(url)
process = "Processing the weather , wait for a few seconds"
cmd1 = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{process}')"
os.system(cmd1)
print(process)
wdic = json.loads(ws.text)
ans = f'''Current Weather of {city} is {wdic["current"]["temp_c"]} degree Celsius'''
cmd2 = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{ans}')"
os.system(cmd2)
print(ans)

