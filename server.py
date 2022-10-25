from flask import Flask, request, jsonify

# flask.request allows you to get info from a request through flask
# flask.jsonify converts inputs into a JSON

app = Flask(__name__)


@app.route('/',
           methods=['Get'])  # This means the route is just "/" so you can
# get here with just the host name. When a request comes in with just a
# "/", it'll run the # server_status()
def server_status():  # Your function name doesn't need to be the same as the
    # route, but they are usually the same
    return 'Server is on.'


@app.route('/info', methods=['GET'])
def information():
    x = 'This website will calculate blood cholesterol levels.\n'
    x += 'It is written by Junqi Lu.'

    return x


@app.route('/hdl_check', methods=['POST'])
def hdl_check_from_internet():
    """
        incoming_json (dict): {'name': <name_str>,
        'hdl_value':<hdl_value_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data['hdl_value']
    print('The received value was {}'.format(hdl_value))
    answer = check_HDL(hdl_value)  # This will print to the window of your
    # server (the server side). This printout won't show up on the client
    # side. The client side can only see the returned values
    return answer


@app.route('/add_numbers', methods=['POST'])
def sum_numbers_from_internet():
    """
        incoming_json (dict): {'a': <int>, 'b': <int>}
    """
    in_data = request.get_json()
    answer = in_data['a'] + in_data['b']
    return jsonify(answer)


@app.route('/add/<a>/<b>', methods=['GET'])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == '__main__':
    app.run()
