import os

THEMES = {
    "Dark": """
[theme]
base="dark"
primaryColor="#00B4D8"
backgroundColor="#0E1117"
secondaryBackgroundColor="#161B22"
textColor="#FAFAFA"
font="sans serif"
""",

    "Light": """
[theme]
base="light"
primaryColor="#1976D2"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F3F4F6"
textColor="#262730"
font="sans serif"
""",

    "Blue": """
[theme]
base="light"
primaryColor="#1565C0"
backgroundColor="#EAF4FF"
secondaryBackgroundColor="#D6E9FF"
textColor="#003366"
font="sans serif"
"""
}


def save_theme(theme_name):

    config = THEMES[theme_name]

    config += """

[server]
headless=true
runOnSave=true

[browser]
gatherUsageStats=false

[client]
toolbarMode="minimal"

[runner]
fastReruns=true
"""

    os.makedirs(".streamlit", exist_ok=True)

    with open(".streamlit/config.toml", "w", encoding="utf-8") as f:
        f.write(config)