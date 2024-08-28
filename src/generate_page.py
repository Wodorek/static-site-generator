from extract_title import extract_title
from markdown_blocks import markdown_to_html_node
import os
import pathlib


def generate_page(from_path, template_path, dest_path):

    print(f'generating page from {from_path} to {
          dest_path} using {template_path} as template')

    content = open(from_path, 'r').read()
    template = open(template_path, 'r').read()
    title = extract_title(content)

    md_as_html = markdown_to_html_node(content).to_html()

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', md_as_html)

    open(os.path.join(dest_path, 'index.html'), 'w').write(template)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):

    items = os.listdir(dir_path_content)

    print(dest_dir_path)

    print(items)

    for item in items:

        path_to_item = os.path.join(dir_path_content, item)

        if os.path.isdir(path_to_item):

            path_to_dest = os.path.join(dest_dir_path, item)

            if not os.path.exists(path_to_dest):
                os.mkdir(path_to_dest)

            generate_page_recursive(
                path_to_item, template_path, path_to_dest)

        else:
            generate_page(path_to_item, template_path, dest_dir_path)
