def job_reflection_agent(applied, practiced, learned, updated_profile, studied, practiced_problems, reason=None):
    
    valid_inputs = ["yes", "no"]

    if applied not in valid_inputs:
        return "Invalid input for 'applied'. Use 'yes' or 'no'."

    if applied == "yes":
        if practiced == "yes":
            if learned == "yes":
                return "Excellent progress day 🚀"
            else:
                return "Good, but add learning for growth"
        else:
            if updated_profile == "yes":
                return "Strong preparation strategy"
            else:
                return "Applied but lacking skill practice and profile updates"

    else:
        if studied == "yes":
            if practiced_problems == "yes":
                return "Learning-focused day 👍"
            else:
                return "Convert learning into practice"
        else:
            if reason == "time":
                return "Improve time management"
            elif reason == "motivation":
                return "Set small daily goals"
            elif reason == "distraction":
                return "Reduce distractions"
            else:
                return "No clear reason provided"


# Example run
print(job_reflection_agent("no", "no", "no", "no", "yes", "no"))
