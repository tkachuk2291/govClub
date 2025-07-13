from django.db import models
from django.utils import timezone


class Homepage(models.Model):
    pass


# class Hero(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='hero_sections')


class Hero(models.Model):
    title_part1 = models.CharField(max_length=255)
    title_part2 = models.CharField(max_length=255)
    description = models.TextField()
    homepage = models.OneToOneField(Homepage, on_delete=models.CASCADE)


class Mission(models.Model):
    homepage = models.OneToOneField(Homepage, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "1. Mission"
        verbose_name_plural = "1. Mission"


class MissionSubsection(models.Model):
    mission_section = models.ForeignKey(Mission, on_delete=models.CASCADE , related_name='mission_subsections')
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'website_mission-subsection'
        verbose_name = "2. MissionSubsection"
        verbose_name_plural = "2. MissionSubsection"

class MissionCard(models.Model):
    mission_section = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=255)
    description = models.TextField()


    class Meta:
        db_table = 'website_mission-card'
        verbose_name = "3. MissionCard"
        verbose_name_plural = "3. MissionCard"


class Direction(models.Model):
    homepage = models.OneToOneField(Homepage, on_delete=models.CASCADE)
    section_title = models.CharField(max_length=255)
    class Meta:
        verbose_name = "4. Direction"
        verbose_name_plural = "4. Direction"


class DirectionCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    direction_section = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='cards')

    class Meta:
        db_table = 'website_direction-card'
        verbose_name = "5. DirectionCard"
        verbose_name_plural = "5. DirectionCard"


class CourseAnnouncement(models.Model):
    homepage = models.OneToOneField(Homepage, on_delete=models.CASCADE, related_name='course_announcements')
    section_title = models.CharField(max_length=255)

    class Meta:
        db_table = 'website_course-announcement'
        verbose_name = "6. CourseAnnouncement"
        verbose_name_plural = "6. CourseAnnouncement"


class CourseAnnouncementCard(models.Model):
    title = models.CharField(max_length=255)
    lector = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    course_announcement = models.ForeignKey(CourseAnnouncement, on_delete=models.CASCADE, related_name='cards')

    class Meta:
        db_table = 'website_course-announcement-card'
        verbose_name = "7. CourseAnnouncementCard"
        verbose_name_plural = "7. CourseAnnouncementCard"
