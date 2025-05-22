import traceback

def save_graph(graph, filename):
    """
    Save the graph to a file in GraphML format.
    """
    try:
        png_bytes = graph.get_graph().draw_mermaid_png()
        with open("graph.png", "wb") as f:
            f.write(png_bytes)
        # display(Image(png_bytes))
    except Exception:
        traceback.print_exc()