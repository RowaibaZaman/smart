
from app import ma
from models.department_model import Department
class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        include_relationships = True
        load_instance = True


dept_schema = DepartmentSchema()
depts_schema = DepartmentSchema(many=True)

