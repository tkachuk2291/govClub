from django.contrib import admin

from django.contrib import admin
from .models import Mission, MissionCard, MissionSubsection, Direction, DirectionCard, CourseAnnouncementCard, \
    CourseAnnouncement


class MissionCardInline(admin.TabularInline):
    model = MissionCard
    extra = 1
    show_change_link = True


class MissionSubsectionInline(admin.TabularInline):
    model = MissionSubsection
    extra = 1
    show_change_link = True


class DirectionCardInline(admin.TabularInline):
    model = DirectionCard
    extra = 1
    show_change_link = True


class CourseAnnouncementCardInline(admin.TabularInline):
    model = CourseAnnouncementCard
    extra = 1
    show_change_link = True


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'homepage']
    list_filter = ['homepage']
    search_fields = ['homepage__id']
    inlines = [MissionCardInline, MissionSubsectionInline]


@admin.register(MissionSubsection)
class MissionSubsectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'mission_section']
    list_filter = ['mission_section']
    search_fields = ['title']


@admin.register(MissionCard)
class MissionCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'mission_section']
    list_filter = ['mission_section']
    search_fields = ['title']


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_title' , 'homepage' , ]
    list_filter = ['homepage' , 'section_title']
    search_fields = ['homepage__id' , 'section_title']
    inlines = [DirectionCardInline]

@admin.register(DirectionCard)
class DirectionCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'direction_section']
    list_filter = ['title' , 'description' , 'direction_section']
    search_fields = ['title' , 'description']


@admin.register(CourseAnnouncement)
class CourseAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_title' , 'homepage' , ]
    list_filter = ['homepage' , 'section_title']
    search_fields = ['homepage__id' , 'section_title']
    inlines = [CourseAnnouncementCardInline]

@admin.register(CourseAnnouncementCard)
class CourseAnnouncementCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'course_announcement']
    list_filter = ['title' ,  'lector' , 'date' ,'description' , 'course_announcement']
    search_fields = ['title' , 'description']
