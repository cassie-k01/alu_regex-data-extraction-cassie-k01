import re

# Sample text 
text = """<<Let Desy_Adventures make your vacation dreams come true!!>>
Contact: desy_r0cks@gmail.com or visit https://www.desy_adventures.com.
"Call me at +1(123) 456-7891  or (123) 456-7890 or 123.456.7890"
Card: 1234-5678-9012-3456 or 1234 5678 9012 3456.
Follow us at #FunLife and #100DaysOfVibes!
"""

# Email regex
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# URL regex
url_pattern = r'https?://[^\s]+'

# Phone number regex

phone_pattern = r'(\+?\d{1,4}[\s\-\.]?)?(\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4})'

# Credit card regex
card_pattern = r'(\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4})'

# Hashtag regex
hashtag_pattern = r'#\w+'

# Extract data
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
matches = re.findall(phone_pattern, text)
phones = ["".join(m) for m in matches]
cards = re.findall(card_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

# Print results
print(" Emails:", emails)
print("URLs:", urls)
print(" Phone Numbers:", phones)
print(" Credit Cards:", cards)
print(" Hashtags:", hashtags)