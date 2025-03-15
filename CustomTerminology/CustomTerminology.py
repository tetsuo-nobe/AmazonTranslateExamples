
import boto3
     
translate = boto3.client('translate')
     
# The terminology file 'CustomTerminology.csv' has the following contents:
'''
en,ja
student,受講者
'''
     
# Read the terminology from a local file
with open('MyCustomTerminology.csv', 'rb') as f:
  data = f.read()
     
file_data = bytearray(data)
     
print("Importing the terminology into Amazon Translate...")
response = translate.import_terminology(Name='my-first-terminology', MergeStrategy='OVERWRITE', TerminologyData={"File": file_data, "Format": 'CSV'})
print("Terminology imported: "),
print(response.get('TerminologyProperties'))
print("\n")
     
print("Getting the imported terminology...")
response = translate.get_terminology(Name='my-first-terminology', TerminologyDataFormat='CSV')
print("Received terminology: "),
print(response.get('TerminologyProperties'))
print("The terminology data file can be downloaded here: " + response.get('TerminologyDataLocation').get('Location'))
print("\n")
     
print("Listing the first 10 terminologies for the account...")
response = translate.list_terminologies(MaxResults=10)
print("Received terminologies: "),
print(response.get('TerminologyPropertiesList'))
print("\n")
     
print("Translating 'student' from English to Japanese with NO terminology...")
response = translate.translate_text(Text="student", SourceLanguageCode="en", TargetLanguageCode="ja")
print("Translated text: " + response.get('TranslatedText'))
print("\n")

print("Translating 'student' from English to Japanese with the 'my-first-terminology' terminology...")
response = translate.translate_text(Text="student", TerminologyNames=["my-first-terminology"], SourceLanguageCode="en", TargetLanguageCode="ja")
print("Translated text: " + response.get('TranslatedText'))
print("\n")

print("Cleaning up by deleting 'my-first-terminology'...")
translate.delete_terminology(Name="my-first-terminology")
print("Terminology deleted.")

'''
en,ja
student,生徒
'''
with open('MyCustomTerminology2.csv', 'rb') as f:
    data = f.read()
     
file_data = bytearray(data)
     
print("Updating the imported terminology in Amazon Translate...")
response = translate.import_terminology(Name='my-first-terminology', MergeStrategy='OVERWRITE', TerminologyData={"File": file_data, "Format": 'CSV'})
print("Terminology updated: "),
print(response.get('TerminologyProperties'))
print("\n")
     
print("Translating 'student' from English to Japanese with NO terminology...")
response = translate.translate_text(Text="student", SourceLanguageCode="en", TargetLanguageCode="ja")
print("Translated text: " + response.get('TranslatedText'))
print("\n")

print("Translating 'student' from Japanese to French with the 'my-first-terminology' terminology...")
response = translate.translate_text(Text="student", TerminologyNames=["my-first-terminology"], SourceLanguageCode="en", TargetLanguageCode="ja")
print("Translated text: " + response.get('TranslatedText'))
print("\n")
     
print("Cleaning up by deleting 'my-first-terminology'...")
translate.delete_terminology(Name="my-first-terminology")
print("Terminology deleted.")