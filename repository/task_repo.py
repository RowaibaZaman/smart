
from app import db
from models.task_model import Task
from datetime import datetime
from schemas.TaskSchema import TaskSchema

class Task_repo:
        @staticmethod     
        def check_task(task_name):
                return Task.query.filter_by(task_name= task_name).first()
   

        @staticmethod
        def check_task_id(task_id):
             check = Task.query.get(task_id)
             return check

        @staticmethod  
        def get_task_by_id(task_id):
                task = db.session.query(Task).filter(Task.id == task_id).first()

                return task
        
        @staticmethod  
        def delete_task_repo(task_id):
                task = Task.query.get(task_id)
                print(f"Query for task_id {task_id} returned: {task}")
                return task
        
        @staticmethod  
        def get_all_task_repo():
                return Task.query.all()

        
        @staticmethod  
        def add_task_repo(args):
                # if args.get('start_date'):
                #         args['start_date'] = datetime.strptime(args['start_date'], '%Y-%m-%d')
                # if args.get('end_date'):
                #         args['end_date'] = datetime.strptime(args['end_date'], '%Y-%m-%d')

                new_task = Task(**args)

                return new_task
        
        @staticmethod
        def get_task_schema(single=True):
                """Create and return the schema instance."""
                return TaskSchema() if single else TaskSchema(many=True)
                
