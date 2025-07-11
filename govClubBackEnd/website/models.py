from django.db import models


class Homepage(models.Model):
    pass


class Hero(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='hero_sections')


class Mission(models.Model):
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='mission_sections')


class MissionSubsection(models.Model):
    mission_section = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='subsections')
    title = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        db_table = 'website_mission-subsection'


class MissionCard(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    mission_section = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='cards')
    mission_subsection = models.ForeignKey(MissionSubsection, on_delete=models.CASCADE, related_name='cards')
    class Meta:
        db_table = 'website_mission-card'


class Direction(models.Model):
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='direction_sections')
    section_title = models.CharField(max_length=255)


class DirectionCard(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    direction_section = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='cards')
    class Meta:
        db_table = 'website_direction-card'


class CourseAnnouncement(models.Model):
    description = models.TextField()
    course_section = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='course_announcements')

    class Meta:
        db_table = 'website_course-announcement'


class CourseAnnouncementCard(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    course_announcement = models.ForeignKey(CourseAnnouncement, on_delete=models.CASCADE, related_name='cards')

    class Meta:
        db_table = 'website_course-announcement-card'
