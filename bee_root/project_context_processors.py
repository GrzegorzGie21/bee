from django.utils import timezone
from django.conf import settings

import os


def get_cuurent_git_version():
    git_cmd = 'git describe --tags $(git rev-list --tags --max-count=1)'
    result = os.popen(git_cmd)
    version = result.read().strip()
    return version[1:]


def footer_cp(request):
    context = {'time': timezone.now(),
               'version': get_cuurent_git_version()}
    return context
