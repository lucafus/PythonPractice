import json

languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

json_string = """
{     
    "Input":[
        {
        "Text" : "Im learning code in AWS",
        "SourceLanguageCode" : "n",
        "TargetLanguageCode": "fr"
        }
    ]
 }
 
 """
 
json_input = json.loads(json_string)
 
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is = to the TargetLanguageCode- nothing to do")
    
elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
    print("Error with the language integrations")
elif SourceLanguageCode in languages and TargetLanguageCode in languages:
    print("Correct language integration")

elif SourceLanguageCode not in languages:
    print("The SourceLanguageCode is not valid - stopping")

elif TargetLanguageCode not in languages:
    print("The TargetLanguageCode is not valid - stopping")    

else:
    print("Check each Source and Target individualy")


