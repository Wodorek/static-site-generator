from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        text = node.text.split(delimiter)

        if len(text) % 2 == 0:
            raise ValueError('Invalid markdown')

        for i in range(len(text)):

            if text[i] == '':
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(text[i], text_type_text))
            else:
                new_nodes.append(TextNode(text[i], text_type))

    return new_nodes
