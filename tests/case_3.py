from app.visualizer import plot_histogram
import xml.etree.ElementTree as ET

# Test matplotlib functionality
plt = plot_histogram([1, 2, 3, 4, 5], title="Test Plot")
plt.savefig("plot.png")

# Test XML parsing
xml_content = "<root><item>123</item></root>"
root = ET.fromstring(xml_content)
print("XML Parsed:", root[0].text)
