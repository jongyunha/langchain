import struct

from langchain.schema import BaseOutputParser


class CommandOutputParser(BaseOutputParser):
    def parse(self, text):
        items = text.strip().split(",")
        return list(map(str.strip, items))


if __name__ == "__main__":
    parser = CommandOutputParser()
    text = "1,2,3,4,5"
    print(parser.parse(text))
