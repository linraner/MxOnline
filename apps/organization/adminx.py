import xadmin


from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc", "add_time"]
    list_filter = ["name", "desc", "add_time"]


class CourseOrgAdmin(object):
    list_display = ["name", "desc",]
    search_fields = ["name", "tag", "city", ]
    list_filter = ["name", "tag", "city",]


class TeacherAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)