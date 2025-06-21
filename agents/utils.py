import traceback

def save_graph(graph, filename):
    """
    Save a compiled langgraph graph as a PNG image file.

    Args:
        graph: The compiled langgraph graph object.
        filename: The file path (including file name) to save the image.

    Functionality:
        Calls the langgraph draw_mermaid_png method to generate PNG bytes of the graph,
        and writes them to the specified file.
        If an exception occurs during saving, the stack trace will be printed.
    """
    try:
        png_bytes = graph.get_graph().draw_mermaid_png()
        with open("graph.png", "wb") as f:
            f.write(png_bytes)
        # display(Image(png_bytes))
    except Exception:
        traceback.print_exc()