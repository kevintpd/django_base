from django.db import models

# Create your models here.
"""
1.模型类需要继承自models.Model
2.系统会自动为我们添加一个主键--id
3.字段

    字段名 = models.类型(选项)
    字段名其实就是数据表的属性名
    字段名不要使用Python、mysql的关键字
"""
class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=10)
    #重写str方法让admin显示书籍名字
    def __str__(self):
        return self.name

#任务先复制过来，后期讲原理
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
