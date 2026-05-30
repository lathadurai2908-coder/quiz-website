from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rishmesh_2009",
    database="quizdb"
)

cursor = db.cursor()

@app.route("/")
def home():

    current_hour = datetime.now().hour

    if 21 <= current_hour < 24:
        return """
        <h1>Quiz is closed.</h1>

        <p>The quiz is available from 12:00 AM to 8:59 PM.</p>

        <a href="/leaderboard">View Leaderboard</a>
        """

    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]

    score = 0
    correct_answers = 0
    wrong_answers = 0
    answers_unattempted = 0

    q1 = request.form.get("q1")

    if q1 == "D":
        score += 4
        correct_answers += 1
    elif q1 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q2 = request.form.get("q2")

    if q2 == "B":
        score += 4
        correct_answers += 1
    elif q2 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q3 = request.form.get("q3")

    if q3 == "B":
        score += 4
        correct_answers += 1
    elif q3 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q4 = request.form.get("q4")

    if q4 == "C":
        score += 4
        correct_answers += 1
    elif q4 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q5 = request.form.get("q5")

    if q5 == "C":
        score += 4
        correct_answers += 1
    elif q5 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q6 = request.form.get("q6")

    if q6 == "B":
        score += 4
        correct_answers += 1
    elif q6 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q7 = request.form.get("q7")

    if q7 == "C":
        score += 4
        correct_answers += 1
    elif q7 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q8 = request.form.get("q8")

    if q8 == "A":
        score += 4
        correct_answers += 1
    elif q8 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q9 = request.form.get("q9")

    if q9 == "C":
        score += 4
        correct_answers += 1
    elif q9 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q10 = request.form.get("q10")

    if q10 == "B":
        score += 4
        correct_answers += 1
    elif q10 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q11 = request.form.get("q11")

    if q11 == "D":
        score += 4
        correct_answers += 1
    elif q11 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q12 = request.form.get("q12")

    if q12 == "C":
        score += 4
        correct_answers += 1
    elif q12 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q13 = request.form.get("q13")

    if q13 == "B":
        score += 4
        correct_answers += 1
    elif q13 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q14 = request.form.get("q14")

    if q14 == "C":
        score += 4
        correct_answers += 1
    elif q14 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q15 = request.form.get("q15")

    if q15 == "D":
        score += 4
        correct_answers += 1
    elif q15 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q16 = request.form.get("q16")

    if q16 == "B":
        score += 4
        correct_answers += 1
    elif q16 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q17 = request.form.get("q17")

    if q17 == "C":
        score += 4
        correct_answers += 1
    elif q17 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q18 = request.form.get("q18")

    if q18 == "B":
        score += 4
        correct_answers += 1
    elif q18 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q19 = request.form.get("q19")

    if q19 == "B":
        score += 4
        correct_answers += 1
    elif q19 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q20 = request.form.get("q20")

    if q20 == "C":
        score += 4
        correct_answers += 1
    elif q20 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q21 = request.form.get("q21")

    if q21 == "B":
        score += 4
        correct_answers += 1
    elif q21 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q22 = request.form.get("q22")

    if q22 == "C":
        score += 4
        correct_answers += 1
    elif q22 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q23 = request.form.get("q23")

    if q23 == "C":
        score += 4
        correct_answers += 1
    elif q23 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q24 = request.form.get("q24")

    if q24 == "C":
        score += 4
        correct_answers += 1
    elif q24 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q25 = request.form.get("q25")

    if q25 == "C":
        score += 4
        correct_answers += 1
    elif q25 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q26 = request.form.get("q26")

    if q26 == "B":
        score += 4
        correct_answers += 1
    elif q26 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q27 = request.form.get("q27")

    if q27 == "C":
        score += 4
        correct_answers += 1
    elif q27 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q28 = request.form.get("q28")

    if q28 == "D":
        score += 4
        correct_answers += 1
    elif q28 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q29 = request.form.get("q29")

    if q29 == "B":
        score += 4
        correct_answers += 1
    elif q29 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    q30 = request.form.get("q30")

    if q30 == "A":
        score += 4
        correct_answers += 1
    elif q30 is None:
        score += 0
        answers_unattempted += 1
    else:
        score -= 1
        wrong_answers += 1

    sql = """
    INSERT INTO leaderboard
    (name, marks, correct_answers, wrong_answers, attempt_time)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        name,
        score,
        correct_answers,
        wrong_answers,
        datetime.now()
    )

    cursor.execute(sql, values)

    db.commit()

    return f"""
    <h1>Quiz Submitted Successfully!</h1>

    Name: {name}<br><br>

    Total Marks: {score}<br><br>

    Correct Answers: {correct_answers}<br><br>

    Wrong Answers: {wrong_answers}<br><br>

    Unattempted Answers: {answers_unattempted}<br><br>

    <hr>

    <h2>Answer Key with Solutions</h2>

    <h3>Question 1</h3>

    Hydraulic brakes and Hydraulic lift are devices in which fluids are used for transmitting<br><br>

    A. Momentum<br>
    B. Power<br>
    C. Force<br>
    D. Pressure<br>

    Your Answer:
    {
    "A. Momentum" if q1=="A"
    else "B. Power" if q1=="B"
    else "C. Force" if q1=="C"
    else "D. Pressure" if q1=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    D. Pressure

    <br><br>

    Explanation:
    According to Pascal’s law, pressure applied to an enclosed fluid is transmitted equally in all directions.

    <hr>

    <h3>Question 2</h3>

    A perfect black body has the unique characteristic feature as<br><br>

    A. Neither an absorber nor radiator<br>
    B. A good absorber and a good radiator<br>
    C. A good radiator only<br>
    D. A good absorber only<br>

    Your Answer:
    {
    "A. Neither an absorber nor radiator" if q2=="A"
    else "B. A good absorber and a good radiator" if q2=="B"
    else "C. A good radiator only" if q2=="C"
    else "D. A good absorber only" if q2=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B.A good absorber and a good radiator

    <br><br>

    Explanation:
    A perfect black body absorbs all incident radiation and is also the best emitter.

    <hr>

    <h3>Question 3</h3>

    A particle moves in a central force field F(r). Which quantity is always conserved?<br><br>

    A. Linear Momentum<br>
    B. Angular Momentum<br>
    C. Mechanical Energy<br>
    D. Potential Energy<br>

    Your Answer:
    {
    "A. Linear Momentum" if q3=="A"
    else "B. Angular Momentum" if q3=="B"
    else "C. Mechanical Energy" if q3=="C"
    else "D. Potential Energy" if q3=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Angular Momentum

    <br><br>

    Explanation:
    Central forces act along the radius vector, so torque is zero and angular momentum is conserved.

    <hr>

    <h3>Question 4</h3>

    Which of the following quantities is conserved in an elastic collision?<br><br>

    A. Momentum only<br>
    B. Kinetic Energy only<br>
    C. Both Momentum and Kinetic Energy<br>
    D. Neither Momentum nor Kinetic Energy<br>

    Your Answer:
    {
    "A. Momentum only" if q4=="A"
    else "B. Kinetic Energy only" if q4=="B"
    else "C. Both Momentum and Kinetic Energy" if q4=="C"
    else "D. Neither Momentum nor Kinetic Energy" if q4=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Both Momentum and Kinetic Energy

    <br><br>

    Explanation:
    Elastic collisions conserve both linear momentum and kinetic energy.

    <hr>

    <h3>Question 5</h3>

    For a wave described by 𝑦(𝑥,𝑡)=𝐴sin(𝑘𝑥−𝜔𝑡), the phase velocity is:<br><br>

    A. 𝜔<br>
    B. 𝑘<br>
    C. 𝜔/𝑘<br>
    D. 𝑘/𝜔<br>

    Your Answer:
    {
    "A. 𝜔" if q5=="A"
    else "B. 𝑘" if q5=="B"
    else "C. 𝜔/𝑘" if q5=="C"
    else "D. 𝑘/𝜔" if q5=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. 𝜔/𝑘

    <br><br>

    Explanation:
    Given wave equation:
        y(x,t) = A sin(kx - ωt)

        Step 1: Phase of the wave is
        φ = kx - ωt

        Step 2: For a point of constant phase,
        kx - ωt = constant

        Step 3: Differentiate with respect to time:
        d/dt (kx - ωt) = 0

        k(dx/dt) - ω = 0

        Step 4: Solving for velocity:
        dx/dt = ω / k

        Hence, phase velocity is:
        v_p = ω / k

    <hr>

    <h3>Question 6</h3>

    A charged particle enters a uniform magnetic field with velocity perpendicular to the field. Its motion is:<br><br>

    A. Linear with constant speed<br>
    B. Circular with constant speed<br>
    C. Spiral with increasing radius<br>
    D. Spiral with decreasing radius<br>

    Your Answer:
    {
    "A. Linear with constant speed" if q6=="A"
    else "B. Circular with constant speed" if q6=="B"
    else "C. Spiral with increasing radius" if q6=="C"
    else "D. Spiral with decreasing radius" if q6=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Circular with constant speed

    <br><br>

    Explanation:
    The magnetic force is always perpendicular to the velocity, acting as a centripetal force. Since speed remains constant and only direction changes, the particle moves in a uniform circular path.

    <hr>

    <h3>Question 7</h3>

    What phenomenon explains why a pencil appears bent when placed in water?<br><br>

    A. Reflection<br>
    B. Diffraction<br>
    C. Refraction<br>
    D. Interference<br>

    Your Answer:
    {
    "A. Reflection" if q7=="A"
    else "B. Diffraction" if q7=="B"
    else "C. Refraction" if q7=="C"
    else "D. Interference" if q7=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Refraction

    <br><br>

    Explanation:
    Light changes direction when it passes from air to water due to a change in speed. This bending of light is called refraction, making the pencil appear bent.

    <hr>

    <h3>Question 8</h3>

    Which law states that the pressure exerted by a gas is inversely proportional to its volume at constant temperature?<br><br>

    A. Boyle's Law<br>
    B. Charles's Law<br>
    C. Newton's Law<br>
    D. Hooke's Law<br>

    Your Answer:
    {
    "A. Boyle's Law" if q8=="A"
    else "B. Charle's Law" if q8=="B"
    else "C. Newton's Law" if q8=="C"
    else "D. Hooke's Law" if q8=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    A. Boyle's Law

    <br><br>

    Explanation:
    According to Boyle’s Law, 𝑃 ∝1/𝑉 for a fixed mass of gas at constant temperature.

    <hr>

    <h3>Question 9</h3>

    Which Maxwell equation implies that a changing magnetic field induces an electric field?<br><br>

    A. Gauss's Law<br>
    B. Gauss's Law for Magnetism<br>
    C. Faraday's Law<br>
    D. Ampere-Maxwell Law<br>

    Your Answer:
    {
    "A. Gauss's Law" if q9=="A"
    else "B. Gauss's Law for Magnetism" if q9=="B"
    else "C. Faraday's Law" if q9=="C"
    else "D. Ampere-Maxwell Law" if q9=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Faraday's Law

    <br><br>

    Explanation:
    Faraday’s law of electromagnetic induction states that a time-varying magnetic field produces an electric field.

    <hr>

    <h3>Question 10</h3>

    The gravitational potential inside a uniform spherical shell is:<br><br>

    A. Zero everywhere<br>
    B. Constant everywhere but non-zero<br>
    C. Inversely proportional to the distance from the center<br>
    D. Directly proportional to the distance from the center<br>

    Your Answer:
    {
    "A. Zero everywhere" if q10=="A"
    else "B. Constant everywhere but non-zero" if q10=="B"
    else "C. Inversely proportional to the distance from the center" if q10=="C"
    else "D. Directly proportional to the distance from the center" if q10=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Constant everywhere but non-zero

    <br><br>

    Explanation:
    Inside a hollow spherical shell, gravitational field is zero, so the gravitational potential remains constant (negative) throughout the interior.

    <hr>

    <h3>Question 11</h3>

    Which of the following has the highest first ionization energy?<br><br>

    A. Na<br>
    B. Mg<br>
    C. Al<br>
    D. Si<br>

    Your Answer:
    {
    "A. Na" if q11=="A"
    else "B. Mg" if q11=="B"
    else "C. Al" if q11=="C"
    else "D. Si" if q11=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    D. Si

    <br><br>

    Explanation:
    Ionization energy increases across a period; Si is highest among given options.

    <hr>

    <h3>Question 12</h3>

    What is the hybridization of the central atom in SF₆?<br><br>

    A. sp³<br>
    B. sp³d<br>
    C. sp³d²<br>
    D. sp²<br>

    Your Answer:
    {
    "A. sp³" if q12=="A"
    else "B. sp³d" if q12=="B"
    else "C. sp³d²" if q12=="C"
    else "D. sp²" if q12=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. sp³d²

    <br><br>

    Explanation:
    SF₆ has six σ bonds → octahedral geometry.

    <hr>

    <h3>Question 13</h3>

    Which compound exhibits hydrogen bonding between its molecules?<br><br>

    A. CH₄<br>
    B. NH₃<br>
    C. H₂S<br>
    D. PH₃<br>

    Your Answer:
    {
    "A. CH₄" if q13=="A"
    else "B. NH₃" if q13=="B"
    else "C. H₂S" if q13=="C"
    else "D. PH₃" if q13=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. NH₃

    <br><br>

    Explanation:
    N–H bonds enable hydrogen bonding.

    <hr>

    <h3>Question 14</h3>

    What is the oxidation number of sulfur in H₂SO₄?<br><br>

    A. +4<br>
    B. +5<br>
    C. +6<br>
    D. +8<br>

    Your Answer:
    {
    "A. +4" if q14=="A"
    else "B. +5" if q14=="B"
    else "C. +6" if q14=="C"
    else "D. +8" if q14=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. +6

    <br><br>

    Explanation:
    Oxidation number of sulfur in H₂SO₄ is +6.

    <hr>

    <h3>Question 15</h3>

    Which factor does NOT affect the rate of a chemical reaction?<br><br>

    A. Temperature<br>
    B. Concentration<br>
    C. Catalyst<br>
    D. Enthalpy Change<br>

    Your Answer:
    {
    "A. Temperature" if q15=="A"
    else "B. Concentration" if q15=="B"
    else "C. Catalyst" if q15=="C"
    else "D. Enthalpy Change" if q15=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    D. Enthalpy Change

    <br><br>

    Explanation:
    Rate depends on temperature, concentration, catalyst—not ΔH.

    <hr>

    <h3>Question 16</h3>

    In an electrochemical cell, oxidation occurs at the:<br><br>

    A. Cathode<br>
    B. Anode<br>
    C. Salt Bridge<br>
    D. Electrolyte<br>

    Your Answer:
    {
    "A. Cathode" if q16=="A"
    else "B. Anode" if q16=="B"
    else "C. Salt Bridge" if q16=="C"
    else "D. Electrolyte" if q16=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Anode

    <br><br>

    Explanation:
    Oxidation always occurs at the anode.

    <hr>

    <h3>Question 17</h3>

    Which species acts as both a Bronsted–Lowry acid and base?<br><br>

    A. HCl<br>
    B. NH₄⁺<br>
    C. H₂O<br>
    D. NaOH<br>

    Your Answer:
    {
    "A. HCl" if q17=="A"
    else "B. NH₄⁺" if q17=="B"
    else "C. H₂O" if q17=="C"
    else "D. NaOH" if q17=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. H₂O

    <br><br>

    Explanation:
    H₂O can act as both acid and base (amphoteric).

    <hr>

    <h3>Question 18</h3>

    What is the shape of the ClF₃ molecule according to VSEPR theory?<br><br>

    A. Trigonal Planar<br>
    B. T-shaped<br>
    C. Trigonal Bipyramidal<br>
    D. Linear<br>

    Your Answer:
    {
    "A. Trigonal Planar" if q18=="A"
    else "B. T-shaped" if q18=="B"
    else "C. Trigonal Bipyramidal" if q18=="C"
    else "D. Linear" if q18=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. T-shaped

    <br><br>

    Explanation:
    ClF₃ has 3 bonds and 2 lone pairs (VSEPR).

    <hr>

    <h3>Question 19</h3>

    Which law explains the relationship between gas volume and temperature at constant pressure?<br><br>

    A. Boyle's Law<br>
    B. Charles's Law<br>
    C. Avogadro's Law<br>
    D. Dalton's Law<br>

    Your Answer:
    {
    "A. Boyle's Law" if q19=="A"
    else "B. Charles's Law" if q19=="B"
    else "C. Avogadro's Law" if q19=="C"
    else "D. Dalton's Law" if q19=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Charles's Law

    <br><br>

    Explanation:
    Volume ∝ Temperature at constant pressure.

    <hr>

    <h3>Question 20</h3>

    Which of the following complexes will show geometrical isomerism?<br><br>

    A. [Ag(NH₃)₂]⁺<br>
    B. [Fe(CN)₆]³⁻<br>
    C. [Pt(NH₃)₂Cl₂]<br>
    D. [Zn(OH)₄]²⁻<br>

    Your Answer:
    {
    "A. [Ag(NH₃)₂]⁺" if q20=="A"
    else "B. [Fe(CN)₆]³⁻" if q20=="B"
    else "C. [Pt(NH₃)₂Cl₂]" if q20=="C"
    else "D. [Zn(OH)₄]²⁻" if q20=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. [Pt(NH₃)₂Cl₂]

    <br><br>

    Explanation:
    Square planar complex shows cis–trans isomerism.

    <hr>

    <h3>Question 21</h3>

    The Treaty of Tordesillas (1494) divided newly discovered lands between which two countries?<br><br>

    A. Spain and France<br>
    B. Spain and Portugal<br>
    C. England and Spain<br>
    D. Portugal and Netherlands<br>

    Your Answer:
    {
    "A. Spain and France" if q21=="A"
    else "B. Spain and Portugal" if q21=="B"
    else "C. England and Spain" if q21=="C"
    else "D. Portugal and Netherlands" if q21=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Spain and Portugal

    <br><br>

    Explanation:
    The Treaty of Tordesillas (1494) divided newly discovered lands between Spain and Portugal.

    <hr>

    <h3>Question 22</h3>

    The Chabahar Port, strategically important to India, is located in:<br><br>

    A. Iraq<br>
    B. Oman<br>
    C. Iran<br>
    D. Yemen<br>

    Your Answer:
    {
    "A. Iraq" if q22=="A"
    else "B. Oman" if q22=="B"
    else "C. Iran" if q22=="C"
    else "D. Yemen" if q22=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Iran

    <br><br>

    Explanation:
    Chabahar Port is in Iran.

    <hr>

    <h3>Question 23</h3>

    Which of the following is NOT a Fundamental Duty under the Indian Constitution?<br><br>

    A. To safeguard public property<br>
    B. To promote harmony<br>
    C. To vote in elections<br>
    D. To protect the environment<br>

    Your Answer:
    {
    "A. To safeguard public property" if q23=="A"
    else "B. To promote harmony" if q23=="B"
    else "C. To vote in elections" if q23=="C"
    else "D. To protect the environment" if q23=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. To vote in elections

    <br><br>

    Explanation:
    Voting is a right, not a Fundamental Duty.

    <hr>

    <h3>Question 24</h3>

    The unit “Henry” is related to the measurement of:<br><br>

    A. Capacitance<br>
    B. Resistance<br>
    C. Inductance<br>
    D. Magnetic Flux<br>

    Your Answer:
    {
    "A. Capacitance" if q24=="A"
    else "B. Resistance" if q24=="B"
    else "C. Inductance" if q24=="C"
    else "D. Magnetic Flux" if q24=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Inductance

    <br><br>

    Explanation:
    Henry is the SI unit of inductance.

    <hr>

    <h3>Question 25</h3>

    Who among the following wrote Arthashastra?<br><br>

    A. Painini<br>
    B. Kalidasa<br>
    C. Chanakya<br>
    D. Patanjali<br>

    Your Answer:
    {
    "A. Panini" if q25=="A"
    else "B. Kalidasa" if q25=="B"
    else "C. Chanakya" if q25=="C"
    else "D. Patanjali" if q25=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Chanakya

    <br><br>

    Explanation:
    Author of Arthashastra is Chanakya.

    <hr>

    <h3>Question 26</h3>

    Which country first introduced paper currency?<br><br>

    A. India<br>
    B. China<br>
    C. Persia<br>
    D. Greece<br>

    Your Answer:
    {
    "A. India" if q26=="A"
    else "B. China" if q26=="B"
    else "C. Persia" if q26=="C"
    else "D. Greece" if q26=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. China

    <br><br>

    Explanation:
    First country to introduce paper currency is China.

    <hr>

    <h3>Question 27</h3>

    The Kyoto Protocol is related to which global issue?<br><br>

    A. Nuclear Disarmament<br>
    B. Biodiversity Conservation<br>
    C. Climate Change<br>
    D. Ozone Depletion<br>

    Your Answer:
    {
    "A. Nuclear Disarmament" if q27=="A"
    else "B. Biodiversity Conservation" if q27=="B"
    else "C. Climate Change" if q27=="C"
    else "D. Ozone Depletion" if q27=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    C. Climate Change

    <br><br>

    Explanation:
    Kyoto Protocol targets greenhouse gas reduction.

    <hr>

    <h3>Question 28</h3>

    Which vitamin is water-soluble?<br><br>

    A. Vitamin A<br>
    B. Vitamin D<br>
    C. Vitamin E<br>
    D. Vitamin C<br>

    Your Answer:
    {
    "A. Vitamin A" if q28=="A"
    else "B. Vitamin D" if q28=="B"
    else "C. Vitamin E" if q28=="C"
    else "D. Vitamin C" if q28=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    D. Vitamin C

    <br><br>

    Explanation:
    Water-soluble vitamin is Vitamin C.

    <hr>

    <h3>Question 29</h3>

    The term “Blue Economy” is associated with:<br><br>

    A. Space Exploration<br>
    B. Marine Resources and Sustainability<br>
    C. Renewable Energy<br>
    D. Digital Economy<br>

    Your Answer:
    {
    "A. Space Exploration" if q29=="A"
    else "B. Marine Resources and Sustainability" if q29=="B"
    else "C. Renewable Energy" if q29=="C"
    else "D. Digital Economy" if q29=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    B. Marine Resources and Sustainability

    <br><br>

    Explanation:
    The term Blue Economy is associated with Marine Resources and Sustainability.

    <hr>

    <h3>Question 30</h3>

    Who was the first non-European to win a Nobel Prize?<br><br>

    A. Rabindranath Tagore<br>
    B. C.V.Raman<br>
    C. Mother Teresa<br>
    D. Homi Bhabha<br>

    Your Answer:
    {
    "A. Rabindranath Tagore" if q30=="A"
    else "B. C.V.Raman" if q30=="B"
    else "C. Mother Teresa" if q30=="C"
    else "D. Homi Bhabha" if q30=="D"
    else "Not Attempted"
    }

    <br><br>

    Correct Answer:
    A. Rabindranath Tagore

    <br><br>

    Explanation:
    First non-European Nobel laureate (1913) is Rabindranath Tagore.

    <br><br>

    <a href="/leaderboard">View Leaderboard</a>


    """

@app.route("/leaderboard")
def leaderboard():

    current_hour = datetime.now().hour

    if current_hour < 21 or current_hour >= 24:
        return """
        <h1>Leaderboard is available only from 9 PM to 12 AM</h1>
        """

    cursor.execute("""
    SELECT name, marks, correct_answers, wrong_answers
    FROM leaderboard
    ORDER BY marks DESC
    """)

    data = cursor.fetchall()

    output = """

    <h1>Leaderboard</h1>

    <table border=1 cellpadding=10>

    <tr>
        <th>Rank</th>
        <th>Name</th>
        <th>Marks</th>
        <th>Correct Answers</th>
        <th>Wrong Answers</th>
    </tr>

    """

    rank = 1

    for row in data:

        output += f"""

        <tr>
            <td>{rank}</td>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
        </tr>

        """

        rank += 1

    output += "</table>"

    return output
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)