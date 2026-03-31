from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Your Question Bank
challenges = [
    {"id": 0, "code": "x = 10\ny = 5\nprint(x // y)", "answer": "2", "hint": "Floor division returns an integer."},
    {"id": 1, "code": "items = ['oil', 'filter']\nitems.append('plug')\nprint(len(items))", "answer": "3", "hint": "How many items are in the list now?"},
]

@app.route('/')
def home():
    # A simple, clean mobile interface
    html = '''
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { font-family: sans-serif; padding: 20px; background: #121212; color: white; }
                pre { background: #2d2d2d; padding: 15px; border-radius: 8px; overflow-x: auto; }
                input { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; }
                button { width: 100%; padding: 10px; background: #3498db; color: white; border: none; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h2>Python Logic Trainer</h2>
            <pre>{{ challenge.code }}</pre>
            <form action="/check/{{ challenge.id }}" method="post">
                <input type="text" name="guess" placeholder="Your Answer" autofocus>
                <button type="submit">Check Answer</button>
            </form>
        </body>
    </html>
    '''
    # For now, let's just show the first question
    return render_template_string(html, challenge=challenges[0])

@app.route('/check/<int:qid>', methods=['POST'])
def check(qid):
    user_answer = request.form.get('guess')
    correct_answer = challenges[qid]['answer']
    if user_answer == correct_answer:
        return "<h1>✅ Correct!</h1><a href='/'>Next Question</a>"
    else:
        return f"<h1>❌ Try Again!</h1><p>Hint: {challenges[qid]['hint']}</p><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
