from lxml import etree
def main():
    xml = etree.parse('config.xml')
    root = xml.getroot()
    filepath = root.xpath('//douyinpath')[0].text
    chromepath = root.xpath('//chromepath')[0].text
    toutiaopic = root.xpath('//toutiaopic')[0].text
    pathconfig = [chromepath,toutiaopic,filepath]
    return pathconfig