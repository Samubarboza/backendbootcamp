from flask import Flask, render_template, request, redirect
import requests
import os

from models import db
from models import Favorite

# instancia Flask
app = Flask(__name__)

# BASE_DIR guarda la ruta absoluta de la carpeta donde está este archivo (.py)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DB_PATH (usando BASE_DIR) construye la ruta completa al archivo de la base de datos (app.db)
DB_PATH = os.path.join(BASE_DIR, "instance", "app.db")

# le decimos a flask + alchemy donde esta la base de datos sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
# desactivamos seguimiento interno para no consumir recursos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

API_URL = "https://rickandmortyapi.com/api/character"

# ruta principal
@app.route("/")
def index():
    page = request.args.get("page", 1)
    # aca comienza la logica de la busqueda de personajes. si hay tiempo agregamos
    name = request.args.get("name")

    # Si hay búsqueda → no paginamos
    if name:
        response = requests.get(API_URL, params={"name": name})
        if response.status_code != 200:
            return render_template("index.html", characters=[], search=True, error_message="Personaje no encontrado")
        data = response.json()
        return render_template("index.html", characters=data["results"], search=True)

    # Listado normal con paginación
    response = requests.get(API_URL, params={"page": page})
    data = response.json()

    return render_template("index.html", characters=data["results"], info=data["info"], page=int(page), search=False)


# ruta para guardar personajes a la db
@app.route("/save", methods=["POST"])
def save():
    api_id = request.form["api_id"]
    name = request.form["name"]
    image = request.form["image"]

    if not Favorite.query.filter_by(api_id=api_id).first():
        fav = Favorite(api_id=api_id, name=name, image=image)
        db.session.add(fav)
        db.session.commit()

    return redirect("/")

        

# ruta de los peronajes favoritos que se guardan en la base de datios
@app.route("/favorites")
def favorites():
    favorites = Favorite.query.all()
    return render_template("favorites.html", favorites=favorites)


# ruta eliminar personajes
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    fav = Favorite.query.get(id)
    if fav:
        db.session.delete(fav)
        db.session.commit()
    return redirect("/favorites")


if __name__ == "__main__":
    app.run(debug=True)
