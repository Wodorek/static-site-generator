from textnode import TextNode


def main():
    node = TextNode('A node', 'bold', 'https://google.com')

    print(node.__repr__())


if __name__ == '__main__':
    main()
