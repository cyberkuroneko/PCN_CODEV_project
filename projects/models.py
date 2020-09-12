from django.db import models

# Create your models here.
class Projects(models.Model):
    """案件モデル"""
    class Meta:
        db_table = 'T_projects'

    company_name = models.CharField(verbose_name='会社名',max_length=50)
    sales_rep = models.CharField(verbose_name='担当者名',max_length=20)
    project_name = models.CharField(verbose_name='案件名',max_length=300)
    needed_skill = models.CharField(verbose_name='必須スキル',max_length=200)
    other_skill = models.CharField(verbose_name='追加スキル',max_length=200)
    company_address = models.CharField(verbose_name='場所',max_length=200, default="岩本町")
    period = models.CharField(verbose_name='期間',max_length=50)
    job_detail = models.CharField(verbose_name='内容',max_length=300)
    needed_member = models.CharField(verbose_name='人数',max_length=10)
