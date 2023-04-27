import graphviz


def draw(vertices, edges):
    pass


dot = graphviz.Source("""
digraph {
1 [label="A"]
2 [label="B"]
1 -> 2
2 -> 1
}
""")

print(dot)