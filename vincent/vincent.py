from IPython.display import Image, Markdown, HTML

def welcome():
    print("Welcome to Vincent's landing page!\nVincent can operate a Jupyter notebook to do multistep tasks for you.\nGo ahead explore this landing page through your curiosity.")

def what_does_vincent_do():
    """Shows Vincent's main capabilities through a visual demonstration."""
    return Image(filename="data/what_do_vincent_do.png")

def common_use_cases():
    """Displays a word cloud of Vincent's common use cases."""
    print('Here are some common things users are asking from Vincent:')
    return Image(filename="data/word_cloud.png")

def join_waitlist():
    """Provides a link to join the waitlist."""
    button = HTML('''
        <div style="text-align: center;">
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
               Join Waitlist
            </a>
        </div>
    ''')
    return button

def privacy():
    """Understand Vincent's privacy and security principles."""
    return Markdown("1. We don't train on your data. \n2. We offer self-hosting with support for your own model provider API key - No data leaves your cloud environment.")

def extendable():
    """Learn how to customize and extend Vincent for your workflows."""
    print("We teach Vincent skills - you can too.\nAll skills are open source.")
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
    return Markdown("""
#### Seffi Cohen ⭐⭐⭐⭐⭐

Super impressive! Vincent has greatly enhanced my research, beyond all other LLMs solutions. Its ability to automatically fix errors and seamlessly handle package dependencies is a game-changer. Highly recommend!

#### Anthony Goldbloom ⭐⭐⭐⭐⭐

This is a huge step up from Github Copilot. It's able to build end to end analysis very accurately. It allows me to specify my preferred libraries (e.g. Plotly for charts). If I have the start of an analysis (e.g. reading in a DataFrame) it learns the columns of that DataFrame and builds on top of it. I almost never start a notebook without using Vincent.
""")

def about():
    """Learn about this notebook landing page."""
    return print("""Yes, Vincent's landing page is a functional notebook (running in browser thanks to pyodide).
Made sense. Notebooks create a rich narrative, and data scientists love to explore. 
And we want to let them.""")

def pricing():
    """Learn about Vincent's pricing."""
    return "While in beta, Vincent is completely free to use. Even after the beta, Vincent will always have a free tier."

def vincent_help():
    # import pandas as pd

    return """{
        'Method': [
            'what_does_vincent_do()',
            'common_use_cases()',
            'join_waitlist()',
            'privacy()',
            'extendable()',
            'manifesto()',
            'features()',
            'love_by()',
            'about()',
            'pricing()'
        ],
        'Description': [
            'What vincent actually does. Technically',
            'How users are using Vincent',
            'a button to join the waitlist',
            'Vincent\'s privacy and security details', 
            'How to extend Vincent through an opensource framework',
            'Why we\'re building Vincent, and how it\'s different',
            'Vincent\'s standout capabilities',
            'Why data scientists love Vincent',
            'About this landing page, not about us=]',
            'Pricing details'
        ]
    }"""
