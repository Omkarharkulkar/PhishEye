# email_parser.py - Parses the email content for analysis
import re

def extract_email_features(email_content):
    # Extract basic features from the email content
    features = {
        'has_links': bool(re.search(r'http[s]?://', email_content)),
        'num_links': len(re.findall(r'http[s]?://', email_content)),
        'num_images': len(re.findall(r'<img', email_content)),
        'has_attachments': 'attachment' in email_content.lower(),
        'num_words': len(email_content.split()),
    }
    return features
