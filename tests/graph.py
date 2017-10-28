from proboscis import test, before_class
from hamcrest import assert_that, is_, is_not, equal_to, has_length, same_instance
from src.graph import Graph, Vertex, Edge


@test
class GraphTest(object):
    """
    Tests that Graph data structure functions properly
    """
    @test
    def sanity(self):
        va_id = "A"
        vb_id = "B"
        vids = [va_id, vb_id]
        edges = {Edge(va_id, vb_id, bidir=False)}
        graph = Graph(vids, edges)

        assert_that(graph.vertices, has_length(len(vids)))

        assert_that(graph.vertices[va_id].id, is_(equal_to(va_id)))
        assert_that(graph.vertices[vb_id].id, is_(equal_to(vb_id)))

        assert_that(graph.vertices[va_id].graph, is_(same_instance(graph)))
        assert_that(graph.vertices[vb_id].graph, is_(same_instance(graph)))

    @test
    def adjacency(self):
        va_id = "A"
        vb_id = "B"
        vids = [va_id, vb_id]
        edges = {Edge(va_id, vb_id, bidir=False)}
        graph = Graph(vids, edges)

        va, vb = graph.vertices[va_id], graph.vertices[vb_id]

        assert_that(va.is_adjacent_to(vb), is_(True))
        assert_that(vb.is_adjacent_to(va), is_(False))

    @test
    def adjacency_bidirectional(self):
        va_id = "A"
        vb_id = "B"
        vids = [va_id, vb_id]
        edges = {Edge(va_id, vb_id, bidir=True)}
        graph = Graph(vids, edges)

        va, vb = graph.vertices[va_id], graph.vertices[vb_id]

        assert_that(va.is_adjacent_to(vb), is_(True))
        assert_that(vb.is_adjacent_to(va), is_(True))

    @test
    def depth_first_search(self):
        vids = ["A", "B", "C", "D"]

    @test
    def breadth_first_search(self):
        pass


@test
class VertexTest(object):
    """
    Tests Graph's component Vertex
    """
    @test
    def labeling(self):
        test_id = "T"
        v = Vertex(id=test_id, graph=Graph())
        assert_that(v.id, is_(equal_to(test_id)))

    @test
    def connection(self):
        graph = Graph()
        va, vb = Vertex("A", graph=graph), Vertex("B", graph=graph)
        assert_that(va.is_adjacent_to(vb), is_(False))

        va.connect_to(vb)
        assert_that(va.is_adjacent_to(vb), is_(True))

    @test
    def disconnection(self):
        graph = Graph()
        va, vb = Vertex("A", graph=graph), Vertex("B", graph=graph)
        assert_that(va.is_adjacent_to(vb), is_(False))

        va.connect_to(vb)
        assert_that(va.is_adjacent_to(vb), is_(True))

        va.disconnect_from(vb)
        assert_that(va.is_adjacent_to(vb), is_(False))


@test
class EdgeTest(object):
    """
    Tests Graph's component Edge
    """
    pass
