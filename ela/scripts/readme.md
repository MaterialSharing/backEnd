# 脚本注意事项
- 如果执行脚本期间,模型做出了修改,那么需重启shell,才可以看到效果.

## 遇到类似: django.db.utils.OperationalError: (2006, 'Server has gone away')的错误时
```python
# close the current connection,then reopen a new connection
import django.db
django.db.close_old_connections()
```