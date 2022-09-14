from django.db import models
from django.db.models.deletion import CASCADE


class Board(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    url = models.CharField(max_length=16)
    is_nsfw = models.BooleanField(default=False)

    def __str__(self):
        return " /" + self.url + " " + self.name


class Forumpost(models.Model):
    pass


class Thread(Forumpost):
    subject = models.CharField(max_length=128)
    content = models.TextField()
    poster = models.CharField(max_length=128, default="Anonymous")
    b_id = models.ForeignKey(Board, on_delete=CASCADE)
    is_sticky = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='', null=True)
    # t_file

    def __str__(self):
        return "thread no" + " " + str(self.pk) + " " + self.subject[:16]


class Reply(Forumpost):
    poster = models.TextField(max_length=128, default="Anonymous")
    content = models.TextField()
    t_id = models.ForeignKey(Thread, on_delete=CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='', null=True, blank=True)

    # r_file

    def __str__(self):
        return "reply no" + " " + str(self.pk) + " " + self.content[:16]


class Report(models.Model):
    f_item = models.ForeignKey(Forumpost, on_delete=CASCADE)
    report_desc = models.TextField()
    report_status = models.CharField(max_length=16)


class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# this is type of model that we are only using one of


class SiteSettings(models.Model):
    sitename = models.CharField(max_length=128)
    welcome = models.TextField()  # this is going to be written in welcome page

    def __str__(self):
        return self.sitename
# those are going to be used in faq of your board


class FaqQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
# this is going to be used in ruleset or something


class Rule(models.Model):
    rule = models.TextField()

    def __str__(self):
        return self.rule
