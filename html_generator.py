
import os
import sys, getopt
from pathlib import Path
from bs4 import BeautifulSoup
import markdown as m
from string import Template

# The directory where we search for Markdown files and we output the HTML one
html_dir = "./posts/"

summary_template = """
<h5 class='text-uppercase color-dark text-bold'>
<a href="posts/$html_filename">$title</a>
</h5>
$summary
<br><br>
"""

# Find all .md files and returns all names as a list
def list_md_files():
    return [md for md in os.listdir(html_dir) if md.endswith(".md")]

# Using the filename it returns a post title
def get_title(filename):
    title = os.path.splitext(filename)[0]
    title = title.replace("_", " ")
    return title.title()

# Write HTML pages
def write_html(html_documents):
    if len(html_documents) == 0:
        print("No HTML pages to write.")
    else:
        for filename, content in html_documents.items():
            with open(html_dir+filename, 'w', encoding='utf-8') as mdfile:
                mdfile.write(content)
                print("Generated: "+filename)

# Get the summary code for the front page
def get_summary(html_filename, title, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    summary = soup.find_all('p')[1].text
    template = Template(summary_template)
    return template.substitute(summary=summary, title=title,html_filename=html_filename)

# - Convert all markdown to HTML
# - Get the title of the post
# - Apply the document template
# - Store filename and content inside a dictionary and return it
def convert_md_to_html(md_list,generate_all):
    html_documents = dict()
    template = "./template.html"
    with open(template, 'r', encoding='utf-8') as template_file:
        template = Template(template_file.read())
        for md in md_list:
            # Check if the html file already exists to skip the creation.
            if not os.path.exists(html_dir+md.replace(".md", ".html")) or generate_all==True:
                with open(html_dir+md, 'r', encoding='utf-8') as mdfile:
                    content = m.markdown(mdfile.read(),extensions=['markdown.extensions.tables','markdown.extensions.fenced_code'])
                    title = get_title(md)
                    html_content = template.substitute(content=content, title=title)
                    html_filename = md.replace(".md", ".html")
                    html_documents[html_filename]=html_content
                    print(get_summary(html_filename,title,html_content))
    return html_documents

def main(argv):
    
    # By default, we don't generate all html documents. Only the new ones.
    generate_all=False

    try:
        opts, _ = getopt.getopt(argv,"ha")

    except getopt.GetoptError:
        print('\ngenerate.py:\n')
        print('\t-h: this help.')
        print('\t-a: generate all posts.\n')
        sys.exit(2)

    for opt, _ in opts:
      if opt == '-h':
        print('\ngenerate.py:\n')
        print('\t-h: this help.')
        print('\t-a: generate all posts.\n')
        sys.exit()
      elif opt in ("-a"):
        generate_all = True
    
    # Clean the database if we are going to generate everything

    html_documents = convert_md_to_html(list_md_files(),generate_all)
    write_html(html_documents)

if __name__ == "__main__":
    main(sys.argv[1:])