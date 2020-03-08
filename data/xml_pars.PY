import xmltodict, json
import os, chardet

#path to the folder holding the XML
directory = 'C:\\Users\\Juan\\bootcamp\\projects\\project_2\\data'

#iterate over the XML files in the folder
for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        f = open(filename)
        #chardet.UniversalDetector
        XML_content = f.read()

        #parse the content of each file using xmltodict
        x = xmltodict.parse(XML_content)
        j = json.dumps(x)

        print (filename)

        filename = filename.replace('.xml', '')
        output_file = open(filename + '.json', 'w')
        output_file.write(j)