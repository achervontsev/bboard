from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('accounts/login/', views.BBLoginView.as_view(), name='login'),
    path('accounts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', views.BBPasswordChangeView.as_view(),
                                      name='password_change'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(),
                                            name='profile_change'),
    path('accounts/profile/', views.profile, name='profile'),
    path('<str:page>/', views.other_page, name='other'),
    path('', views.index, name='index'),
]
