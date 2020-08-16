
​    
```python
from dbs import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # 学号
    name = db.Column(db.String(20))     # 姓名
    english = db.Column(db.Integer, default=0) # 英语成绩
    python = db.Column(db.Integer, default=0)   # python成绩
    c = db.Column(db.Integer, default=0)        # c成绩
    score = db.Column(db.Integer, default=0)  # 总成绩

    def __repr__(self):
        return '<student id:%s name:%s english:%s python:%s c:%s score:%s>'%(self.id, self.name, self.english, self.python,self.c,self.score)
```

