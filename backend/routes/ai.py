from flask import Blueprint, request, jsonify
import os
import google.generativeai as genai

ai_bp = Blueprint("ai", __name__)

genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))

@ai_bp.route("/generate", methods=["POST"])
def generate_blog_content():
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("subtitle", "")
    img = data.get("img", "")
    
    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 🎯 Improved prompt with formatting rules
        prompt = f"""
        You are a professional blog writer. 
        Generate a well-formatted blog article for:

        📝 Title: {title}
        🔖 Subtitle: {subtitle if subtitle else "N/A"}
        🖼️ Image: {img if img else "N/A"}

        ✅ Formatting Instructions:
        1. Start with a short engaging introduction (2–3 lines).
        2. Use clear section with emojis.
        3. Keep paragraphs short and easy to scan.
        4. Use bullet points or numbered lists when explaining.
        5. End with a concise conclusion + call-to-action.
        6. Do NOT add markdown image references like (Image: ...). Just assume image will be displayed.
        7. Output should be ready to display on a blog (no raw markdown like ## ,* <h1> ,and all those things ).
        for reference :📌 Introduction
        8.dont add * like this directly content only  ☀️ **Hydration and Movement:** 

For decades, computers have been the driving force of innovation. But traditional computers, no matter how powerful, are limited by binary logic—processing information as 0s and 1s. Enter Quantum Computing, a revolutionary technology that uses the strange principles of quantum physics to perform calculations unimaginable for classical machines.


⚡ What is Quantum Computing?


Unlike normal bits, qubits can exist in multiple states simultaneously thanks to superposition. Combined with entanglement and quantum gates, qubits allow quantum computers to explore many solutions at once.


This doesn’t mean quantum computers will replace classical ones—but they will solve problems that were previously considered impossible.


🚀 Real-World Applications

1. Drug Discovery & Healthcare


Quantum computers can simulate complex molecules at an atomic level, helping scientists design life-saving drugs faster and cheaper.


2. Cryptography & Security


Current encryption methods like RSA could be cracked by quantum algorithms in minutes. This has led to the rise of post-quantum cryptography to keep data secure.


3. Artificial Intelligence


Quantum-enhanced AI can handle massive datasets more efficiently, accelerating deep learning, optimization, and natural language processing.


4. Logistics & Supply Chains


From delivery routes to airline scheduling, quantum optimization can save billions in costs and improve efficiency globally.


5. Climate Modeling


By processing complex climate variables, quantum systems could help predict weather patterns and design better renewable energy systems.


⚠️ Challenges Ahead


Fragile Qubits: Quantum states are extremely sensitive to noise and temperature.


High Costs: Current quantum machines are expensive and require special cooling systems.


Limited Access: Only a few companies and research labs have real quantum computers.


Despite these, global tech giants like Google, IBM, and Microsoft are investing heavily, and governments are funding large-scale quantum research.


🔮 The Road Ahead


Quantum computing is still in its early days, but progress is rapid. Within the next decade, hybrid computing systems (classical + quantum) could become common. Industries like finance, healthcare, and cybersecurity will see the biggest disruptions.


✅ Conclusion


Quantum computing is not just another upgrade—it’s a paradigm shift. While today’s prototypes are experimental, the technology is advancing quickly. As businesses prepare for a quantum future, individuals must also be aware of its impact on jobs, security, and society.


👉 Just as the internet transformed the world in the 1990s, quantum computing might redefine the 2030s. like this u have to ggenerate other to use diff format its okey but ... content should be clear and cllean
        """     

        response = model.generate_content(prompt)
        content = response.text.strip()
        print(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"description": content}), 200
