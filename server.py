from flask import Flask, jsonify, request
from flask.views import MethodView
from typing import Type

from sqlalchemy.exc import IntegrityError
import pydantic

from db import Session
from models import AnAd
from shema import CreateAds, PatchAds


app = Flask('app_an_ad')


def validate(input_data: dict, validation_model: Type[CreateAds] | Type[PatchAds]):
    try:
        model_item = validation_model(**input_data)
        return model_item.dict(exclude_none=True)
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())


class HttpError(Exception):

    def __init__(self, status_code: int, description: str | dict | list):
        self.status_code = status_code
        self.description = description


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({'status': 'error', 'description': error.description})
    response.status_code = error.status_code
    return response


def get_ads(ads_id: int, session: Session):
    an_ad = session.get(AnAd, ads_id)
    if an_ad is None:
        raise HttpError(404, 'an_ad not found')
    return an_ad


class AdsView(MethodView):

    def get(self, ads_id: int):
        with Session() as session:
            ads = get_ads(ads_id, session)
            return jsonify({'id': ads.id,
                            'title': ads.title,
                            'description': ads.description,
                            'creation_date': ads.creation_date.isoformat(),
                            'owner': ads.owner})

    def post(self):
        json_data = request.json
        json_data = validate(json_data, CreateAds)
        with Session() as session:
            ads = AnAd(**json_data)
            session.add(ads)
            try:
                session.commit()
            except IntegrityError as er:
                raise HttpError(409, 'ads already exists')
            return jsonify({'id': ads.id})

    def patch(self, ads_id: int):
        json_data = validate(request.json, PatchAds)
        with Session() as session:
            ads = get_ads(ads_id, session)
            for field, value in json_data.items():
                setattr(ads, field, value)
            session.add(ads)
            session.commit()
            return jsonify({'status': 'patched'})

    def delete(self, ads_id: int):
        with Session() as session:
            ads = get_ads(ads_id, session)
            session.delete(ads)
            session.commit()
            return jsonify({f'an_ad - {ads_id}': 'deleted'})


app.add_url_rule('/ads/<int:ads_id>/', view_func=AdsView.as_view('ads'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ads/', view_func=AdsView.as_view('ads_create'), methods=['POST'])

if __name__ == '__main__':
    app.run()
