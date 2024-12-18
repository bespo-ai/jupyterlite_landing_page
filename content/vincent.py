
def what_can_vincent_do():
    """Shows Vincent's main capabilities through a visual demonstration."""
    from IPython.display import Image
    return Image(filename="content/data/what_do_vincent_do.png")

def use_cases_word_cloud():
    """Displays a word cloud of Vincent's common use cases."""
    from IPython.display import Image
    return Image(filename="content/data/word_cloud.png")

def download_vincent():
    """Provides a link to download Vincent from the VS Code marketplace."""
    from IPython.display import Markdown
    return Markdown("[Download Vincent from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=BespoAI.vincent&ssr=false#overview)")

def privacy():
    """Understand Vincent's privacy and security principles."""
    return "Vincent offers self-hosting with support for your own model provider API key. This ensures that no data ever leaves your secure cloud environment, keeping your workflows private and compliant."

def extendable():
    """Learn how to customize and extend Vincent for your workflows."""
    from IPython.display import Image
    return Image(filename="content/data/extendable.png")

def manifesto():
    """Explore the vision, philosophy, and mission behind Vincent."""
    with open('content/data/manifesto.md', 'r') as f:
        from IPython.display import Markdown
        return Markdown(f.read())

def features():
    """Discover the standout capabilities of Vincent."""
    return "Vincent's features include notebook operation, code assistance, and natural language interaction capabilities."

def love_by():
    """See how users and developers are leveraging Vincent effectively."""
    return "Vincent is being used by data scientists and researchers for enhanced workflow productivity and creative exploration."

def about():
    """Learn about this notebook landing page."""
    return "This is Vincent's landing page notebook, showcasing its capabilities and principles."