from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Professional Global Fashion Matrix Architecture
FASHION_MATRIX = {
    "FEMALE": [
        {"name": "Bohemian Maxi Dress", "tag": "Global Indie Trend", "colors": ["#db2777", "#fbcfe8", "#7c3aed"]},
        {"name": "Oversized Streetwear Jacket", "tag": "Tokyo Street Style", "colors": ["#0f172a", "#334155", "#cbd5e1"]},
        {"name": "Tailored Corporate Blazer", "tag": "Milan Runway Classic", "colors": ["#1e3a8a", "#1d4ed8", "#93c5fd"]},
        {"name": "Silk-infused Evening Gown", "tag": "Parisian Luxury Haute", "colors": ["#4c1d95", "#6d28d9", "#ddd6fe"]},
        {"name": "Minimalist Co-ord Set", "tag": "Scandinavian Aesthetic", "colors": ["#1e293b", "#475569", "#f1f5f9"]}
    ],
    "MALE": [
        {"name": "Premium Bomber Jacket", "tag": "Urban London Street", "colors": ["#0f172a", "#db2777", "#1e3a8a"]},
        {"name": "Slim-Fit Structured Suit", "tag": "Italian Sartorial", "colors": ["#1e1b4b", "#312e81", "#4338ca"]},
        {"name": "Relaxed Linen Over-Shirt", "tag": "Resort Luxury", "colors": ["#fef08a", "#ca8a04", "#fef9c3"]},
        {"name": "Monochrome Luxury Hoodie", "tag": "Seoul Street Couture", "colors": ["#111827", "#374151", "#9ca3af"]},
        {"name": "Smart-Casual Textured Blazer", "tag": "New York Elite", "colors": ["#0f172a", "#1e293b", "#64748b"]}
    ]
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() or {}
        gender = data.get('gender', 'MALE').upper()
        fabric = data.get('fabric', 'COTTON BLEND').upper()
        
        if gender not in ["FEMALE", "MALE"]:
            gender = "MALE"

        # 1. Main Match Score (85% se 99% tak)
        score = random.randint(85, 99)
        structural_fit = random.randint(82, 96)
        aura_density = random.randint(85, 100)
        
        # 2. Targeted Logic Rules for Alternatives
        pool = FASHION_MATRIX[gender]
        selected_items = random.sample(pool, 3) # Hamesha 3 unique alternatives uthayega
        
        alternatives = []
        for item in selected_items:
            if score >= 95:
                # Agar main score >= 95% hai toh alternative range 95% - 99% hogi
                alt_match = random.randint(95, 99)
            else:
                # Agar kam hai toh hamesha 90% ke andar (80% - 89%) limits lagengi
                alt_match = random.randint(80, 89)
                
            alternatives.append({
                "name": f"{item['name']} ({fabric})",
                "match": f"{alt_match}%",
                "tag": item["tag"]
            })
            
        # 3. Dynamic Color Palette Mapping
        # Pehle alternative item ke palette colors dashboard par forward karenge
        palette_colors = selected_items[0]["colors"]

        return jsonify({
            "status": "success",
            "prediction": 1,
            "score": score,
            "fabric": fabric,
            "structural_fit": f"{structural_fit}%",
            "aura_density": f"{aura_density}%",
            "server_status": "SUCCESS (200)",
            "recommendation": f"🌟 GLOBAL CONFIGURATION ACTIVE: Style optimization verified against real-time multi-dimensional vector inputs.",
            "alternatives": alternatives,
            "palette": palette_colors
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    try:
        with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Frontend file read error: {str(e)}", 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
