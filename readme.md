Python Flask基础框架
=====================
## 启动
* export ops_config=local|production && python manage.py runserver

## 根据数据库生成model
工具：flask-sqlacodegen  
```
flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/user.py"  --flask
```

## 安装依赖
pip install -r requirements.txt
