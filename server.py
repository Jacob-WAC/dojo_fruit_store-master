from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    amount = int(request.form["strawberry"]) + \
        int(request.form["raspberry"]) + int(request.form["apple"])
    print(
        f'Charging {request.form["first_name"]} {request.form["last_name"]} for {amount} fruits')
    return render_template("checkout.html", strawberry=request.form["strawberry"], raspberry=request.form["raspberry"], apple=request.form["apple"], firstName=request.form["first_name"], lastName=request.form["last_name"], idNum=request.form["student_id"])


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
