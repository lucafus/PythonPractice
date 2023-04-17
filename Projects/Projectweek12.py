#Create and populate an empty list with AWS services using append or insert.

list = []
list.append('SQS')
list.append('S3')
list.append('DynamoDB')
list.append('SNS')
list.append('Lambda')

#Print the list and the length of the list.

print('Services', list) 
print('Lenght of the services list:', len (list))

#Remove two specific services from the list by name or by index.

del list[1]
del list[2]

#Print the new list and the new length of the list.

print('New services', list) 
print('Lenght of the new services list:', len (list))

