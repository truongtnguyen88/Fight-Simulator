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
    if request.method == "POST":
        fighter1_name = request.form["fighter1_name"]
        fighter1_age = int(request.form["fighter1_age"])
        fighter1_weight = float(request.form["fighter1_weight"])
        fighter1_bitch_energy = int(request.form["fighter1_bitch_energy"])

        fighter2_name = request.form["fighter2_name"]
        fighter2_age = int(request.form["fighter2_age"])
        fighter2_weight = float(request.form["fighter2_weight"])
        fighter2_bitch_energy = int(request.form["fighter2_bitch_energy"])

        # Avatar choice based on the random number
        avatar1 = "avatar1.jpg" if random.choice([True, False]) else "avatar2.jpg"
        avatar2 = "avatar1.jpg" if random.choice([True, False]) else "avatar2.jpg"

        fighter1 = {
            "name": fighter
