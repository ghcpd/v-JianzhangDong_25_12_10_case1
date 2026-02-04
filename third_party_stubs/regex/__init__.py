import re

# Minimal compatibility wrapper
match = re.match
search = re.search
findall = re.findall
sub = re.sub

__all__ = ['match', 'search', 'findall', 'sub']