data = [{'File_name': '0097036e1ec7cb58.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0097036e1ec21c2a.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0097036e1ebdb5dd.mp3',
  'Expected_result': 'Yes',
  'predicted': 'No',
  'Test_Result': 'Fail'},
 {'File_name': '0097036e1ebcd48e.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0097036e1eb0a27a.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0094036ecd651382.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0094036ecd643a33.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0094036ecd6309b7.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0094036ecd58caeb.mp3',
  'Expected_result': 'Yes',
  'predicted': 'Yes',
  'Test_Result': 'Pass'},
 {'File_name': '0094036ecd587f35.mp3',
  'Expected_result': 'Yes',
  'predicted': 'No',
  'Test_Result': 'Fail'},
 ]

'''
count_no = sum(1 for item in data if item['Expected_result'] == item['predicted']== "No")
count_casereason_fail = sum(1 for item in data if item['predicted']== "No")
print(count_no)
print(count_casereason_fail)
'''
import  pandas as pd
file_path = "C:/Users/Admin/Downloads/New folder/abc(1).csv"
a = pd.DataFrame(data)
a.to_csv(file_path, index= False)
print(f"Successfully Report Save To: {file_path}")
