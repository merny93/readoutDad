import json
import os
import webbrowser
from functools import wraps

from flask import Flask, url_for, render_template, jsonify, request, make_response
import webview
import app
import sys

gui_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'gui')  # development path

if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')

server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching


def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data = json.loads(request.data)
        token = data.get('token')
        if token == webview.token:
            return function(*args, **kwargs)
        else:
            raise Exception('Authentication error')

    return wrapper


@server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


@server.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html', token=webview.token)


@server.route('/setup')
def setup():
    return render_template('setup.html', token=webview.token)

@server.route('/monitor')
def monitor():
    return render_template('monitor.html', token=webview.token)



@server.route("/values/<vals>", methods=['POST'])
def values(vals):
    '''
    Set the desired params for device
    '''
    worked = app.set_params(vals)

    if worked:
        response = {
            'status': 'ok',
        }
    else:
        response = {
            'status': 'error',
        }
    return jsonify(response)


@server.route('/init', methods=['POST'])
@verify_token
def initialize():
    '''
    Perform heavy-lifting initialization asynchronously.
    :return:
    '''
    can_start = app.initialize()

    if can_start:
        response = {
            'status': 'ok',
        }
    else:
        response = {
            'status': 'error'
        }

    return jsonify(response)


@server.route('/choose/path', methods=['POST'])
@verify_token
def choose_path():
    '''
    Invoke a folder selection dialog here
    :return:
    '''
    dirs = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
    print(dirs, file=sys.stderr)
    if dirs and len(dirs) > 0:
        directory = dirs
        if isinstance(directory, bytes):
            directory = directory.decode('utf-8')
            app.dir(directory)

        response = {'status': 'ok', 'directory': directory}
    else:
        response = {'status': 'cancel'}

    return jsonify(response)


@server.route('/fullscreen', methods=['POST'])
@verify_token
def fullscreen():
    webview.windows[0].toggle_fullscreen()
    return jsonify({})



@server.route('/do/stuff', methods=['POST'])
@verify_token
def do_stuff():
    result = app.do_stuff()

    if result:
        response = {'status': 'ok', 'result': result}
    else:
        response = {'status': 'error'}

    return jsonify(response)


@server.route('/connection', methods=['POST'])
@verify_token
def connection():
    result = app.serial_connection()

    if result:
        response = {'status': 'ok', 'result': result}
    else:
        response = {'status': 'error'}

    return jsonify(response)


def run_server():
    server.run(host='127.0.0.1', port=23948, threaded=True)


if __name__ == '__main__':
    run_server()