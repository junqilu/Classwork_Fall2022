"""
Database format: a list of dictionaries that contains patient info. This is
the format that the prof follows
[{
'name': <str>,
'id': <int>,
'blood_type': <str>,
'test_name': [<str1>, <str2>,...],
'test_result': [<str1>, <str2>,...]
}]

Alternative format
[{
'name': <str>,
'id': <int>,
'blood_type': <str>,
'tests': {'test_name1': [result1, result2,...], 'test_name2': [result1,
result2,...]}
}]
"""

from flask import Flask, request, jsonify

db = []  # Make the db global

app = Flask(__name__)


@app.route('/', methods=['GET'])
def server_on():
    return 'DB server is on'  # You can click on the server link generated by
    # PyCharm to check on the status of the server after it starts running


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {'name': patient_name,
                   'id': patient_id,
                   'blood_type': blood_type,
                   'test_name': [],
                   'test_result': []}

    db.append(new_patient)


def init_server():
    # Function to initialize the db and anything else the server needs

    # Add couples of patients
    add_patient('Ann Ables', 1, 'A+')
    add_patient('Bob Boyles', 2, 'B+')

    # Initialize logging should be here

    return 0


@app.route('/new_patient', methods=['POST'])
def add_new_patient_to_server():
    """
    Receive data from POST request
    Call other functions to do all the work
    Return information
    """
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):  # This is the driver function that does
    # all the work
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400  # 400 is the status code
    add_patient(in_data['name'],
                in_data['id'],
                in_data['blood_type'])
    return 'Patient successfully added', 200  # 200 is actually default so you
    # don't need to write it out, but writing it out can increase the
    # readability of your code


def validate_new_patient_info(in_data):
    # All the return will go back to the requester
    # There might be easier way to validate these data types, but below is
    # the basic
    if type(in_data) is not dict:
        return 'POST data wat not a dictionary'

    expected_keys = ['name', 'id', 'blood_type']
    for key in expected_keys:  # We don't care about the extra data sent in
        # that the server doesn't need, but you need to ensure at least the
        # needed data was sent in
        if key not in in_data:
            return 'Key {} is missing from POST data'.format(key)

    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):  # ex_type is used
        # here rather than type so type() later still works
        if type(in_data[key]) is not ex_type:
            return "Key {}'s value has the wrong data type".format(key)

    return True


if __name__ == '__main__':
    app.run()
