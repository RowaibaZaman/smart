
from app import db
from repository.task_repo import Task_repo

class Task_BL:
    
    @staticmethod
    def get_task(task_id):
        task = Task_repo.get_task_by_id(task_id)
        if task:
            task_dict = Task_repo.get_task_schema.dump(task)
            if 'resource' in task_dict:
                del task_dict['resource']
            return task_dict
        else:
            return {"message":"task doesn't exist"}
    @staticmethod
    def delete_task_bl(task_id):
        try:
            task = Task_repo.delete_task_repo(task_id)
            if task:
                db.session.delete(task)
                db.session.commit()
                return {"message": "Task deleted successfully"}, 200
            else:
                return {"message": "Task not found"}, 404
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    
    @staticmethod
    def add_task(args):

        if not args:
            return {'message': 'No data entered'}
        
        existing_task = Task_repo.check_task(args.get("task_name"))
        if existing_task:
            return {"message": "Task already exists"}, 400

        try:
            new_task = Task_repo.add_task_repo(args)
            db.session.add(new_task)
            db.session.commit()

            return {'message': "Task added successfully"}, 201

        except Exception as e:
            db.session.rollback()
            return {'message': f"An error occurred: {str(e)}"}, 500

    @staticmethod
    def get_all_tasks():
            try:
                tasks = Task_repo.get_all_task_repo()

                serialized_tasks = Task_repo.get_task_schema.dump(tasks)
                for i in serialized_tasks:
                    if 'resource' in i:
                        del i['resource']

                return serialized_tasks

            except Exception as e:
                return {'message': f"An error occurred: {str(e)}"}, 500
            

