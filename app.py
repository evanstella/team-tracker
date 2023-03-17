from flask import Flask, render_template, make_response, send_from_directory, redirect, url_for, request, flash, session, jsonify
import time, json
import bleach

import Client
from Authorized import AUTHORIZED_TOKENS, secret_key

app = Flask(__name__)

# you thought this was enterprise-grade???? WRONG
app.secret_key = secret_key

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        token_str = request.form.get('token')
        desig_str = request.form.get('designation')
    except:
        return render_template('index.html', message="TOKEN INVALID!!!\n")

    try:
        token = int(token_str)
    except (ValueError, TypeError):
        return render_template('index.html', message="TOKEN INVALID!!!\n")
    
    client = AUTHORIZED_TOKENS.get(token)
    if (client == None or client.name != desig_str):
        return render_template('index.html', message="TOKEN INVALID!!!\n")

    session['token'] = token
        
    return redirect('/map')


@app.route('/report', methods=['POST'])
def report():
    token = session.get('token')
    if token == None:
        return redirect('/')

    client = AUTHORIZED_TOKENS[token]

    try:
        content = request.json
        lat = float(content.get('latitude'))
        lon = float(content.get('longitude'))
    except:
        print("Report error from client")
        return jsonify(success=False)
    
    client.online = True
    client.last_checkin = time.time()
    client.lat = lat
    client.lon = lon

    return jsonify(success=True)


@app.route('/map')
def map():
    token = session.get('token')
    if token == None:
        return redirect('/')

    client = AUTHORIZED_TOKENS[token]

    return render_template('map.html', client=client.to_dict())


@app.route('/markers')
def markers():
    token = session.get('token')
    if token == None:
        return redirect('/')

    client = AUTHORIZED_TOKENS[token]

    try:
        f = open("./markers.json")
        markers = json.load(f)
    except:
        return jsonify(success=False)

    return jsonify(markers)


@app.route('/units')
def units():
    token = session.get('token')
    if token == None:
        return redirect('/')

    client = AUTHORIZED_TOKENS[token]

    active_units = []

    for tok in AUTHORIZED_TOKENS.keys():
        if (tok == token):
            continue

        unit = AUTHORIZED_TOKENS[tok]
        if (unit.lat == None or unit.lon == None):
            continue

        active_units.append(unit.to_dict()) 

    return jsonify(active_units)


@app.route('/update_unit', methods=['POST'])
def update():
    token = session.get('token')
    if token == None:
        return redirect('/')

    client = AUTHORIZED_TOKENS[token]
    if (not client.admin):
        return jsonify(success=False)

    try:
        content = request.json
        name  = content.get('name')
        notes = content.get('notes')
    except:
        print("update error from client")
        return jsonify(success=False)

    for tok in AUTHORIZED_TOKENS.keys():
        unit = AUTHORIZED_TOKENS[tok]
        if (unit.name == bleach.clean(name)):
            unit.notes = bleach.clean(notes)

    return redirect('/map')



if __name__ == "__main__":
    client = AUTHORIZED_TOKENS[11872584467618672260]
    client.lat = 38.870615
    client.lon = -77.119351
    client = AUTHORIZED_TOKENS[10363704738994368361]
    client.lat = 38.880625
    client.lon = -77.119351
    app.run(debug=True)