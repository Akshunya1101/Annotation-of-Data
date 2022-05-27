import xml.etree.ElementTree as ET
mytree = ET.ElementTree(file='case.xml')
myroot = mytree.getroot()

out = open('output.txt', 'w')
for i in myroot:
    #if i.tag =='Laws' :
    # out.write("Root Tags : " + i.tag + '\n')
    if(i.tag=='JudgmentText'):
        for legis in i:
            # out.write("Inside Judgement Text : " + legis.tag + '\n')
            if(legis.tag=='I'):
                for para in legis:
                    out.write(para.text + '\n\n')