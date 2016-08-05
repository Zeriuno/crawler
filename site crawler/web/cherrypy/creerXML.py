from lxml import etree

def creationXML():
    users = etree.Element("users")

    words_level1 = []

    for words_level1 in words_level1:
        user = etree.SubElement(users, "user")
        user.set("data-id", words_level1[0])
        nom = etree.SubElement(user, "nom")
        nom.text = words_level1[1]
        metier = etree.SubElement(user, "metier")
        metier.text = words_level1[2]
        print(etree.tostring(users, pretty_print=True))
