import sqlite3
import json

database = 'questions.db'
def init_db():
    """ Initialzie the database connection and tables """
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        with open('./db_init.sql', 'r') as file:
            sql_commands = file.read()
            print(sql_commands)
            cursor.executescript(sql_commands)

class PythonQuestion:
    """A single question with multiple choice options"""
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __repr__(self):
        options_str = '\n'.join([f'{key}: {value}' for key, value in self.options.items()])
        return f'Question: {self.question}\nOptions:\n{options_str}\nAnswer: ???'

    @classmethod
    def from_database(cls, question_id):
        """Get a question object by id"""
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM python_questions WHERE id={question_id}"
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                question = row[1]
                options = json.loads(row[2])
                answer = row[3]
                return PythonQuestion(question, options, answer)
            else:
                return None