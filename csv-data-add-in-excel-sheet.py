input1 = '''Timestamp,Email,Full Name,Student ID,Algorithm,Algorithm Lab,Functional Bangla,Engineering Drawing,EEE-203,EEE-204
2023-05-31 10:00:00,johndoe@example.com,John Doe,123456,Section A,Section B,Section C,Section D,Section E,Section F
2023-05-31 10:05:00,janesmith@example.com,Jane Smith,654321,Section B,Section C,Section D,Section E,Section F,Section G
2023-05-31 10:10:00,alicejohnson@example.com,Alice Johnson,987654,Section C,Section D,Section E,Section F,Section G,Section H
2023-05-31 10:15:00,bobanderson@example.com,Bob Anderson,456789,Section D,Section E,Section F,Section G,Section H,Section I
'''

input2 = '''Name,Email,Full Name,Student ID,Section,Course,Phone,Social Media Link,Messenger Group Link
John Doe,johndoe@example.com,John Doe,123456,Section A,Algorithm,1234567890,https://www.facebook.com/johndoe,https://m.me/messenger_group_link_1
Jane Smith,janesmith@example.com,Jane Smith,654321,Section B,Algorithm Lab,9876543210,https://www.facebook.com/janesmith,https://m.me/messenger_group_link_2
Alice Johnson,alicejohnson@example.com,Alice Johnson,987654,Section C,Functional Bangla,5555555555,https://www.facebook.com/alicejohnson,https://m.me/messenger_group_link_3
Bob Anderson,bobanderson@example.com,Bob Anderson,456789,Section D,Engineering Drawing,1111111111,https://www.facebook.com/bobanderson,https://m.me/messenger_group_link_4

'''

# Save input1 as A.csv
with open('A.csv', 'w') as file:
    file.write(input1)

# Save input2 as B.csv
with open('B.csv', 'w') as file:
    file.write(input2)

print("CSV files created successfully.")
