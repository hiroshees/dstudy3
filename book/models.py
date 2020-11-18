from django.db import models

class Book (models.Model):
    title = models.CharField(
        verbose_name="タイトル",
        max_length=255,
    )
    price = models.IntegerField(
        verbose_name="金額",
        default = 0,
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        verbose_name="著者",
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name="カテゴリ",
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )
    
    def __str__(self):
        return self.title;


class Author(models.Model):
    name = models.CharField(
        verbose_name="著者名",
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )

    def __str__(self):
        return self.name;

class Category(models.Model):
    name = models.CharField(
        verbose_name="カテゴリ名",
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name="登録日",
    )
    modified = models.DateTimeField(
        auto_now = True,
        verbose_name="更新日",
    )

    def __str__(self):
        return self.name;

