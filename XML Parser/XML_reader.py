import xml.etree.ElementTree as ET

tree = ET.parse("output.xml")   
root = tree.getroot()            # root element
print(root.tag)

record = len(root.findall("book"))
print("Total records:", record)

unique_author = set()
unique_title = set()
List = []
Dict = {}

for book in root.findall("book"):
    title = book.find("title")
    if title is not None:
        Title = title.text
        unique_title.add(Title.strip())

    authors_block = book.find("authors")
    if authors_block is not None:
        for a in authors_block.findall("author"):
            if a.text:
                unique_author.add(a.text.strip())
   
    issued = book.find("issued").text
    if issued is not None:
        List.append(issued)

print("Total unique authors:", len(unique_author))
print("Total unique titles:", len(unique_title))

print("-"*80)
print("AUTHOR NAME")
for i,item in enumerate(unique_author):
    print(i,item)
    
print("-"*80)
print("TITLE NAME")
for i,item in enumerate(unique_title):
    print(i,item)

print("-"*80)
for item in List:
    print("Issued on:", item)
