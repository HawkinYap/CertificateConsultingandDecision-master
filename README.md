# CertificateConsultingandDecision-master
College Students' Certificate Consulting and Decision System
#### 摘要
为解决盲目考证、一味追求证书数量等普遍存在于大学生群体中的问题，本系统为大学生提供“考证一对一”的个性化考证信息咨询与决策服务。考证信息查询与决策系统有如下模块：证书查询、经验分享、晒证书、试题下载个人空间和后台管理，其中个人空间又包括分享管理、试题上传、个人信息管理模块。各模块相互关联又独立的完成了考证信息查询与决策系统的全业务流程。

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
#### 界面展示
**系统首页**
![image](https://github.com/HawkinYap/CertificateConsultingandDecision-master/blob/master/system_fig/system_show6.png)
注册前仅可查看三类证书信息，注册并登陆后可显示完整系统功能

**证书介绍**
![image](https://github.com/HawkinYap/CertificateConsultingandDecision-master/blob/master/system_fig/system_show4.png)
展示证书基本信息：

**考证心得汇总**
![image](https://github.com/HawkinYap/CertificateConsultingandDecision-master/blob/master/system_fig/system_show7.png)
展示所有权限用户的考证心得，并展示热度心得推荐列表与最新心得列表

**个人主页**
![image](https://github.com/HawkinYap/CertificateConsultingandDecision-master/blob/master/system_fig/system_show5.png)
个人主页为用户提供更改个人信息、文章管理、试题上传、证书图片上传、考证决策功能

**考证决策**
个性化决策
![image](https://github.com/HawkinYap/CertificateConsultingandDecision-master/blob/master/system_fig/system_show2.png)
设计考证决策辅助问卷，对800名大学生进行问卷调查，了解其考证的选择、备考、考证动机等因素，综合学生数据，利用层次分析法（AHP）对问卷问题进行权重处理，用户想要考取某个证书前，可通过填写问卷并查看得分意见的方式，做出考证决策

VS决策
![image](https://github.com/HawkinYap/CertificateConsultingandDecision-master/blob/master/system_fig/system_show3.png)
利用两个证书的参数对比来辅助用户做出考证决策
### 附件
系统文档请查看： document/document.pdf
