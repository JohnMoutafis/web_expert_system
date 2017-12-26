from flask import Flask, request, jsonify
from pyknow import Fact

from maximum_example import compute_max
from robot_example import TrafficLight, robot


app = Flask(__name__)


@app.route('/example/robot/', methods=['POST'])
def pyknow_example():
    light = request.get_json().get('light', None)
    if light is None or light not in ['green', 'red', 'yellow', 'blinking_yellow']:
        return 'That is not a valid light color...'
    robot.reset()
    robot.declare(TrafficLight(color=light))
    robot.run()
    return jsonify({'robot_response': robot.response})


@app.route('/example/maximum/', methods=['POST'])
def maximum_example():
    compute_max.reset()
    compute_max.declare(*[Fact(val=n) for n in set(
            [int(x) for x in request.get_json().get('find_max_of', [])]
        )
    ])
    compute_max.run()
    return jsonify({'response': compute_max.response})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
