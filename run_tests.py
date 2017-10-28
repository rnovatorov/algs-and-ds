from proboscis import TestProgram


def main():
    from tests.graph import GraphTest

    TestProgram().run_and_exit()


if __name__ == "__main__":
    main()
