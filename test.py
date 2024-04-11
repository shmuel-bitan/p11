import requests

# Liste des emails à tester
emails = [
    "john@simplylift.co",
    "admin@irontemple.com",
    "kate@shelifts.co.uk",
    "nonexistent@example.com"  # Ajoute un email inexistant pour tester le message d'erreur
]

# URL de l'application Flask
base_url = 'http://localhost:5000/showSummary'

# Parcourir chaque email et envoyer une requête POST à l'application Flask
for email in emails:
    data = {'email': email}
    response = requests.post(base_url, data=data)
    print(f"Email: {email}, Response: {response.status_code}")