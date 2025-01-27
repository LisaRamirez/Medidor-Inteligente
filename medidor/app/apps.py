from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mapa():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
