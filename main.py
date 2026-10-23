from pyscript import document

def candidate_checker(e):
    club_members = {
        "lexie uaje",
        "kyle delacalzada",
        "angelica delrosario",
        "millicent meneses",
        "aaron deguzman",
        "river datiles",
        "gilliah tabaldo",
    }

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate = f"{first_name} {last_name}".strip()

    if candidate.lower() in club_members:
        message = f"Congratulations, {candidate}! You are a member of the Marching Band."
    else:
        message = f"Sorry, {candidate}. Your name is not on the list."

    document.getElementById("result").innerText = message

