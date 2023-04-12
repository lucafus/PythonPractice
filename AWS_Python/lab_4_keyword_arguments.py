import boto3

def translate_text(**kwargs):
    client = boto3.client("translate")
    response = client.translate_text(**kwargs)
    print(response)
    

kwargs = {'Text':"Reducing my code length", 'SourceLanguageCode': 'en', 'TargetLanguageCode': 'fr'}

def main():
    translate_text(**kwargs)
    
if __name__ == "__main__":
    main()
