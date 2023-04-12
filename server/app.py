#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate

from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>HOME</h1>'

@app.route("/episodes")
def episodes():
    all_episodes = []
    for episode in Episode.query.all():
        episode_dict = episode.to_dict()
        all_episodes.append(episode_dict)

    jsonified_episodes = jsonify(all_episodes)

    response = make_response(jsonified_episodes, 200)

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)

