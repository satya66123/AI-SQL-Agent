def light():
    return """
    <style>

    .stApp{
        background-color:white;
        color:black;
    }

    section[data-testid="stSidebar"]{
        background:#F5F5F5;
        color:black;
    }
    
    input[type="radio"]{
    color:black;
    }

    div[data-baseweb="select"] > div{
        background:white;
        color:black;
    }

    .stButton>button{
        background:#1976D2;
        color:white;
        border:none;
        border-radius:8px;
    }

    .stTextInput input,
    .stTextArea textarea{
        background:white;
        color:black;
        border:1px solid #CCCCCC;
    }

    </style>
    """