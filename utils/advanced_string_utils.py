import re
import unicodedata
import random
import string
from typing import List

def remove_accents(text: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def extract_emails(text: str) -> List[str]:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def extract_urls(text: str) -> List[str]:
    pattern = r'https?://[^\s<>"{}|\\^`$$  $$]+'
    return re.findall(pattern, text)

def mask_string(text: str, visible_start: int = 4, visible_end: int = 4, mask_char: str = '*') -> str:
    if len(text) <= visible_start + visible_end:
        return text
    masked_length = len(text) - visible_start - visible_end
    return text[:visible_start] + mask_char * masked_length + text[-visible_end:]

def random_string(length: int = 10, include_digits: bool = True, include_symbols: bool = False) -> str:
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def sanitize_filename(text: str) -> str:
    text = re.sub(r'[^\w\s.-]', '', text)
    text = re.sub(r'\s+', '_', text)
    return text.strip('_.-')

def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

__all__ = [
    'remove_accents',
    'extract_emails',
    'extract_urls',
    'mask_string',
    'random_string',
    'sanitize_filename',
    'levenshtein_distance'
]