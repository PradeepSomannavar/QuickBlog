from flask import Blueprint, request, jsonify
import os
import requests

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/generate", methods=["POST"])
def generate_blog_content():
    data = request.get_json()
    title = data.get("title")
    subtitle = data.get("subtitle", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    prompt = f"""You are a professional blog writer. Generate a well-formatted blog article.

Title: {title}
Subtitle: {subtitle if subtitle else "N/A"}

Format rules:
1. Start with a short engaging introduction (2-3 lines).
2. Use clear sections with emoji headings.
3. Keep paragraphs short and easy to scan.
4. Use bullet points or numbered lists when explaining.
5. End with a concise conclusion.
6. Output ready-to-display content. No markdown syntax like ##, *, or <h1>.
7. Write in plain paragraphs with emoji section headers.

Example format:
📌 Introduction
Your engaging intro here...

☀️ Main Point One
Your content here...

🎯 Conclusion
Your closing thoughts here."""

    try:
        api_key = os.getenv("GOOGLE_AI_API_KEY")
        if not api_key:
            return jsonify({"error": "GOOGLE_AI_API_KEY not configured"}), 500

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": prompt.strip()}]}]}

        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        content = result["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"description": content}), 200
