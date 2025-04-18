from flask import Flask, request, render_template


def kg_lb(x):
    return x * 2.20462

def lb_kg(x):
    return x / 2.20462

def cm_in(x):
    return x / 2.54

def in_cm(x):
    return x * 2.54

def metre_foot(x):
    return x * 3.28084

def foot_metre(x):
    return x / 3.28084

def gal_l(x):
    return x * 3.78541

def l_gal(x):
    return x / 3.78541

def ounce_g(x):
    return x * 28.3495

def g_ounce(x):
    return x / 28.3495

def cup_ml(x):
    return x * 250

def ml_cup(x):
    return x / 250

def mile_km(x):
    return x * 1.60934

def km_mile(x):
    return x / 1.60934

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def unit_converter():
    result = None
    unit = None

    if request.method == "POST":
        unit = request.form["unit"]
        try:
            if unit == "kg_lb":
                num = float(request.form["num"])
                result = kg_lb(num)

            elif unit == "lb_kg":
                num = float(request.form["num"])
                result = lb_kg(num)

            elif unit == "cm_in":
                num = float(request.form["num"])
                result = cm_in(num)

            elif unit == "in_cm":
                num = float(request.form["num"])
                result = in_cm(num)

            elif unit == "metre_foot":
                num = float(request.form["num"])
                result = metre_foot(num)

            elif unit == "foot_metre":
                num = float(request.form["num"])
                result = foot_metre(num)

            elif unit == "gal_l":
                num = float(request.form["num"])
                result = gal_l(num)

            elif unit == "l_gal":
                num = float(request.form["num"])
                result = l_gal(num)

            elif unit == "ounce_g":
                num = float(request.form["num"])
                result = ounce_g(num)

            elif unit == "g_ounce":
                num = float(request.form["num"])
                result = g_ounce(num)

            elif unit == "cup_ml":
                num = float(request.form["num"])
                result = cup_ml(num)

            elif unit == "ml_cup":
                num = float(request.form["num"])
                result = ml_cup(num)

            elif unit == "mile_km":
                num = float(request.form["num"])
                result = mile_km(num)

            elif unit == "km_mile":
                num = float(request.form["num"])
                result = km_mile(num)

            result = round(result, 2)

        except (ValueError, KeyError, TypeError):
            "Please enter all required fields."

    return render_template("unit_converter.html", result=result, unit=unit)

if __name__ == "__main__":
    app.run(debug=True)
