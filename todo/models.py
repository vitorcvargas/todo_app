from todo import db

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    activities = db.relationship('Activities', backref = "todo", lazy = True)

    def __repr__(self):
        return f"Todo('{self.todo_name}')"

class Activities(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key = True)
    activity = db.Column(db.String(50), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

    def __repr__(self):
        return f"Activities('{self.activities}')"
