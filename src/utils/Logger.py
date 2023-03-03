class Logger:
    def __init__(self, name: str) -> None:
        self.name = name

    def info(self, s: str) -> None:
        print(f'[{self.name}] {s}')


def main():
    logger = Logger("MyLogger")
    logger.info("1")
    logger.info("2")
    logger.info("3")


if __name__ == '__main__':
    main()
