from flask import Flask, url_for, jsonify
from random import randint
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)   
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/ad_stats/<ad_id>', methods = ['GET'])
def api_ad_stats(ad_id):
    views = randint(0, 100)
    contacts = randint(0, 50)
    ad_data = {
        'ad_id'  : ad_id,
        'num_views' : views,
        'num_contacts' : contacts,
        'emoji' : emoji_calculator(views),
        'version' : '4.0'
    }

    resp = jsonify(ad_data)
    resp.status_code = 200

    return resp

def emoji_calculator(views):
    if views <= 25:
        emoji = 'bad'
    elif views <= 50:
        emoji = 'ok'
    else:
        emoji = 'good'
    return emoji

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




