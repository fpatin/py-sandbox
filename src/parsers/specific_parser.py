from parser import Parser


class SpecificParser(Parser):

    def parse(self, s: str):
        print(f"Parsing {s}")
