from flask import Flask, jsonify, render_template_string, request
from crewai import Agent, Task, Crew
import os

app = Flask(__name__)


os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Multi-Agent Manufacturing System</title>

        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                margin: 0;
                color: white;
            }

            .container {
                max-width: 900px;
                margin: 60px auto;
                text-align: center;
            }

            h1 {
                font-size: 38px;
                margin-bottom: 20px;
            }

            .input-box {
                display: flex;
                gap: 10px;
                justify-content: center;
            }

            input {
                width: 70%;
                padding: 14px;
                border-radius: 10px;
                border: none;
                font-size: 16px;
            }

            button {
                padding: 14px 25px;
                border-radius: 10px;
                background: #00c9a7;
                color: white;
                border: none;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background: #00b894;
                transform: scale(1.05);
            }

            .output {
                margin-top: 40px;
                background: white;
                color: #2c3e50;
                padding: 30px;
                border-radius: 15px;
                text-align: left;
                box-shadow: 0px 10px 40px rgba(0,0,0,0.25);
                line-height: 1.7;
            }

            .loading {
                font-style: italic;
                color: #ddd;
                margin-top: 20px;
            }

            h3 {
                color: #2c3e50;
                margin-top: 20px;
                border-left: 5px solid #00c9a7;
                padding-left: 10px;
            }

            ul {
                padding-left: 20px;
            }

            li {
                margin-bottom: 6px;
            }
        </style>
    </head>

    <body>

        <div class="container">
            <h1>Multi-Agent Manufacturing System</h1>

            <div class="input-box">
                <input id="prompt" placeholder="Enter manufacturing idea..." />
                <button onclick="generate()">Generate</button>
            </div>

            <div id="loading" class="loading"></div>

            <div class="output" id="output"></div>
        </div>

        <script>
            function formatOutput(text) {
                // Convert markdown-like to HTML
                text = text.replace(/\\*\\*(.*?)\\*\\*/g, "<b>$1</b>");
                text = text.replace(/\\n/g, "<br>");
                return text;
            }

            async function generate() {
                let prompt = document.getElementById("prompt").value;

                document.getElementById("loading").innerText = "Agents are collaborating...";
                document.getElementById("output").innerHTML = "";

                let res = await fetch('/generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({prompt: prompt})
                });

                let data = await res.json();

                document.getElementById("loading").innerText = "";
                document.getElementById("output").innerHTML = formatOutput(data.output);
            }
        </script>

    </body>
    </html>
    """)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    try:
        from openai import OpenAI

        client = OpenAI(
            api_key="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",  # 🔴 YOUR KEY HERE
            base_url="https://openrouter.ai/api/v1"
        )

       
        research = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "user", "content": f"""
                You are a Manufacturing Research Agent.

                Give short insights for: {prompt}

                Include:
                - materials
                - machines
                - workflow

                Keep it under 200 words.
                """}
            ],
            max_tokens=150
        )

        research_output = research.choices[0].message.content

        
        writer = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "user", "content": f"""
                You are a Technical Writer Agent.

                Convert this into structured report:

                {research_output}

                Format:
                - Introduction
                - Process
                - Materials
                - Conclusion

                Keep it concise.
                """}
            ],
            max_tokens=200
        )

        final_output = writer.choices[0].message.content

        return jsonify({"output": final_output})

    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
