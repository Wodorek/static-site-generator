from markdown_blocks import markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    title = ''

    for block in blocks:
        if block.startswith('# '):
            title = block.strip().replace('# ', '')

    if len(title) > 0:
        return title

    raise Exception('no valid title found')
