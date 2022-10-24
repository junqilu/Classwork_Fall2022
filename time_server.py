from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/',
           methods=['Get'])  # This means the route is just "/" so you can
# get here with just the host name. When a request comes in with just a
# "/", it'll run the # server_status()
def server_status():  # Your function name doesn't need to be the same as the
    # route, but they are usually the same
    return 'Server is on.'


@app.route('/date', methods=['GET'])
def get_date():
    date_time = datetime.now()
    date = date_time.date()
    date_str = date.strftime('%m/%d/%Y')
    date_str
    return date_str


@app.route('/age', methods=['POST'])
def post_age():
    in_data = request.get_json()
    in_date_str = in_data['date']
    in_date = datetime.strptime(in_date_str, '%m/%d/%Y').date()  # Convert the
    # date str into a date object based on the pattern of '%m/%d/%Y'

    current_date = datetime.now().date()
    difference_in_days = current_date - in_date  # datetime.timedelta object

    difference_in_yrs = difference_in_days.days() / 365  # You can ignore leap
    # years and just return the resulting float
    return jsonify(difference_in_yrs)


app.route('/until_next_meal/<meal>', methods=['GET'])


def meal_time(meal):
    if meal in ['breakfast', 'lunch', 'dinner']:
        return 'correct'


if __name__ == '__main__':
    app.run()