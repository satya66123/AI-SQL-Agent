from src.history.chat_history import ChatHistory

ChatHistory.add_message(

    "user",

    "Show all employees"

)

ChatHistory.add_message(

    "assistant",

    "SELECT * FROM employees"

)

print(

    ChatHistory.get_history()

)

print("--------------------------------")

print(

    ChatHistory.build_context()

)