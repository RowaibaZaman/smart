# from app import ma

# from model import Department, Resource, ResourceAllocation, Employee, Task, Role,Project



# class EmployeeSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Employee
#         include_relationships = True
#         load_instance = True

#     department = ma.Nested('DepartmentSchema', only = ["dep_name"])

# class DepartmentSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Department
#         include_relationships = True
#         load_instance = True

# class Resource(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Resource
#         include_relationships = True
#         load_instance = True

   
#     task = ma.Nested('TaskSchema', only = ['task_name', 'start_date', 'end_date'])

# class TaskSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Task
#         include_relationship = True
#         load_instance= True

#     resource = ma.Nested('Resource')
    
# class ResourceAllocation(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = ResourceAllocation
#         include_relationships = True
#         load_instance = True

# class Role(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Role
#         include_relationships = True
#         load_instance = True

# class Project(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Project
#         include_relationships = True
#         load_instance = True
#         tasks = ma.Nested('TaskSchema', many = True, only = ['task_name'])

# # Initialize schemas

# dept_schema = DepartmentSchema()
# depts_schema = DepartmentSchema(many=True)

# employee_schema = EmployeeSchema()
# employees_schema = EmployeeSchema(many=True)

# project_schema = Project()
# projects_schema = Project(many=True)

# resourcesallocation_schema = ResourceAllocation()
# resourcesallocations_schema = ResourceAllocation(many=True)

# resource_schema = Resource()
# resources_schema = Resource(many=True)

# role_schema = Role()
# roles_schema = Role(many=True)

# task_schema = TaskSchema()
# tasks_schema = TaskSchema(many=True)

