import boto3
     
translate = boto3.client('translate')

# 翻訳禁止のタグなし
text_en = "<h3>I use Amazon Bedrock.</h3>"
print("Translating text from English to Japanese")
response = translate.translate_text(Text=text_en, SourceLanguageCode="en", TargetLanguageCode="ja")
print("Translated text: " + response.get('TranslatedText'))
print("\n")


# 翻訳禁止のタグあり
text_en_with_tag = "<h3>I use <span translate=\"no\">Amazon Bedrock</span>.</h3>"
print("Translating text from English to Japanese with do-not-translate-tag")
response = translate.translate_text(Text=text_en_with_tag , SourceLanguageCode="en", TargetLanguageCode="ja")
print("Translated text: " + response.get('TranslatedText'))
print("\n")