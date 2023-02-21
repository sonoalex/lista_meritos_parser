
import PyPDF2
import re
import pprint

# Creating a pdf file object
pdfFileObj = open('llista-provisional-merits-cos-especialitat.pdf','rb')

# Creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Getting number of pages in pdf file
pages = pdfReader.pages

id_regex = re.compile(r'\*\*\*\d+\*\*')
r = re.compile(r"\d+\,\d+")
regex_name = r"\b[^\d\W]+\b"

result = []

# Loop for reading all the Pages
for page in pages:

        # Creating a page object

        # Printing Page Number
        text = page.extract_text()
        if  not re.findall('Francès', text):
            continue
        
        split_text = page.extract_text().split("\n")

        i = 0
        for item in split_text:
            #print(item)
            match = id_regex.search(item)
            
            if match:
                #print('punts: ', split_text[i+2].split())
                name = " ".join(re.findall(regex_name, split_text[i]))
                points = r.search(split_text[i])[0]
                #match_2 = r.search(name)
                

                result.append(
                    {
                        'name':name,
                        'points':float(points.replace(',', '.'))
                    }
                )
            i = i+1


sorted_result = sorted(result, key=lambda d: d['points'], reverse=True) 
print(sorted_result)

# closing the pdf file object
pdfFileObj.close()