from flask import Flask, render_template, request, url_for, redirect
from dbs import db
from sqlalchemy import or_
from models import Student
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# 主页
@app.route('/')
def index():
    # 所有学生信息
    s_student = Student.query.all()
    return render_template('index.html',student=s_student)

# 添加
@app.route('/add_student/',methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        s_name = request.form.get('name')
        s_english = request.form.get('english')
        s_python = request.form.get('python')
        s_c = request.form.get('c')
        if s_name and s_python and s_english and s_c:
            s_score = int(s_english) + int(s_python) + int(s_c)
            data = Student(name=s_name, english=s_english, python=s_python, c=s_c, score=s_score)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_student.html',err='嘿，你忘记写全了！！！')
    return render_template('add_student.html')

# 删除
@app.route('/del_student/',methods=['GET','POST'])
def del_student():
    del_id = request.args.get('del')
    if del_id:
        Student.query.filter(Student.id == del_id).delete()
        db.session.commit()
        return redirect(url_for('index'))
# 修改
@app.route('/mod_student/',methods=['GET','POST'])
def mod_student():
    mod_id = request.args.get('mod')
    data = Student.query.filter(Student.id == mod_id)
    if request.method == 'POST':
        s_name = request.form.get('name')
        s_english = request.form.get('english')
        s_python = request.form.get('python')
        s_c = request.form.get('c')
        if s_name and s_python and s_english and s_c:
            s_score = int(s_english) + int(s_python) + int(s_c)
            data.update({'name': s_name, 'english': s_english, 'python': s_python, 'c': s_c, 'score':s_score})
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('mod_student.html',err='嘿，修改你都能忘记写全，你个垃圾！！！')
    return render_template('mod_student.html')


if __name__ == '__main__':
    app.run(debug=True)

