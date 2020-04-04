"""
Simple HTML generator from Markdown:
- Reads all the .md files present.
- Converts them to HTML using the template template.html
- Outputs a short summary that can be copy/pasted on some sort of indes

Used for https://blog.miguelangelnieto.net
"""

import os
import sys
import getopt
from string import Template
import markdown as m
from bs4 import BeautifulSoup

# The directory where we search for Markdown files and we output the HTML one
HTML_DIR = "./posts/"

SUMMARY_TEMPLATE = """
<h5 class='text-uppercase color-dark text-bold'>
<a href="posts/$html_filename">$title</a>
</h5>
$summary
<br><br>
"""

def list_md_files():
    """
    Find all .md files and returns all names as a list
    """
    return [md for md in os.listdir(HTML_DIR) if md.endswith(".md")]

def get_title(filename):
    """
    Using the filename it returns a post title
    """
    title = os.path.splitext(filename)[0]
    title = title.replace("_", " ")
    return title.title()

def write_html(html_documents):
    """
    Write HTML pages
    """
    if len(html_documents) == 0:
        print("No HTML pages to write.")
    else:
        for filename, content in html_documents.items():
            with open(HTML_DIR+filename, 'w', encoding='utf-8') as mdfile:
                mdfile.write(content)
                print("Generated: "+filename)

def get_summary(html_filename, title, html_content):
    """
    Returns the summary of the post.
    - Page title
    - First paragraph
    TODO: To automate this...
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    summary = soup.find_all('p')[1].text
    template = Template(SUMMARY_TEMPLATE)
    return template.substitute(summary=summary, title=title, html_filename=html_filename)

def convert_md_to_html(md_list, generate_all):
    """
    - Convert all markdown to HTML
    - Get the title of the post
    - Apply the document template
    - Store filename and content inside a dictionary and return it
    """
    html_documents = dict()
    template = "./template.html"
    with open(template, 'r', encoding='utf-8') as template_file:
        template = Template(template_file.read())
        for md_file in md_list:
            # Check if the html file already exists to skip the creation.
            if not os.path.exists(HTML_DIR+md_file.replace(".md", ".html")) or generate_all:
                with open(HTML_DIR+md_file, 'r', encoding='utf-8') as mdfile:
                    content = m.markdown(mdfile.read(),
                                         extensions=['markdown.extensions.tables',
                                                     'markdown.extensions.fenced_code'])
                    title = get_title(md_file)
                    html_content = template.substitute(content=content, title=title)
                    html_filename = md_file.replace(".md", ".html")
                    html_documents[html_filename] = html_content
                    print(get_summary(html_filename, title, html_content))
    return html_documents

def main(argv):
    """
    Main function. We generate the HTML pages.
    """
    generate_all = True

    try:
        opts, _ = getopt.getopt(argv, "ha")

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
      elif opt in "-a":
        generate_all = True

    html_documents = convert_md_to_html(list_md_files(), generate_all)
    write_html(html_documents)

if __name__ == "__main__":
    main(sys.argv[1:])
