from django.db import models

class Record(models.Model):
	create_at = models.DateTimeField(auto_now_add=True)
	nickname = models.CharField(max_length=50)
	insta = models.CharField(max_length=50)
	age = models.CharField(max_length=50)
	sex = models.CharField(max_length=50)
	country = models.CharField(max_length=50) 
	song = models.CharField(max_length=50)
	music_video = models.CharField(max_length=50)
	time_stamp = models.CharField(max_length=50)
	theory = models.CharField(max_length=5000)

	def __str__(self):
		return(f"{self.song} {self.music_video} {self.time_stamp} {self.theory}")

