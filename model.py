def static_answer(message):
    msg = message.lower()

    # Responses for basic questions
    if any(word in msg for word in ["your name", "who are you", "what are you"]):
        return "I am V.O.I.D – Versatile Optimized Intelligent Dialogue."

    elif "creator" in msg or "who created you" in msg:
        return (
            "I was created by a group of Devs:\n\n"
            "#India\n"
            "@Kolkata Model School (Owner / Backend Dev)\n\n"
            "#Indonesia\n"
            "@Roan (Backend Dev)\n\n"
            "#Ukraine\n"
            "@Yuvi (Logic Handler)\n\n"
            "#America\n"
            "@Lisa (UI Dev)\n"
            "@Emma (UI Dev)"
        )

    elif "version" in msg:
        return "You're chatting with V.O.I.D version 3.0 🚀"

    return None
