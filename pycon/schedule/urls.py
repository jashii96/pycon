from django.conf.urls import url, patterns


urlpatterns = patterns(
    "pycon.schedule.views",
    url(r"^sessions/staff.txt$", "session_staff_email", name="schedule_session_staff_email"),
    url(r"^sessions/$", "session_list", name="schedule_session_list"),
    url(r"^session/(\d+)/$", "session_detail", name="schedule_session_detail"),
    url(r"^session-staff.json", "session_staff_json", name="session_staff_json"),
    url(r"^slides_upload/(?P<presentation_id>[0-9,]+)/$", "slides_upload", name="pycon_schedule_slides_upload"),
    url(r"^slides_download/$", "slides_download", name="pycon_schedule_slides_download"),
)
