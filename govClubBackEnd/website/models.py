from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Homepage(models.Model):
    pass


class Hero(models.Model):
    title_part1 = models.CharField(max_length=255)
    title_part2 = models.CharField(max_length=255)
    description = models.TextField()
    homepage = models.OneToOneField(Homepage, on_delete=models.CASCADE)
    verbose_name = "0. Hero"
    verbose_name_plural = "0. Hero"


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
    slug = models.SlugField(blank=True, null=True)
    image = models.URLField()
    title = models.CharField(max_length=255)
    lector = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    course_announcement = models.ForeignKey(CourseAnnouncement, on_delete=models.CASCADE, related_name='cards')

    class Meta:
        db_table = 'website_course-announcement-card'
        verbose_name = "8. CourseAnnouncementCard"
        verbose_name_plural = "8. CourseAnnouncementCard"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            i = 1
            while CourseAnnouncementCard.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)


class CourseDetail(models.Model):
    card = models.OneToOneField('CourseAnnouncementCard', on_delete=models.CASCADE, related_name='course_detail')
    class Meta:
        db_table = 'website_course-detail'

        verbose_name = "9. CourseDetail"
        verbose_name_plural = "9. CourseDetail"

class HeroSectionCourse(models.Model):
    date = models.DateField(default=timezone.now)
    image = models.URLField()
    section_title= models.CharField(max_length=255)
    card = models.OneToOneField('CourseDetail', on_delete=models.CASCADE, related_name='hero_section')

    class Meta:
        db_table = 'website_course-hero-section-course'
        verbose_name = "10. HeroSectionCourse"
        verbose_name_plural = "10. HeroSectionCourse"

class CourseCurator(models.Model):
    db_table = 'website_course-curator'

    section_title= models.CharField(max_length=255)
    fullname = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField()
    card = models.OneToOneField('CourseDetail', on_delete=models.CASCADE, related_name='curator')

    class Meta:
        db_table = 'website_course-curator'

        verbose_name = "11. CourseCurator"
        verbose_name_plural = "11. CourseCurator"

class AboutCourse(models.Model):
    section_title= models.CharField(max_length=255)
    description = models.TextField()
    card = models.OneToOneField('CourseDetail', on_delete=models.CASCADE, related_name='about_course')

    class Meta:
        db_table = 'website_about-course'

        verbose_name = "12. AboutCourse"
        verbose_name_plural = "12. AboutCourse"

class PhotoCourse(models.Model):
    card = models.OneToOneField('CourseDetail', on_delete=models.CASCADE, related_name='course_photo')
    image = models.URLField()

    class Meta:
        db_table = 'website_photo-course'

        verbose_name = "13. PhotoCourse"
        verbose_name_plural = "13. PhotoCourse"

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    page = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'website_feedback'
        verbose_name = "14. Feedback"
        verbose_name_plural = "14. Feedback"


class Team(models.Model):
    pass


class TeamHeroSection(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='hero_section')

    class Meta:
        db_table = 'website_team-hero-section'
        verbose_name = "15. TeamHeroSection"
        verbose_name_plural = "15. TeamHeroSection"

class TeamInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='info')

    class Meta:
        db_table = 'website_team-info'
        verbose_name = "16. TeamInfo"
        verbose_name_plural = "16. TeamInfo"

class TeamMemberCard(models.Model):
    image = models.URLField()
    fullname = models.CharField(max_length=255)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    class Meta:
        db_table = 'website_team-member-card'
        verbose_name = "17. TeamMemberCard"
        verbose_name_plural = "17. TeamMemberCard"