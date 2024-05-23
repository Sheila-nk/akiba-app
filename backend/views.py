from flask import Blueprint, request, jsonify
from flask.views import MethodView

from . import db
from .error_handling import BadRequest
from .models import Budget
from .validation import CreateBudgetSchema, CreateSpendingSchema


budget_blueprint = Blueprint('akiba', __name__)


class BudgetAPI(MethodView):
    def post(self):
        post_data = request.get_json()
        budget_schema = CreateBudgetSchema()

        errors = budget_schema.validate(post_data)

        if errors:
            raise BadRequest(errors)

        try:
            budget = Budget(**post_data)
            db.session.add(budget)
            db.session.commit()

            response_object = {'message': 'Budget added successfully'}
            response = jsonify(response_object)
            response.status_code = 201

            return response

        except Exception as e:
            raise e
        
budget_view = BudgetAPI.as_view('budget_api')
budget_blueprint.add_url_rule(
    '/budget',
    view_func=budget_view,
    methods=['POST']
)


class SpendingAPI(MethodView):
    def post(self):
        post_data = request.get_json()
        spending_schema = CreateSpendingSchema()

        errors = spending_schema.validate(post_data)

        if errors:
            raise BadRequest(errors)
        
        try:
            spending = Budget(**post_data)
            db.session.add(spending)
            db.session.commit()

            response_object = {'message': 'Spending added successfully'}
            response = jsonify(response_object)
            response.status_code = 201

            return response
        
        except Exception as e:
            raise e
        
spending_view = SpendingAPI.as_view('spending_api')
budget_blueprint.add_url_rule(
    '/transactions',
    view_func=spending_view,
    methods=['POST']
)
