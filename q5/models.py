from django.db import models

class series(models.Model):
	imdb_id = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	streaming = models.IntegerField()
	next_episode = models.DateTimeField(null=True, blank=True)
	next_season = models.DateField(null=True, blank=True)
	def __str__(self):
		return "%s %s" % (self.name, self.imdb_id)

class user(models.Model):
	email_id = models.CharField(max_length=200)
	def __str__(self):
		return "%s %s" % (self.email_id, self.id)

class subscription(models.Model):
	series = models.ForeignKey(series, on_delete=models.CASCADE)
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	def __str__(self):
		return "%s %s" % (self.user, self.series)