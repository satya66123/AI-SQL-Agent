def dark():
    return """
    <style>

    .stApp{
        background-color:#0E1117;
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:#161B22;
    
    }

    div[data-baseweb="select"] > div{
        background:#1E1E2F;
        color:white;
    }

    .stButton>button{
        background:#00B4D8;
        color:white;
        border:none;
        border-radius:8px;
    }

    .stTextInput input,
    .stTextArea textarea{
        background:#1E1E2F;
        color:white;
    }

    </style>
    """