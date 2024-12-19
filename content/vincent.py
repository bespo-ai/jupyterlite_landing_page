
from IPython.display import Image, Markdown

def what_can_vincent_do():
    """Shows Vincent's main capabilities through a visual demonstration."""
    return Image(filename="data/what_do_vincent_do.png")
def use_cases_word_cloud():
    """Displays a word cloud of Vincent's common use cases."""
    return Image(filename="data/word_cloud.png")

def join_waitlist():
    """Provides a link to join the waitlist."""
    return Markdown("[Waitlist](https://marketplace.visualstudio.com/items?itemName=BespoAI.vincent&ssr=false#overview)")

def privacy():
    """Understand Vincent's privacy and security principles."""
    return print("Vincent offers self-hosting with support for your own model provider API key. This ensures that no data ever leaves your secure cloud environment, keeping your workflows private and compliant.")

def extendable():
    """Learn how to customize and extend Vincent for your workflows."""
    return Image(filename="data/extendable.png")

def manifesto():
    """Explore the vision, philosophy, and mission behind Vincent."""
    with open('data/manifesto.md', 'r') as f:
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