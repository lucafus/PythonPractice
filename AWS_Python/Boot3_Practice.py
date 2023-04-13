import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='Im translating this text to french',
        SourceLanguageCode= 'en',
        TargetLanguageCode= 'fr'
        )
        
    print(response)
    
translate_text()