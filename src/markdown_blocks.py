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
