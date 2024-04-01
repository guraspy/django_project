from django.contrib.auth.hashers import check_password

hashed_password = 'pbkdf2_sha256$720000$NHSDBjcGIODpEwJsder2TK$bcc0U30wLMD+PLci2DISQr+qyYS1oGUd2f4Xls98W20='
password_to_check = 'password123'

# Check if the password matches the hash
result = check_password(password_to_check, hashed_password)

if result:
    print("Password matches!")
else:
    print("Password does not match.")