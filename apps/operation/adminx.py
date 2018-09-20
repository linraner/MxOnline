import xadmin


from .models import UserAsk, CourseComments, UserFavorite, UserCourse, UserMessage


class UserAskAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


class CourseCommentsAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


class UserFavoriteAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


class UserCourseAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


class UserMessageAdmin(object):
    list_display = []
    search_fields = []
    list_filter = []


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)