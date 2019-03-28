# CertificateConsultingandDecision-master
College Students' Certificate Consulting and Decision System
#### 摘要
**摘要**:为解决盲目考证、一味追求证书数量等普遍存在于大学生群体中的问题，本系统为大学生提供“考证一对一”的个性化考证信息咨询与决策服务。考证信息查询与决策系统有如下模块：证书查询、经验分享、晒证书、试题下载个人空间和后台管理，其中个人空间又包括分享管理、试题上传、个人信息管理模块。各模块相互关联又独立的完成了考证信息查询与决策系统的全业务流程。

* * *
#### 使用说明
**系统运行环境**
 + MySQL5-7.17及其以上版本；
 + Python 3.6+Django；
 + 用浏览器Google Chrome57.0.2987.133，IE 11及火狐等其它主流浏览器运行；
#### 项目运行
**数据库迁移**
``` python
python manage.py makemigrations
python manage.py migrate
```
**创建超级管理员**
``` python
python manage.py createsuperuser  
```
**启动服务**
``` python
python manage.py runserver 
```
**访问主页**
http://localhost:8000/list
* * *
