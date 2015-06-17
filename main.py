from flask import Flask, render_template, request, redirect, jsonify, url_for
from extraction import extraction
from replaceText import replaceText

app = Flask(__name__)


# @app.route('/restaurant/<int:restaurant_id>/menu/JSON')
# def restaurantMenuJSON(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(
#         restaurant_id=restaurant_id).all()
#     return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/', methods=['POST'])
def hello():
    input_string = request.get_json()
    noun_list = extraction(input_string["input"])
    input_string["input"] = replaceText(input_string["input"],noun_list)
    print input_string["input"] 
    return jsonify(output=input_string["input"]+".")

@app.route('/',methods=['GET'])
def Iconify():

    return render_template('Iconify.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
