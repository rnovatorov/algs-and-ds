from proboscis import TestProgram


def main():
    from tests import graph

    TestProgram(groups=[
        "graph-edge",
        "graph-vertex"
    ]).run_and_exit()


if __name__ == "__main__":
    main()
