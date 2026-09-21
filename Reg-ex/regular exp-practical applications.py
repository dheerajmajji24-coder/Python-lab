#week-6
#task-5
#1
import re
def is_valid_email(s):
    pattern = r'^[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'
    return bool(re.fullmatch(pattern, s))
# Valid examples
valid_emails = [
    "user@example.com",
    "john.doe@gmail.com",
    "a@b.co",
    "student_123@college.edu"
]
# Invalid examples
invalid_emails = [
    "no-at-sign.com",
    "user@example",
    "@example.com",
    "user@.com"
]
print("Valid emails:")
for email in valid_emails:
    print(email, "->", is_valid_email(email))
print("\nInvalid emails:")
for email in invalid_emails:
    print(email, "->", is_valid_email(email))


#output
#Valid emails:
#user@example.com -> True
#john.doe@gmail.com -> True
#a@b.co -> True
#student_123@college.edu -> True

#Invalid emails:
#no-at-sign.com -> False
#user@example -> False
#@example.com -> False
#user@.com -> False


#2
import re
text = """
Call 555-123-4567 or (555) 987-6543.
You can also reach us at 555.222.3333.
Another number is 555-444-5555.
"""
# Pattern for -, ., or parentheses formats
pattern = r'(?:\(\d{3}\)|\d{3})[-.\s]\d{3}[-.]\d{4}'
phone_numbers = re.findall(pattern, text)
print("Original phone numbers:")
for phone in phone_numbers:
    print(phone)
print("\nNormalized phone numbers:")
for phone in phone_numbers:
    # Remove parentheses, spaces, dots, and hyphens
    normalized = re.sub(r'[\s().-]', '', phone)
    # Convert to 555-123-4567 format
    normalized = re.sub(
        r'(\d{3})(\d{3})(\d{4})',
        r'\1-\2-\3',
        normalized
    )
    print(normalized)

#output
#Original phone numbers:
#555-123-4567
#(555) 987-6543
#555.222.3333
#555-444-5555

#Normalized phone numbers:
#555-123-4567
#555-987-6543
#555-222-3333
#555-444-5555



#3
import re
text = """
Important dates are 15/08/2024, 01/01/2025,
and 25/12/2025.
"""
# Extract dates using groups
pattern = r'(\d{2})/(\d{2})/(\d{4})'
dates = re.findall(pattern, text)
print("Extracted dates:")
for date in dates:
    print(date)
# Convert DD/MM/YYYY to YYYY-MM-DD
new_text = re.sub(pattern, r'\3-\2-\1', text)
print("\nReformatted text:")
print(new_text)


#output
#Extracted dates:
#('15', '08', '2024')
#('01', '01', '2025')
#('25', '12', '2025')
#Reformatted text:
#Important dates are 2024-08-15, 2025-01-01,
#and 2025-12-25.




#4
import re
def clean_text(html):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html)

    # Collapse spaces, tabs, and newlines
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing spaces
    return text.strip()
html = """
<p>Hello <b>world</b>!</p>
<div>This   is a    test.</div>
<p>Python\t\tis\nawesome.</p>
"""
result = clean_text(html)
print(result)

#output
#Hello world! This is a test. Python is awesome.





#5
import re
def check_password(pw):
    failed_rules = []
    # Rule 1: At least 8 characters
    if len(pw) < 8:
        failed_rules.append("Password must be at least 8 characters long.")
    # Rule 2: At least one uppercase letter
    if not re.search(r'[A-Z]', pw):
        failed_rules.append("Password must contain at least one uppercase letter.")
    # Rule 3: At least one lowercase letter
    if not re.search(r'[a-z]', pw):
        failed_rules.append("Password must contain at least one lowercase letter.")
    # Rule 4: At least one digit
    if not re.search(r'\d', pw):
        failed_rules.append("Password must contain at least one digit.")
    # Rule 5: At least one allowed symbol
    if not re.search(r'[!@#$%^&*]', pw):
        failed_rules.append("Password must contain at least one symbol from !@#$%^&*.")
    return failed_rules

# Test passwords
passwords = [
    "Strong@123",
    "weak",
    "abcdefgh",
    "ABCDEFGH",
    "Abcdefgh",
    "Abcdefg1"
]
for password in passwords:
    print("Password:", password)
    failures = check_password(password)
    if not failures:
        print("Result: Strong password")
    else:
        print("Failed rules:")
        for rule in failures:
            print("-", rule)
    print()

#output
#Password: Strong@123
#Result: Strong password
#Password: weak
#Failed rules:
#- Password must be at least 8 characters long.
#- Password must contain at least one uppercase letter.
#- Password must contain at least one digit.
#- Password must contain at least one symbol from !@#$%^&*.

#Password: abcdefgh
#Failed rules:
#- Password must contain at least one uppercase letter.
#- Password must contain at least one digit.
#- Password must contain at least one symbol from !@#$%^&*.

#Password: ABCDEFGH
#Failed rules:
#- Password must contain at least one lowercase letter.
#- Password must contain at least one digit.
#- Password must contain at least one symbol from !@#$%^&*.

#Password: Abcdefgh
#Failed rules:
#- Password must contain at least one digit.
#- Password must contain at least one symbol from !@#$%^&*.

#Password: Abcdefg1
#Failed rules:
#- Password must contain at least one symbol from !@#$%^&*.


