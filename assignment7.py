import re

text = """
Contact us at john.doe@gmail.com or support@example.com.
You can also email admin123@yahoo.co.in for more information.
"""

# Regular expression pattern for email addresses
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the results
print("Email addresses found:")
for email in emails:
    print(email)