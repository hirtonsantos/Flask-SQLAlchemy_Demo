from http import HTTPStatus
from flask import jsonify, request
from app.models.ProductModel import ProductModel
from app.configs.database import db
from sqlalchemy.orm import Query


def create_call_record():
    data = request.get_json()

    call_record = ProductModel(**data)

    db.session.add(call_record)
    db.session.commit()

    # print(f"{call_record.id=}")
    # serialized_call_record = {
    #     key: value for key, value in call_record.__dict__.items() if key != "_sa_instance_state"
    # }

    # print(f"{serialized_call_record=}")

    return jsonify(call_record), HTTPStatus.CREATED


def retrieve_call_record():
    base_query: Query = db.session.query(ProductModel)

    # records = base_query.order_by(CallRecord.id).all()
    records = base_query.all()

    print(records)

    return jsonify(records), HTTPStatus.OK
