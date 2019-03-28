# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AccountFile(models.Model):
    file = models.CharField(max_length=100)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_file'


class AccountUserinfo(models.Model):
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    getcert = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    aboutme = models.TextField()
    user = models.ForeignKey('AuthUser', unique=True)
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'account_userinfo'


class AccountUserprofile(models.Model):
    stunamber = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('AuthUser', unique=True)

    class Meta:
        managed = False
        db_table = 'account_userprofile'


class ArticleArticlecolumn(models.Model):
    column = models.CharField(max_length=200)
    created = models.DateField()
    user = models.ForeignKey('AuthUser')

    class Meta:
        managed = False
        db_table = 'article_articlecolumn'


class ArticleArticlepost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    author = models.ForeignKey('AuthUser')
    column = models.ForeignKey(ArticleArticlecolumn)

    class Meta:
        managed = False
        db_table = 'article_articlepost'


class ArticleArticlepostUsersLike(models.Model):
    articlepost = models.ForeignKey(ArticleArticlepost)
    user = models.ForeignKey('AuthUser')

    class Meta:
        managed = False
        db_table = 'article_articlepost_users_like'
        unique_together = (('articlepost', 'user'),)


class ArticleComment(models.Model):
    commentator = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField()
    article = models.ForeignKey(ArticleArticlepost)

    class Meta:
        managed = False
        db_table = 'article_comment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogBlogarticles(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    publish = models.DateTimeField()
    author = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'blog_blogarticles'


class CertificateTbl(models.Model):
    cert_id = models.AutoField(primary_key=True)
    cert_class = models.IntegerField()
    cert_name = models.CharField(max_length=20)
    cert_ename = models.CharField(max_length=50)
    cert_content = models.CharField(max_length=1000)
    cert_time = models.CharField(max_length=1000)
    cert_qualif = models.CharField(max_length=1000)
    cert_relate = models.CharField(max_length=1000, blank=True, null=True)
    cert_intro = models.CharField(max_length=1000)
    cert_link = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_tbl'


class CertificateVs(models.Model):
    cert_id = models.AutoField(primary_key=True)
    cert_name = models.CharField(max_length=50)
    cert_dif = models.CharField(max_length=20)
    cert_quality = models.CharField(max_length=50)
    cert_condition = models.CharField(max_length=200)
    cert_time = models.CharField(max_length=200)
    cert_cost = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'certificate_vs'


class ContractContract(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'contract_contract'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImageImage(models.Model):
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateField()
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'image_image'


class ImgDbImg(models.Model):
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'img_db_img'
