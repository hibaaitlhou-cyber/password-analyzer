def generate_feedback(analysis_results: dict) -> dict:
    """
    Generates a score, strength rating, and feedback messages
    based on the analysis results.
    """
    score = 0
    feedback_messages = []

    # Check each criteria. If true, increase score. If false, add a suggestion.
    if analysis_results["length"]:
        score += 1
    else:
        feedback_messages.append("Password is too short. Use at least 8 characters.")

    if analysis_results["uppercase"]:
        score += 1
    else:
        feedback_messages.append("Add at least one uppercase letter (A-Z).")

    if analysis_results["lowercase"]:
        score += 1
    else:
        feedback_messages.append("Add at least one lowercase letter (a-z).")

    if analysis_results["number"]:
        score += 1
    else:
        feedback_messages.append("Add at least one number (0-9).")

    if analysis_results["special"]:
        score += 1
    else:
        feedback_messages.append("Add at least one special character (e.g., !@#$%^&*).")

    # Determine overall strength based on the score (0 to 5)
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "messages": feedback_messages
    }
