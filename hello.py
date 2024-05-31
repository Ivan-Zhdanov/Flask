from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    first_name = 'John'
    pizza = ['Peperoni', '4 cheese', 'American']
    return render_template("index.html", pizza=pizza)


# localhost:5000/users/Ivan
@app.route('/users')
def users():
    return render_template("users.html")


# Создание обработки страниц ошибок
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_err(e):
    return render_template("500.html"), 500




if __name__ == "__main__":
    app.run(debug=True)