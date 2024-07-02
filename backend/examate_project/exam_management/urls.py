from django.urls import path
from .views import (
    ExamCreationView,
    ExamUpdationView,
    ExamDetailView,
    ExamListView,
    SoftDeleteView,
    EndUserExamView,
    ExamSubjectsListView,
    FeedbackAPIView,
    ExamSubjectTimeDurationView,
    ExamScheduledTimeView,
    ExamQuestionView,
    RegenarateQuestionView,
    SubjectPopularityView,
    ExamDetailViews,
    PendingEvaluationListView,
    DownloadMarkListView,
    ExamCountAPIView,
    DashboardExamListAPIView,
    ExamCancelAPIView,
)


urlpatterns = [
    path("create-exam/", ExamCreationView.as_view(), name="create-exam"),
    path("exam-list/", ExamListView.as_view(), name="exam-list"),
    path("exam-delete/<int:pk>/", SoftDeleteView.as_view(), name="delete-exam"),
    path("update-exam/<int:pk>/", ExamUpdationView.as_view(), name="update-exam"),
    path("exam-detail/<int:examid>/", ExamDetailView.as_view(), name="exam-details"),
    path("exam-detail/<str:token>/", EndUserExamView.as_view(), name="exam-details-token"),
    path("exam-subjects/<int:exam_id>/",ExamSubjectsListView.as_view(),name="exam-subjects-list",),
    path("exam-data/<int:exam_subject_id>/",ExamSubjectTimeDurationView.as_view(),name="exam-data",),
    path("exam-time/<int:exam_id>/",ExamScheduledTimeView.as_view(),name="exam-schedule",),
    path("exam-feedback/", FeedbackAPIView.as_view(), name="exam-feedback"),
    path('exam-feedback/<int:exam_id>/', FeedbackAPIView.as_view(), name='exam-feedback-detail'),
    path("exam-questions/<int:exam_subject_id>/",ExamQuestionView.as_view(),name="exam-questions",),
    path("regenarate-questions/<int:exam_id>/<int:subject_id>/",RegenarateQuestionView.as_view(),name="regenarate-questions",),
    path("subject-popularity/",SubjectPopularityView.as_view(),name="subject-popularity", ),
    path("exam-details/<int:examid>/", ExamDetailViews.as_view(), name="exam-details"),
    path("exam-detail/", EndUserExamView.as_view(), name="exam-details-token"),
    path( "pending-evaluation-list/", PendingEvaluationListView.as_view(),name="pending-evaluation-list",),
    path("download-mark-list/<int:exam_id>/",DownloadMarkListView.as_view(),name="download_mark_list",),
    path("exam-count",ExamCountAPIView.as_view(),name="exam-count"),
    path('dasboardExamList/<str:status>/', DashboardExamListAPIView.as_view(), name='dashboard-exam-list'),
    path("exam-cancel/<int:exam_id>/", ExamCancelAPIView.as_view(), name="exam-cancel"),
]
