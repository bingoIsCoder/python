import urllib.request
import re


def split_poetry(poetry):
    data = re.split(r'[，。？]', poetry)
    data = [item for item in filter(lambda x: x != '', data)]  # remove empty string
    return data


mach_code = r'<a style=".*?" target=".*?" href="/mingju/.*?">(.*?)</a>'

url = "http://so.gushiwen.org/mingju/Default.aspx?p="

page_num = 116
count = 1
pre_compile = re.compile(mach_code)

poetry_file = open('poetry.txt', 'w', encoding='utf-8')

for index in range(1, page_num + 1):
    full_url = url + ('%d' % index)
    print(full_url)
    data = urllib.request.urlopen(full_url).read().decode('utf-8')
    poetry_list = pre_compile.findall(data)
    for poetry in poetry_list:
        sp_list = split_poetry(poetry)
        for single in sp_list:
            poetry_file.write('%d' % count)
            poetry_file.write(';"' + single + '";\n')
            count += 1
poetry_file.close()


#    print(poetry)

