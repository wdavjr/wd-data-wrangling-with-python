from xml.etree import ElementTree as ET

tree = ET.parse("data-text.xml")
root = tree.getroot()

data = root.find("Data")

all_data = []

for observation in data:
    record = {}
    for item in observation:
        lookup_key = list(item.attrib.keys())[0]  # Retrieve the first attribute key

        if lookup_key == "Numeric":
            rec_key = "NUMERIC"
            rec_value = item.attrib.get("Numeric")
        else:
            rec_key = item.attrib.get(lookup_key)
            rec_value = item.attrib.get("Code")

        record[rec_key] = rec_value

    all_data.append(record)

# Print all_data after processing all observations
print(all_data)
