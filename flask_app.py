from flask import Flask, render_template
import requests

app = Flask(__name__)

# L'URL de l'API qu'on va tester
API_URL = "https://api.quotable.io/random"

@app.route('/')
def home():
    try:
        # On tente d'appeler l'API
        response = requests.get(API_URL, timeout=5)
        
        # Si le code est 200, l'API est en ligne (UP)
        if response.status_code == 200:
            status = "UP ✅"
            data = response.json()
            message = f"Citation du moment : {data['content']} — {data['author']}"
        else:
            status = f"DOWN ❌ (Code: {response.status_code})"
            message = "L'API répond mais avec une erreur."
            
    except Exception as e:
        # Si on n'arrive même pas à joindre l'API
        status = "DOWN ❌"
        message = f"Erreur de connexion : {str(e)}"

    return render_template('index.html', status=status, message=message)

if __name__ == '__main__':
    app.run(debug=True)
