from IPython.display import Image, Markdown, HTML
import pandas as pd
import plotly.express as px
import random


def welcome():
    print("Welcome to Vincent's landing page!\nVincent can operate a notebook to do multistep tasks for you.\nGo ahead explore this landing page through your curiosity.\n")

def vincent_help():
    print("Vincent's landing page methods:")
    methods = [
    ("what_does_vincent_do()", "What Vincent actually does. Technically"),
    ("common_use_cases()", "How users are using Vincent"),
    ("join_waitlist()", "A button to join the waitlist"),
    ("privacy()", "Vincent's privacy and security details"),
    ("extendable()", "How to extend Vincent through an opensource skills"),
    ("manifesto()", "Why we're building Vincent, and how it's different"),
    ("features()", "Vincent's standout capabilities"),
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


def feature_importance():
    """Discover the standout capabilities of Vincent."""
    feature_importance = {
        "Error correction": "Automatically detects and fixes code errors in real-time",
        "Prompt enhancement": "Improves user prompts for better results and clearer communication",
        "Custom Instructions": "Allows users to set persistent preferences and coding styles",
        "Control Permissions": "Granular control over what Vincent can access and modify",
        "Context": "Maintains awareness of the full codebase and conversation history",
        "Steps": "Breaks down complex tasks into clear, manageable steps"
    }
    # Feature names and arbitrary importance values
    features = list(feature_importance.keys())
    importance_values = [random.uniform(0, 1) for _ in features]  # Generate random importance values

    # Create a DataFrame for plotting
    importance_df = pd.DataFrame({'Feature': features, 'Importance': importance_values, 'Description': list(feature_importance.values())})

    # Create an interactive bar plot
    fig = px.bar(importance_df, x='Feature', y='Importance', 
                title='Feature Importance',
                hover_data={'Description': True},  # Only show descriptions on hover
                labels={'Importance': 'Importance Value'})
    fig.show()
    return  
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
    return print("""Yes, Vincent's landing page is a functional notebook (running in browser thanks to pyodide).
Made sense. Notebooks create a rich narrative, and data scientists love to explore. 
And we want to let them.""")

def pricing():
    """Learn about Vincent's pricing."""
    return print("While in beta, Vincent is completely free to use. Even after the beta, Vincent will always have a free tier.")    

