from rest_framework import serializers
from .models import Hero, MissionSubsection, MissionCard, Direction, DirectionCard, \
    CourseAnnouncement, CourseAnnouncementCard, Homepage, Mission


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class MissionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionCard
        fields = "__all__"

class MissionSubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSubsection
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    mission_card = MissionCardSerializer(source='cards', many=True)
    mission_subsection = MissionSubsectionSerializer(source='mission_subsections', many=True)
    class Meta:
        model = Mission
        fields = ['mission_subsection' , 'mission_card']




class DirectionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionCard
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    direction_cards = DirectionCardSerializer(source='cards' , many=True)
    class Meta:
        model = Direction
        fields = [ 'section_title', 'direction_cards']



class CourseAnnouncementCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAnnouncementCard
        fields = "__all__"

class CourseAnnouncementSerializer(serializers.ModelSerializer):
    course_announcement_card = CourseAnnouncementCardSerializer(source='cards' , many=True)

    class Meta:
        model = CourseAnnouncement
        fields = ['section_title', 'course_announcement_card']



class HomepageSerializer(serializers.ModelSerializer):
    mission = MissionSerializer()
    direction = DirectionSerializer()
    course_announcements = CourseAnnouncementSerializer()

    class Meta:
        model= Homepage
        fields = ['mission' , 'direction' , 'course_announcements']




#
#
# class Direction(models.Model):
#     homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='direction_sections')
#     section_title = models.CharField(max_length=255)
#
#
# class DirectionCard(models.Model):
#     text = models.CharField(max_length=255)
#     description = models.TextField()
#     direction_section = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='cards')
#     class Meta:
#         db_table = 'website_direction-card'
#
#
# class CourseAnnouncement(models.Model):
#     description = models.TextField()
#     course_section = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='course_announcements')
#
#     class Meta:
#         db_table = 'website_course-announcement'
#
#
# class CourseAnnouncementCard(models.Model):
#     text = models.CharField(max_length=255)
#     description = models.TextField()
#     course_announcement = models.ForeignKey(CourseAnnouncement, on_delete=models.CASCADE, related_name='cards')
#
#     class Meta:
#         db_table = 'website_course-announcement-card'
#


