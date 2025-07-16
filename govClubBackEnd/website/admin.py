from django.contrib import admin

from django.contrib import admin
from .models import Mission, MissionCard, MissionSubsection, Direction, DirectionCard, CourseAnnouncementCard, \
    CourseAnnouncement, Hero, CourseDetail, AboutCourse, CourseCurator, HeroSectionCourse, PhotoCourse


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


class HeroSectionCourseInline(admin.TabularInline):
    model = HeroSectionCourse
    extra = 1
    show_change_link = True


class CourseCuratorInline(admin.TabularInline):
    model = CourseCurator
    extra = 1
    show_change_link = True

class AboutCourseInline(admin.TabularInline):
    model = AboutCourse
    extra = 1
    show_change_link = True

class PhotoCourseInline(admin.TabularInline):
    model = PhotoCourse
    extra = 1
    show_change_link = True



# website_course-detail


@admin.register(Hero)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'homepage', 'title_part1', 'title_part2', 'description']
    list_filter = ['id', 'homepage', 'title_part1', 'title_part2', 'description']
    search_fields = ['homepage__id', 'title_part1', 'title_part2', 'description']


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
    list_display = ['id', 'section_title', 'homepage', ]
    list_filter = ['homepage', 'section_title']
    search_fields = ['homepage__id', 'section_title']
    inlines = [DirectionCardInline]


@admin.register(DirectionCard)
class DirectionCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'direction_section']
    list_filter = ['title', 'description', 'direction_section']
    search_fields = ['title', 'description']


@admin.register(CourseAnnouncement)
class CourseAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_title', 'homepage', ]
    list_filter = ['homepage', 'section_title']
    search_fields = ['homepage__id', 'section_title']
    inlines = [CourseAnnouncementCardInline]


@admin.register(CourseAnnouncementCard)
class CourseAnnouncementCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'description', 'course_announcement']
    list_filter = ['title', 'lector', 'date', 'description', 'course_announcement']
    search_fields = ['title', 'description']


@admin.register(CourseDetail)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'card_id']
    list_filter = ['id', 'card_id']
    search_fields = ['id', 'card_id']
    inlines = [HeroSectionCourseInline ,CourseCuratorInline ,AboutCourseInline ,  PhotoCourseInline ]


@admin.register(HeroSectionCourse)
class HeroSectionCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'image', 'section_title']
    list_filter = ['id', 'date', 'image', 'section_title']
    search_fields = ['id', 'date', 'image', 'section_title']

@admin.register(CourseCurator)
class CourseCuratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_title', 'image', 'description' ]
    list_filter = ['id', 'section_title', 'image', 'description' ]
    search_fields = ['id', 'section_title', 'image', 'description' ]

@admin.register(AboutCourse)
class CourseCuratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_title', 'description' ]
    list_filter = ['id', 'section_title', 'description' ]
    search_fields = ['id', 'section_title', 'description' ]


@admin.register(PhotoCourse)
class PhotoCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_filter = ['id', 'image']
    search_fields = ['id', 'image']
