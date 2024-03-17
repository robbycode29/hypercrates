from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import DoctorViewSet, PatientViewSet, AssistantViewSet, TreatmentViewSet, DoctorPatientTreatmentsView, PatientAssistantView, TreatmentAssistantView, PatientTreatmentsReportView, DoctorsPatientsReportView

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'assistants', AssistantViewSet)
router.register(r'treatments', TreatmentViewSet)
router.register(r'doctors/(?P<doctor_id>[^/.]+)/patients/(?P<patient_id>[^/.]+)/treatments', DoctorPatientTreatmentsView, basename='doctor_patient_treatments')
router.register(r'patients/(?P<patient_id>[^/.]+)/treatments/report', PatientTreatmentsReportView, basename='patient_treatments_report')
router.register(r'report', DoctorsPatientsReportView, basename='report')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('patients/<int:pk>/assistants/', PatientAssistantView.as_view({'put': 'update', 'get': 'retrieve'})),
    path('treatments/<int:pk>/assistant/', TreatmentAssistantView.as_view({'put': 'update', 'get': 'retrieve'})),
]