from app import db



class Employee(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    qualification = db.Column(db.String(10), nullable=False)
    experience = db.Column(db.Integer, nullable=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id'))
    
    dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))  
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), nullable = True)

    # dept = db.relationship('Department', back_populates='employee')


