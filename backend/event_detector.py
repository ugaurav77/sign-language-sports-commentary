def detect_event(text):

    text = text.lower()

    if "six" in text:
        return "SIX"

    if "four" in text:
        return "FOUR"

    if "wicket" in text or "out" in text:
        return "WICKET"

    if "goal" in text:
        return "GOAL"

    return None