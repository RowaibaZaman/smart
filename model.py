

# from app import db 

# class Task(db.Model):
#     __tablename__ = 'task'

#     id = db.Column(db.Integer, primary_key=True)
#     task_name = db.Column(db.String(40), nullable = False)
#     start_date = db.Column(db.Date)
#     end_date = db.Column(db.Date)
#     description = db.Column(db.Text)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))


#     project = db.relationship('Project', back_populates = 'tasks')
#     Resource_Allocation = db.relationship('ResourceAllocation', back_populates = 'taskss', lazy = True)


# class Resource(db.Model):
#     __tablename__ = 'resource'  
    
#     resource_id = db.Column(db.Integer, primary_key=True)
#     resource_name = db.Column(db.String(50), nullable=False)  
#     dep_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))
    
#     resource_allocation = db.relationship('ResourceAllocation', back_populates='resource')
#     dep = db.relationship("Department")


# class ResourceAllocation(db.Model):
#     __tablename__ = 'resource_allocation'
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
#     resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id'))  
#     allocation_date = db.Column(db.Date) 
#     task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
#     dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))  

#     taskss = db.relationship('Task', back_populates = 'Resource_Allocation')
#     project = db.relationship('Project', back_populates = 'ResourceAllocation')
#     resource = db.relationship('Resource', back_populates='resource_allocation')
    
# class Project(db.Model):
#     __tablename__ = 'project'
#     project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     project_name = db.Column(db.String(50), nullable=False)
#     start_date = db.Column(db.Date)
#     end_date = db.Column(db.Date)
#     description = db.Column(db.Text)

    
#     tasks = db.relationship('Task', back_populates = 'project' )
#     ResourceAllocation = db.relationship("ResourceAllocation", back_populates = 'project')


# class Department(db.Model):
#     __tablename__ = 'department'
#     dept_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     dep_name = db.Column(db.String(10), nullable=False)

#     employee = db.relationship('Employee', back_populates='dept')



# class Role(db.Model):
#     __tablename__ = 'role'

#     role_id = db.Column(db.Integer, primary_key=True)
#     role_name = db.Column(db.String(20), nullable=False)



# class Employee(db.Model):
#     __tablename__ = 'employee'
#     employee_id = db.Column(db.Integer, primary_key=True)
#     emp_name = db.Column(db.String(10), nullable=False)
#     gender = db.Column(db.String(6), nullable=False)
#     qualification = db.Column(db.String(10), nullable=False)
#     experience = db.Column(db.Integer, nullable=True)
#     resource_id = db.Column(db.Integer, db.ForeignKey('resource.resource_id'))
    
#     dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))  
#     project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), nullable = True)

#     dept = db.relationship('Department', back_populates='employee')


