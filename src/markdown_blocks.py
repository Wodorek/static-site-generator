block_type_heading = 'heading'
block_type_paragraph = 'paragraph'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_ulist = 'ulist'
block_type_olist = 'olist'


def markdown_to_blocks(markdown):

    blocks = markdown.split('\n\n')

    def remove_blank(items):
        new_items = []

        for item in items:
            if len(item) > 0:
                new_items.append(item)

        return new_items

    stripped = list(map(lambda x: x.strip(), blocks))
    blank_removed = remove_blank(stripped)

    return blank_removed


def block_to_block_type(block):

    lines = block.split('\n')

    if (block.startswith('# ')
            or block.startswith('## ')
            or block.startswith('### ')
            or block.startswith('#### ')
            or block.startswith('##### ')
            or block.startswith('###### ')):

        return block_type_heading

    if (lines[0].startswith("```") and lines[-1].startswith("```")):

        return block_type_code

    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph

        return block_type_quote

    if block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph

        return block_type_ulist

    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph

        return block_type_ulist

    if block.startswith('1. '):

        i = 1

        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1

        return block_type_olist

    return block_type_paragraph
