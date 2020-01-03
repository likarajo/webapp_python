from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    name = request.args.get('name', None)
    print('name:', name)
    response = {}
    if not name:
        response['ERROR'] = 'no name found'
    elif str(name).isdigit():
        response['ERROR'] = 'name cannot be numeric'
    else:
        response['MESSAGE'] = f'Welcome {name}!'
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    if param:
        return jsonify({
            'Message': f'Welcome {name}',
            'METHOD': 'POST'
        })
    else:
        return jsonify({
            'ERROR': 'no name found'
        })

@app.route('/')
def index():
    return '<h1>Welcome to the server</h1>'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)