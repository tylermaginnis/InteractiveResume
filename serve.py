from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/textures/<path:filename>')
def serve_textures(filename):
    return send_from_directory('textures', filename)

if __name__ == '__main__':
    app.run(debug=True)
