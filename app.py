from flask import Flask, render_template, request
import random

app = Flask(__name__)

def calculate_score(age, weight, bitch_energy):
    # Normalize each stat
    stamina_score = max(100 - abs(30 - age) * 2, 10)  # Best age ~30
    power_score = weight * 0.5  # More weight = more power
    bitch_energy_score = bitch_energy * 10  # Direct boost

    total = stamina_score + power_score + bitch_energy_score
    return total

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    avatar1 = avatar2 = None

    if request.method == "POST":
        # Fighter 1 data
        fighter1_name = request.form["fighter1_name"]
        fighter1_age = int(request.form["fighter1_age"])
        fighter1_weight = float(request.form["fighter1_weight"])
        fighter1_bitch_energy = int(request.form["fighter1_bitch_energy"])

        # Fighter 2 data
        fighter2_name = request.form["fighter2_name"]
        fighter2_age = int(request.form["fighter2_age"])
        fighter2_weight = float(request.form["fighter2_weight"])
        fighter2_bitch_energy = int(request.form["fighter2_bitch_energy"])

        # Assign avatars
        avatar1 = random.choice(["avatar1.jpg", "avatar2.jpg"])
        avatar2 = random.choice(["avatar1.jpg", "avatar2.jpg"])

        # Create fighter data dictionaries
        fighter1 = {
            "name": fighter1_name,
            "age": fighter1_age,
            "weight": fighter1_weight,
            "bitch_energy": fighter1_bitch_energy
        }

        fighter2 = {
            "name": fighter2_name,
            "age": fighter2_age,
            "weight": fighter2_weight,
            "bitch_energy": fighter2_bitch_energy
        }

        # Calculate fight results
        score1 = calculate_score(fighter1["age"], fighter1["weight"], fighter1["bitch_energy"])
        score2 = calculate_score(fighter2["age"], fighter2["weight"], fighter2["bitch_energy"])

        if abs(score1 - score2) < 10:
            result = "It was a savage, close battle..."
        if score1 > score2:
            result = f"{fighter1['name']} wins with unmatched bitch energy!"
        elif score2 > score1:
            result = f"{fighter2['name']} wins with supreme bitch energy!"
        else:
            result = "It's a draw! The crowd goes wild!"

        return render_template("index.html",
                               fighter1=fighter1,
                               fighter2=fighter2,
                               avatar1=avatar1,
                               avatar2=avatar2,
                               result=result)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
