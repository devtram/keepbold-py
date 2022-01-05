import os  # for directory/file access
from pathlib import Path  # for path access
from bs4 import BeautifulSoup

# packaging html-font-weight to <strong> python script into function
def replacefw_tostrong(html_file_unfiltered):
    # 1st step - started small
    soup = BeautifulSoup(html_file_unfiltered,  'html.parser')

    # 2nd Step - another more small step
    for htmltag in soup.find_all('span'):
        if htmltag.has_attr('style'):
            # if found = style.properties >>> contain('font-weight') then
            if htmltag['style'].__contains__('font-weight'):
                # soup.span  = 'strong'
                htmltag.name = 'strong'
                soup.span = htmltag.name

    return soup




# open file calling the function write the filtered html and then close
for dirpath, dirs, files in os.walk("."):
    print("--" + dirpath)
    for filename in files:
        if filename.endswith(".html"):

            print("filename:", filename)
            file = open(os.path.join(dirpath, filename), "r").read()
            html_filtered = replacefw_tostrong(file)

            markdown_file = open(os.path.join(dirpath, filename.replace(".html", ".htm")), "w")         
            n = markdown_file.write(html_filtered.__str__())
            markdown_file.close()
        else:
            continue

