
from flask import Flask, render_template

app =Flask(__name__)

@app.route("/")
def home():

    return  render_template('index.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/detail")
def dashboard():
    return render_template('detail.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')
@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/register")
def register():
    return render_template('register.html')
@app.route("/basmatirice")
def rice():
    return render_template('basmatirice.html')
@app.route("/bread")
def bread():
    return render_template('bread.html')

@app.route("/pasta")
def pasta():
    return render_template('pasta.html')
@app.route("/grapes")
def grapes():
    return render_template('grapes.html')
@app.route("/cucumber")
def cucumber():
    return render_template('cucumber.html')

@app.route("/potato")
def potato():
    return render_template('potato.html')

@app.route("/milk")
def milk():
    return render_template('milk.html')

@app.route("/strawberry")
def strawberry():
    return render_template('strawberry.html')

@app.route("/onion")
def onion():
    return render_template('onion.html')

@app.route("/thankyou")
def thanku():
    return render_template('thankyou.html')

app.run(debug=True)

