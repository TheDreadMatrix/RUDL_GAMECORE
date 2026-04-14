import json
import xml.etree.ElementTree as ET


class Joshua:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def readData(self):
        data = None
        with open(self.json_path, "r") as f:
            data = json.load(f)

        return data 
    
    def saveData(self, data: dict):
        with open(self.json_path, "w") as f:
            json.dump(data, f, indent=4)


    def __repr__(self):
        return f"<Joshua: {self.json_path}>"
            





class Xmlion:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path

        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def readXML(self) -> dict:
        def _to_dict(element):
            data = {}

            
            if element.attrib:
                data["@attributes"] = element.attrib

            for child in element:
                if len(child):
                    data[child.tag] = _to_dict(child)
                else:
                    data[child.tag] = child.text

            return data

        return _to_dict(self.root)
    
    def saveXML(self, data: dict):
        def _build(element, data_dict):
            for key, value in data_dict.items():
                if key == "@attributes":
                    for attr, val in value.items():
                        element.set(attr, str(val))
                    continue

                child = ET.SubElement(element, key)

                if isinstance(value, dict):
                    _build(child, value)
                else:
                    child.text = str(value)

        self.root.clear()

        _build(self.root, data)

        self.tree.write(self.xml_path)