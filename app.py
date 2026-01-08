from flask import Flask, render_template, request

app = Flask(__name__)

company = {
    'name': 'FurryCompany',
    'slogan': 'Мы команда mama twoya',
    'description': 'Ми FurryCompany, ми робимо Фурсьюти',
    'email': 'furryCompanySupport@furaffinity.net',
    'phone': '+380 67 451 61 67',
    'city': 'Zhytomyr, Ukraine'
}


@app.route('/')
def home():
    return render_template("home.html", company=company, active_page="home")


@app.route('/about')
def about():
    return render_template("about.html", company=company, active_page="about")


@app.route('/services')
def services():
    return render_template("services.html", company=company, active_page="services")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", company=company, active_page="portfolio")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = None
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        text = request.form.get("message")

        if not name or not email or not text:
            error = "заповніть ім'я, email та повідомлення"
        else:
            message = "Заявка прийнята!"

    return render_template(
        "contacts.html",
        company=company,
        active_page="contacts",
        message=message,
        error=error
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", company=company), 404


if __name__ == "__main__":
    app.run(debug=True)
