# assets/Model.py
from thefuzz import fuzz

qa_data = {
    "who is your creator": (
        "I'm created by **Kolkata Model School** students, built by a group of passionate developers and designers:\n\n"
        "**#India** 🇮🇳\n"
        "- @swaroj (Owner / Backend Dev)\n"
        "- @player (Tester)\n"
        "- @player (Helper)\n"
        "- @player (Trainer)\n\n"
        "**#Indonesia** 🇮🇩\n"
        "- @Roan (Backend Dev)\n\n"
        "**#Ukraine** 🇺🇦\n"
        "- @Yuri (Backend Dev)\n\n"
        "**#America** 🇺🇸\n"
        "- @Lisa (UI Designer)\n"
        "- @Emma (UI Designer)"
    )
}

def get_static_answer(user_input):
    cleaned_input = user_input.strip().lower().rstrip("?")
    for question, answer in qa_data.items():
        if fuzz.partial_ratio(cleaned_input, question) >= 80:
            return answer
    return None
