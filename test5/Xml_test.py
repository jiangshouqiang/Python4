import xml.etree.ElementTree
import io
# tree = xml.etree.ElementTree.ElementTree()
fh = open("MCA0017034_CTL.XML").read()
print(io.StringIO(fh))
tree = xml.etree.ElementTree.parse("MCA0017034_CTL.XML",parser=None)
# parse = xml.etree.ElementTree.ElementTree.getiterator()
# print(tree.parse(fh))
set = []
# for element in tree.attrib:
#     set.append(element)
for el in tree.getiterator("Set"):
    print(el.text)
