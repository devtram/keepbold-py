
from bs4 import BeautifulSoup
import cssutils
import re 


html_file = """
            <p lang="en-GB" ><span style="font-weight:bold;">MODULE 3: </span><span style="font-weight:bold"> UI and UX Scenarios </span></p>
			<p lang="en-GB" ><span >Homepage UX Scenarios WITH UI</span></p>
			<p lang="en-GB" ><span >Shopping Page UX Scenarios WITH UI</span></p>
			<p lang="en-GB" ><span >Final Theme for Homepage</span></p>
			<p lang="en-GB" ><span >Saasland</span></p>
			<h2 lang="en-GB" ><span >Final Theme for Shopping</span></h2>
			<h1 lang="en-GB" ><span >Any Customization?</span></h1>
"""

# 1st step - started small
soup = BeautifulSoup(html_file,  'html.parser')

# 2nd Step - a little more small step
for span in soup.find_all('span'):
    if span.has_attr('style'):
        text = re.compile(r':font-weight')
        # if found = style.properties >>> contain('font-weight') then
        if span['style'].__contains__('font-weight'):
            soup.span.name = 'strong'
print(soup)


# statement mistakes
## if soup.span.attrs.__contains__('font-weight'):


