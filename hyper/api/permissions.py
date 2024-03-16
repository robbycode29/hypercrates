# from django.shortcuts import get_object_or_404
from rest_framework import permissions
from django.contrib.auth.models import Group, User

class IsGeneralManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='General Manager').exists()

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Doctor').exists() or request.user.groups.filter(name='General Manager').exists()

class IsAssistant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Assistant').exists()
    
group_doctor, created = Group.objects.get_or_create(name='Doctor')
group_assistant, created = Group.objects.get_or_create(name='Assistant')
group_gm, created = Group.objects.get_or_create(name='General Manager')

user = User.objects.get(username='trroop')
user.groups.add(group_gm)