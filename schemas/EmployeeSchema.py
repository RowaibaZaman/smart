from models. employee_model import Employee
from app import ma

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_relationships = True
        load_instance = True


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
