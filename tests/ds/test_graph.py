from src.ds.graph import Graph


class TestGraph(object):

    def test_sanity(self):
        # Create
        graph = Graph()
        assert graph._conns == {}

        # Default connection weight
        graph.connect("A", "B")
        assert graph._conns == {
            "A": {
                "B": Graph.DEFAULT_WEIGHT
            },
            "B" : {}
        }

        # Custom connection weight
        graph.connect("B", "A", weight=2)
        assert graph._conns == {
            "A": {
                "B": Graph.DEFAULT_WEIGHT
            },
            "B": {
                "A": 2
            }
        }

        # More connections
        graph.connect("A", "C", weight=3)
        assert graph._conns == {
            "A": {
                "B": Graph.DEFAULT_WEIGHT,
                "C": 3
            },
            "B": {
                "A": 2
            },
            "C": {}
        }

        # Disconnect
        graph.disconnect("B", "A")
        assert graph._conns == {
            "A": {
                "B": Graph.DEFAULT_WEIGHT,
                "C": 3
            },
            "B": {},
            "C": {}
        }
