import re
import unicodedata

def to_snake_case(text: str) -> str:
    text = re.sub(r'([A-Z]+)', r'_\1', text)
    text = re.sub(r'[\s-]+', '_', text)
    text = text.strip('_').lower()
    return text

def to_camel_case(text: str) -> str:
    parts = text.replace('-', ' ').replace('_', ' ').split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

def to_pascal_case(text: str) -> str:
    return ''.join(word.capitalize() for word in text.replace('-', ' ').replace('_', ' ').split())

def slugify(text: str, separator: str = '-') -> str:
    text = str(text).strip()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s]+', separator, text)
    return text.strip(separator)

def truncate(text: str, max_length: int, suffix: str = '...') -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def capitalize_words(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())

def reverse(text: str) -> str:
    return text[::-1]

__all__ = [
    'to_snake_case',
    'to_camel_case',
    'to_pascal_case',
    'slugify',
    'truncate',
    'capitalize_words',
    'reverse'
]