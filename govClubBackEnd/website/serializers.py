from rest_framework import serializers
from .models import Hero, MissionSubsection, MissionCard, Direction, DirectionCard, \
    CourseAnnouncement, CourseAnnouncementCard, Homepage, Mission, HeroSectionCourse, CourseCurator, AboutCourse, \
    PhotoCourse, CourseDetail, Feedback, TeamHeroSection, TeamInfo, TeamMemberCard, Team


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
    hero = HeroSerializer()
    mission = MissionSerializer()
    direction = DirectionSerializer()
    course_announcements = CourseAnnouncementSerializer()

    class Meta:
        model= Homepage
        fields = ['hero' , 'mission' , 'direction' , 'course_announcements']



class HeroSectionCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionCourse
        fields = ['date', 'image', 'section_title']

class CourseCuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCurator
        fields = ['section_title', 'fullname', 'image', 'description']

class AboutCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCourse
        fields = ['section_title', 'description']

class PhotoCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCourse
        fields = ['image']

class CourseDetailSerializer(serializers.ModelSerializer):
    hero_section = HeroSectionCourseSerializer()
    curator = CourseCuratorSerializer()
    about_course = AboutCourseSerializer()
    course_photo = PhotoCourseSerializer()

    class Meta:
        model = CourseDetail
        fields = ['hero_section', 'curator', 'about_course', 'course_photo']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class TeamHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamHeroSection
        fields = ['title', 'image']

class TeamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInfo
        fields = '__all__'

class TeamMemberCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberCard
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    hero_section = TeamHeroSectionSerializer()
    team_info = TeamInfoSerializer(source='info')
    team_member_cards = TeamMemberCardSerializer(source='members', many=True)

    class Meta:
        model = Team
        fields = ['hero_section', 'team_info', 'team_member_cards']