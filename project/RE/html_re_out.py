#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-6-1 上午11:07
# Author:张印
# Desc：
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'starpro.settings'
django.setup()
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass