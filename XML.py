import xml.etree.ElementTree as ET

class XML():           
    def getDetails(self,tag,path):
        tree = ET.parse(path)
        root = tree.getroot()
        nTag = ".//"+tag
        value = root.find(nTag)
        return value.text
    