from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo, ObjectId
import logging

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/data1'

mongo = PyMongo(app) 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler and set the level to INFO
file_handler = logging.FileHandler('todo_Application_log.log')
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

@app.route('/')
def home():

    tasks = mongo.db.todo_data.find()
    return render_template('Home.html', tasks=tasks)




@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == "POST":
        db = mongo.db.todo_data

        title = request.form.get("taskTitle")
        description = request.form.get("taskDescription")
        due_date_time = request.form.get("dueDateTime")

        data = {
            'Task_title': title,
            'Task_description': description,
            'due_date_time': due_date_time,
            'status':"not_done"
        }
        logger.info(f"Task added: Title: {title}, Description: {description}, Due Date: {due_date_time}")

        db.insert_one(data)
        return redirect(url_for('home'))
    
@app.route('/edit_task/<string:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task_id_obj = ObjectId(task_id)
    task = mongo.db.todo_data.find_one({'_id': task_id_obj})

    if request.method == 'POST':
        # Update the task details in the database
        new_title = request.form.get('taskTitle')
        new_description = request.form.get('taskDescription')
        new_due_date_time = request.form.get('dueDateTime')
        logger.info(f"Task edited: {task_id}, New Title: {new_title}, New Description: {new_description}, New Due Date: {new_due_date_time}")

        mongo.db.todo_data.update_one(
            {'_id': task_id_obj},
            {'$set': {
                'Task_title': new_title,
                'Task_description': new_description,
                'due_date_time': new_due_date_time
            }}
        )

        return redirect(url_for('home'))

    return render_template('Edit_page.html', task=task)

@app.route('/delete_task/<string:task_id>',methods=['GET'])
def delete_task(task_id):
    task_id_obj = ObjectId(task_id)
    deleted_task = mongo.db.todo_data.find_one({'_id': task_id_obj})
    logger.info(f"Task deleted: {task_id}, Title: {deleted_task['Task_title']}, Description: {deleted_task['Task_description']}, Due Date: {deleted_task['due_date_time']}")

    mongo.db.todo_data.delete_one({'_id':task_id_obj})
    return redirect(url_for('home'))

@app.route('/mark_as_done/<string:task_id>', methods=['GET'])
def mark_as_done(task_id):
    task_id_obj = ObjectId(task_id)
    task = mongo.db.todo_data.find_one({'_id': task_id_obj})
    new_status = 'done' if task['status'] == 'not_done' else 'not_done'
    logger.info(f"Task status updated: {task_id}, New Status: {new_status}")
    mongo.db.todo_data.update_one({'_id': task_id_obj}, {'$set': {'status': 'done'}})
    return redirect(url_for('home'))

   

if __name__ == '__main__':
    app.run(debug=True)
