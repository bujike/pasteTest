# pasteTest
框架说明：
webob 将简单函数包装成wsgi应用
paste  载入WSGI中的Web App使用
routes 路由映射
启动方式 
1.python wsgi.py
2.uwsgi --http 192.168.13.234:35358 --wsgi-file wsgi.py
