from src.algs.tables import tabularize, detabularize


def test_sanity():
    table = tabularize(
        [
            {"foo": "bar"},
            {"foo": "bar", "ham": "goo"},
            {"foo": "bar", "ham": "goo", "gym": "jam"},
        ]
    )
    assert table == {
        "foo": ["bar", "bar", "bar"],
        "ham": [None, "goo", "goo"],
        "gym": [None, None, "jam"],
    }
    assert detabularize(table) == [
        {"foo": "bar", "ham": None, "gym": None},
        {"foo": "bar", "ham": "goo", "gym": None},
        {"foo": "bar", "ham": "goo", "gym": "jam"},
    ]
