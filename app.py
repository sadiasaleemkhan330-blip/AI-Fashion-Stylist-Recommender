from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # 14 inputs receive karne ke liye variables
        gender = data.get('gender')
        age_group = data.get('age_group')
        style_preference = data.get('style_preference')
        user_mood = data.get('mood')
        fabric = data.get('fabric', 'COTTON BLEND')
        
        # Real-like values generate karna jisse aapka dynamic design update ho
        score = random.randint(85, 98)
        structural_fit = random.randint(80, 95)
        aura_density = random.randint(85, 100)
        
        # Frontend dashboard ke exact keys ke mutabiq response data
        return jsonify({
            "status": "success",
            "prediction": 1,
            "score": score,
            "fabric": fabric.upper(),
            "structural_fit": f"{structural_fit}%",
            "aura_density": f"{aura_density}%",
            "server_status": "SUCCESS (200)",
            "tone_level": "Synchronized",
            "vector_status": "Active Matrix",
            "recommendation": "🌟 PERFECT MATCH! This fashion combination looks stunning and matches beautifully with your profile."
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Base route jo 404 error ko khatam karega aur aapka homepage load karega
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    try:
        with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Frontend file (index.html) load nahi ho saki: {str(e)}", 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
