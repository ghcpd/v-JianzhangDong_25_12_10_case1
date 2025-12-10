import xml.etree.ElementTree as ET

def fromstring(s):
    return ET.fromstring(s)

__all__ = ['fromstring']