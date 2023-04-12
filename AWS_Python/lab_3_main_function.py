import boto3

client = boto3.client('translate')

def translate_text(text, source_language_code, target_language_code):
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text('I am learning', 'en', 'es')

if __name__=="__main__":
    main()
