def blue():
    return """
    <style>

    .stApp{
        background-color:#EAF4FF;
        color:#003366;
    }

    section[data-testid="stSidebar"]{
        background:#D6E9FF;
    }

    div[data-baseweb="select"] > div{
        background:white;
        color:#003366;
    }

    .stButton>button{
        background:#1565C0;
        color:white;
        border:none;
        border-radius:8px;
    }

    .stButton>button:hover{
        background:#0D47A1;
    }

    .stTextInput input,
    .stTextArea textarea{
        background:white;
        color:#003366;
        border:1px solid #64B5F6;
    }

    </style>
    """