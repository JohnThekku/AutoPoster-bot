from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/rewrite', methods=['POST'])
def rewrite():
    subprocess.run(['python', 'rewrite_posts.py'])
    return "✅ Rewrite complete!"

if __name__ == '__main__':
    app.run(port=5000)
