from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_score(age, weight_lbs, bitch_energy):
    stamina_score = max(100 - abs(30 - age) * 2, 10)
    power_score = weight_lbs * 0.23
    bitch_energy_score = bitch_energy * 10
    return stamina_score + power_score + bitch_energy_score

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fight', methods=['POST'])
def fight():
    fighter1_name = request.form['name1']
    fighter1_age = int(request.form['age1'])
    fighter1_weight = float(request.form['weight1'])
    fighter1_be = int(request.form['be1'])

    fighter2_name = request.form['name2']
    fighter2_age = int(request.form['age2'])
    fighter2_weight = float(request.form['weight2'])
    fighter2_be = int(request.form['be2'])

    score1 = calculate_score(fighter1_age, fighter1_weight, fighter1_be)
    score2 = calculate_score(fighter2_age, fighter2_weight, fighter2_be)

    if abs(score1 - score2) < 10:
        result = "It was a savage, close battle..."
    elif score1 > score2:
        result = f"{fighter1_name} wins with unmatched bitch energy!"
    else:
        result = f"{fighter2_name} wins with supreme bitch energy!"

    return render_template('result.html',
                           result=result,
                           fighter1=fighter1_name,
                           fighter2=fighter2_name,
                           score1=round(score1, 1),
                           score2=round(score2, 1))

if __name__ == '__main__':
    app.run(debug=True)
