import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView, BaseListView
from ModuleCommon.models import Attorney, Student, Teacher, Administrative

