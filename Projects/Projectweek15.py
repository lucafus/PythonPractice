from datetime import datetime
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('The actual time and date when this SQS queue was created was: ' + time)