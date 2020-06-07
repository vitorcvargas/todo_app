from todo import db

class Todo(db.Models):
    __tablename__ = 'todo'
    id = db.Columns(db.Integer, primary_key = True)
    todo_name = db.Columns(db.String(50), nullable = False)
    # TODO backref
    activities = db.relationship('Activities', lazy = True)

    def __repr__(self):
        return f"Todo('{self.todo_name}')"

class Activities(db.Models):
    __tablename__ = 'activities'
    id = db.Columns(db.Integer, primary_key = True)
    activities = db.Columns(db.String(50), nullable = False)
    todo.id = db.Columns(db.Integer, db.ForeignKey('todo.id'))

    def __repr__(self):
        return f"Activities('{self.activities}')"