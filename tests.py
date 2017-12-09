from proboscis import TestProgram


def main():
    import tests

    TestProgram(
        groups=[
            "graph",
            "sorting"
        ]
    ).run_and_exit()


if __name__ == "__main__":
    main()
