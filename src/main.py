from textnode import TextType, TextNode


def main():
    test = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(test)


if __name__ == "__main__":
    main()
