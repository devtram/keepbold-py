import os  # for directory/file access
from pathlib import Path  # for path access
from bs4 import BeautifulSoup

html = """
<table style="position:absolute; border: textbox 1px solid; writing-mode:lr-tb; left:45px; top:81px; width:127px; height:9px;">
    <h1 style="font-family: EICMDA+AdvTrebu-R; font-size:8px">Journal of     Infection (2015) 
    </h1>
    <h2 style="font-family: EICMDB+AdvTrebu-B; font-size:8px">xx</h2>
    <h3 style="font-family: EICMDA+AdvTrebu-R; font-size:8px">, 1</h3>
    <h4 style="font-family: EICMDD+AdvPS44A44B; font-size:7px">e</h4>
    <h5 style="font-family: EICMDA+AdvTrebu-R; font-size:8px">4
    <br/>
    </h5>
</table>

"""

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

