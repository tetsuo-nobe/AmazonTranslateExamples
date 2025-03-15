import boto3
     
translate = boto3.client('translate')

text_en = "Hi, My name is John Doe!"

# 注意: boto3 のバージョンが古い場合、Settings には Profanity 以外のパラメータがサポートされていない

# INFORMAL
settings_informal = {
  'Formality': 'INFORMAL',
  'Profanity':'MASK'
}

# FORMAL
settings_formal = {
  'Formality': 'FORMAL',
  'Profanity':'MASK'
}

# INFORMAL での翻訳
print("Translating text from English to Japanese with Formality=INFORMAL")
response = translate.translate_text(Text=text_en, SourceLanguageCode="en",TargetLanguageCode="ja",Settings=settings_informal)
print("Translated text: " + response.get('TranslatedText'))
print("--- 下記はレスポンス全体 ---")
print(response)
print("\n")

# FORMAL での翻訳
print("Translating text from English to Japanese with Formality=FORMAL")
response = translate.translate_text(Text=text_en, SourceLanguageCode="en",TargetLanguageCode="ja",Settings=settings_formal)
print("Translated text: " + response.get('TranslatedText'))
print("--- 下記はレスポンス全体 ---")
print(response)
print("\n")
