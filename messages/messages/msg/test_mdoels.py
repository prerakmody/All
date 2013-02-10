class WallPost(models.Model):
	text=models.CharField()
	url=models.URLField()

class UserProfile(models.Model):
	name=models.CharField()
	wall_posts=models.ManyToManyField(WallPost,through='UserWall')

class UserWall(models.Model):
	profile=models.ForeignKey(UserProfile)
	post=models.ForeignKey(WallPost)

class Group(models.Model):
	name=models.CharField()
	wall_posts=models.ManyToManyField(WallPost,through='GroupWall')

class GroupWall(models.Model):
	group=models.ForeignKey(Group)
	post=models.ForeignKey(WallPost)

