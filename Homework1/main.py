from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/clothes/")
def clothes():
    clothes_list = [
        {
            "photo": "https://standard.gdebirka.ru/pi/manshortfull/500/29/p2946725.webp",
            "name": "футболка",
            "cost": 15000,
        },
        {
            "photo": "https://img.printfact.ru/image/big/women/hudi-pivozavr-black-gmow0ba.jpg",
            "name": "худи",
            "cost": 20000,
        },
    ]
    return render_template("clothes.html", clothes_list=clothes_list)


@app.route("/jackets/")
def jackets():
    jacket_list = [
        {
            "photo": "https://profi-overalls.ru/public_files/images/products/2098/12121jpeg.jpeg",
            "name": "кутка_1",
            "cost": 5000,
        },
        {
            "photo": "https://st24.stpulscen.ru/images/product/221/298/265_original.jpg",
            "name": "кутка_2",
            "cost": 10000,
        },
    ]
    return render_template("jackets.html", jacket_list=jacket_list)


@app.route("/shoes/")
def shoes():
    shoes_list = [
        {
            "photo": "https://www.yavmode.ru/wp-content/uploads/2014/01/valenki-5.jpg",
            "name": "обувь_1",
            "cost": 3500,
        },
        {
            "photo": "https://ck152.ru/wp-content/uploads/2019/07/sapogi-EVA-bolotnye.jpeg",
            "name": "обувь_2",
            "cost": 8000,
        },
    ]
    return render_template("shoes.html", shoes_list=shoes_list)


if __name__ == "__main__":
    app.run(debug=True)