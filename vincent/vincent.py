from IPython.display import Image, Markdown, HTML, display
import plotly.express as px


def welcome():
    print("Welcome to Vincent's landing page!\nVincent can operate a notebook to do multistep tasks for you.\nGo ahead explore this landing page through your curiosity.\n")

def vincent_help():
    print("Vincent's landing page methods:")
    methods = [
    ("what_does_it_do()", "What Vincent actually does. Technically"),
    ("common_use_cases()", "How users are using Vincent"),
    ("download()", "Try Vincent today"),
    ("privacy()", "Vincent's privacy and security details"),
    ("manifesto()", "Why we're building Vincent, and how it's different"),
    ("feature_importance()", "Vincent's standout capabilities"),
    ("loved_by()", "How users and developers are leveraging Vincent"),
    ("about()", "About this landing page"),
    ("pricing()", "Pricing details"),
]

# Formatting the table as plain text
    print(f"{'Method':<25} {'Description'}")
    print("=" * 60)
    for method, description in methods:
        print(f"{method:<25} {description}")
    return


def what_does_it_do():
    """Shows Vincent's main capabilities through a visual demonstration."""
    print("""It's pretty simple. 
Vincent can see your notebook and act on it like a collaborator.
When you ask it something, it will plan, act and observe in a loop until finished.""")
    return Image(filename="data/vincent_loop.png.png")

def common_use_cases():
    """Displays a word cloud of Vincent's common use cases."""
    print('Here are some common things users are asking from Vincent:')
    return Image(filename="data/word_cloud.png")

def download():
    """Provides a link to join the waitlist."""
    print("Vincent in your VSCode:")
    print("• Alpha version\n• Extension\n• Local")
    
    download_button = HTML('''
        <a href="https://marketplace.visualstudio.com/items?itemName=BespoAI.vincent&ssr=false#overview" 
           target="_blank"
           style="
               display: inline-block;
               text-align: center !important;
               background-color: #000000;
               border: 2px solid #000000;
               color: white;
               padding: 12px 24px;
               text-decoration: none;
               font-size: 14px;
               font-weight: 500;
               margin: 8px 0;
               cursor: pointer;
               border-radius: 6px;
               transition: all 0.2s ease-in-out;
           "
           onmouseover="this.style.backgroundColor='#ffffff'; this.style.color='#000000';"
           onmouseout="this.style.backgroundColor='#000000'; this.style.color='#ffffff';">
           Download
        </a>
    ''')
    
    display(download_button)
    
    print("\nVincent in the cloud:")
    print("• Organizational collaboration and memory\n• It's own compute resources\n• Multiple Vincent instances in parallel\n• Longer tasks")
    
    waitlist_button = HTML('''
        <a href="https://example.com/waitlist" 
           target="_blank"
           style="
               display: inline-block;
               text-align: center !important;
               background-color: #000000;
               border: 2px solid #000000;
               color: white;
               padding: 12px 24px;
               text-decoration: none;
               font-size: 14px;
               font-weight: 500;
               margin: 8px 0;
               cursor: pointer;
               border-radius: 6px;
               transition: all 0.2s ease-in-out;
           "
           onmouseover="this.style.backgroundColor='#ffffff'; this.style.color='#000000';"
           onmouseout="this.style.backgroundColor='#000000'; this.style.color='#ffffff';">
           Waitlist
        </a>
    ''')
    
    return waitlist_button

def privacy():
    """Understand Vincent's privacy and security principles."""
    return Markdown("""1. We don't train on your data. 
\n 2. We offer self-hosting with support for your own model provider API key - No data leaves your cloud environment. 
\n 3. [privacy policy](https://bespo.notion.site/privacypolicy) 
\n 4. [terms of service](https://bespo.notion.site/tos)""")

def manifesto():
    """Explore the vision, philosophy, and mission behind Vincent."""
    with open('data/manifesto.md', 'r') as f:
        return Markdown(f.read())


def feature_importance():
    """Discover the Vincent's features. And their importance?"""
    return Image(filename="data/feature_importance.png")

def loved_by():
    """See how users and developers are leveraging Vincent effectively."""
    return Markdown("""
#### Seffi Cohen ⭐⭐⭐⭐⭐

Super impressive! Vincent has greatly enhanced my research, beyond all other LLMs solutions. Its ability to automatically fix errors and seamlessly handle package dependencies is a game-changer. Highly recommend!

#### Anthony Goldbloom ⭐⭐⭐⭐⭐

This is a huge step up from Github Copilot. It's able to build end to end analysis very accurately. It allows me to specify my preferred libraries (e.g. Plotly for charts). If I have the start of an analysis (e.g. reading in a DataFrame) it learns the columns of that DataFrame and builds on top of it. I almost never start a notebook without using Vincent.
""")

def about():
    """Learn about this notebook landing page."""
    return print("""Yes, Vincent's landing page is a functional python notebook (running in browser thanks to pyodide).
Made sense. Notebooks create a rich narrative, and data scientists love to explore. 
And we're here to let them.""")

def pricing():
    """Learn about Vinccent's priing."""
    return print("While in beta, Vincent is completely free to use.")    