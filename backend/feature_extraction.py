# feature_extraction.py - Feature extraction for URLs
from urllib.parse import urlparse

def extract_url_features(url):
    parsed_url = urlparse(url)
    features = {
        'url_length': len(url),
        'has_ip': bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)),
        'has_at_symbol': '@' in url,
        'num_subdomains': len(parsed_url.netloc.split('.')) - 2,
        'path_length': len(parsed_url.path),
    }
    return features
