from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"

SYSTEM_PROMPT = """Act as a world-class AI prompt engineer. Transform the given prompt into a highly detailed, structured, and optimized prompt. Maintain the original intent while improving clarity, depth, and quality. Add context, constraints, objectives, and expected output format if relevant.

Enhancement Rules:
- Keep intent same
- Expand with clarity and depth
- Add professional wording
- Add structure and completeness
- Make output ready for real-world use

Category Intelligence:
- Coding → technical, structured, precise
- UI/UX → design-focused, layout, user experience
- Business → strategy, execution, scalability
- Content → creative, engaging, audience-focused

CRITICAL: Return ONLY the enhanced prompt text. NO code, NO explanations, NO JSON, NO descriptions."""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enhance', methods=['POST'])
def enhance_prompt():
    try:
        data = request.get_json()
        user_prompt = data.get('prompt', '').strip()
        
        if not user_prompt:
            return jsonify({'error': 'Prompt cannot be empty'}), 400
        
        payload = {
            "model": MODEL_NAME,
            "prompt": f"{SYSTEM_PROMPT}\n\nUser Prompt:\n{user_prompt}",
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 500
            }
        }
        
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        
        if response.status_code == 200:
            result = response.json()
            enhanced_prompt = result.get('response', '').strip()
            return jsonify({'enhanced_prompt': enhanced_prompt})
        else:
            error_msg = f'Ollama API error {response.status_code}'
            try:
                error_detail = response.json()
                error_msg += f': {error_detail}'
            except:
                error_msg += f': {response.text}'
            return jsonify({'error': error_msg}), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to Ollama. Make sure it is running on http://localhost:11434'}), 503
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timeout. Try a smaller prompt or check if Ollama is responding.'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
