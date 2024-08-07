from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# OpenAI APIキーの設定
openai.api_key = 'あなたのAPIキー'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['GET', 'POST'])
def generate_resume():
    if request.method == 'POST':
        user_info = request.form['user_info']
        prompt = f"以下の情報を基に、簡潔な履歴書を作成してください：\n{user_info}"
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500
        )
        
        resume = response.choices[0].text.strip()
        return render_template('resume.html', resume=resume)
    return render_template('resume.html')

@app.route('/interview_practice', methods=['GET', 'POST'])
def interview_practice():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        
        prompt = f"面接官として、以下の質問と回答を評価し、改善点を指摘してください：\n質問: {question}\n回答: {answer}"
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200
        )
        
        feedback = response.choices[0].text.strip()
        return render_template('interview.html', feedback=feedback)
    return render_template('interview.html')

@app.route('/analyze_company', methods=['GET', 'POST'])
def analyze_company():
    if request.method == 'POST':
        company_name = request.form['company_name']
        
        prompt = f"{company_name}について、業界での位置づけ、強み、弱み、今後の展望を分析してください。"
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=300
        )
        
        analysis = response.choices[0].text.strip()
        return render_template('company_analysis.html', analysis=analysis)
    return render_template('company_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)