import jsonpickle

from src.controller.CivilizationController import CivilizationController
import flask

from flask import request

from src.models.api.error import Error


class Router:

    def __init__(self,
                 app: flask.Flask,
                 civilization_controller: CivilizationController
                 ) -> None:

        @app.route("/", methods=['GET'])
        def default():
            return "<h2>Endpoints</h2>" \
                   "" \
                   "<p>/civilizations - this is used to retrieve all civilizations and preload the data in mysql and " \
                   "cache in redis<p>" \
                   "" \
                   "<p>/civilization?civ_id=1 OR /civilization?name=Slavs"

        @app.route('/civilizations', methods=['GET'])
        def fetch_all_civilizations():
            try:
                resp = flask.Response(civilization_controller.fetch_and_load_all_civilizations())
            except Exception as e:
                print(e)
                resp = flask.Response(Error("Something went wrong try again please").to_string())

            resp.headers['Content-Type'] = 'application/json'
            return resp

        @app.route('/civilization', methods=['GET'])
        def fetch_specific_civilization():
            try:
                civ_name = request.args.get('name')
                civ_id = request.args.get('civ_id')

                if civ_name is None and civ_id is None:
                    return jsonpickle.encode(Error("please define a civ_id or name in the url"), unpicklable=False)

                resp = ""
                if civ_name is not None:
                    resp = flask.Response(
                        jsonpickle.encode(civilization_controller.fetch_civilization_by_name(civ_name),
                                          unpicklable=False))
                if civ_id is not None:
                    resp = flask.Response(
                        jsonpickle.encode(civilization_controller.fetch_civilization_by_id(int(civ_id)),
                                          unpicklable=False))
            except Exception as e:
                print(e)
                resp = flask.Response(Error("Something went wrong try again please").to_string())

            resp.headers['Content-Type'] = 'application/json'
            return resp
