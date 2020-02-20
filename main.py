import waitress
import app

waitress.serve(app.app, port=8080, url_scheme='https')