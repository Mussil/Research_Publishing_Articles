# This file takes a source file and creates a destination file after filtering by:
# All records that are just 'article', 'inproceedings',' proceedings.
# And if it's an article then only if there is a label journals



# import xml.etree.cElementTree as etree
import lxml.etree as etree

allTags=['article','inproceedings','proceedings','book','incollection', 'phdthesis', 'mastersthesis','www',]
unwantedTags=['book','incollection', 'phdthesis', 'mastersthesis','www']
path = '../'
source_xml = path + 'originalData/' + 'dblp.xml'
dest_xml=path+'modifiedData/'+'filteredDBLP.json'




def getelements():
    context = iter(etree.iterparse(source_xml, events=('start', 'end'),load_dtd=True))
    _, root = next(context) # get root element
    for event, elem in context:
        if event == 'end' and elem.tag in allTags:
            yield elem
            root.clear() # free memory



def keep(page):

    if page.tag in unwantedTags:
        print("deleted(unwanted): ", page.tag)
        return False
    if page.tag== 'article':
        sub = map(lambda x: x.tag, list(page.iter()))
        if 'journal' not in sub:
            print("deleted(no journal): ", page.tag)
            return False

    # yearPage = page.find('year').text
    # if int(yearPage)<2002:
    #     print("deleted(under 2002): ", page.tag)
    #     return False

    return True

with open(dest_xml, 'wb') as file:
    # start root
    file.write(b'<?xml version="1.0" encoding="ISO-8859-1"?>\n')
    file.write(b'<!DOCTYPE dblp SYSTEM "dblp.dtd">\n')
    file.write(b'<dblp>\n')
    counter=0
    for page in getelements():
        if keep(page):
            print(counter)
            counter+=1
            file.write(etree.tostring(page, encoding='utf-8'))

    # close root
    file.write(b'</dblp>')

print(counter)