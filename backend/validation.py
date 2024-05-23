from marshmallow import Schema, fields, validate

class CreateBudgetSchema(Schema):
    budget_amount = fields.Integer(required=True, validate=validate.Range(min=1))
    withdraw_category = fields.Str(required=True, validate=validate.Length(min=2))

class CreateSpendingSchema(Schema):
    withdraw_category = fields.Str(required=True, validate=validate.Length(min=2))
    withdraw_description = fields.Str(required=True, validate=validate.Length(min=2))
    withdraw_amount = fields.Integer(required=True, validate=validate.Range(min=1))
