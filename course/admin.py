from django.contrib import admin
from .models import (
    Course,
    Section,
    CourseAttendance,
    CourseAssignToTeacher,
    CourseAssignToStudent,
    DailyAttendance
)


admin.site.register(Course)
admin.site.register(Section)
admin.site.register(CourseAttendance)
admin.site.register(CourseAssignToTeacher)
admin.site.register(CourseAssignToStudent)
admin.site.register(DailyAttendance)