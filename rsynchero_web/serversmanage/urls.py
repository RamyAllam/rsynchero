from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'serversmanage'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^server/(?P<pk>[0-9]+)/$', views.ServerInfo.as_view(), name='serverinfo'),
    url(r'^serveradd/$', views.ServerAdd.as_view(), name='serveradd'),
    url(r'^server/(?P<pk>[0-9]+)/edit/$', views.ServerUpdate.as_view(), name='serveredit'),
    url(r'^server/(?P<pk>[0-9]+)/delete/$', views.ServerDelete.as_view(), name='serverdelete'),
    url(r'^runbackup/$', views.request_page_cmd, name='runcommand'),
    url(r'^server/(?P<server_id>[0-9]+)/list_backup/$', views.list_backup, name='list_backup'),
    url(r'^server/(?P<server_id>[0-9]+)/view_logs/$', views.view_logs, name='view_logs'),
    url(r'^server/(?P<server_id>[0-9]+)/test_ssh/$', views.test_ssh, name='test_ssh'),
    url(r'^server/(?P<server_id>[0-9]+)/view_running_jobs/$', views.view_running_jobs, name='view_running_jobs'),
    url(r'^server/(?P<server_id>[0-9]+)/kill_running_jobs/$', views.kill_running_jobs, name='kill_running_jobs'),
    url(r'^server/(?P<server_id>[0-9]+)/restore_backup.*$', views.restore_backup, name='restore_backup'),
    url(r'^server/(?P<server_id>[0-9]+)/disable/$', views.serverdisable, name='serverdisable'),
    url(r'^server/(?P<server_id>[0-9]+)/enable/$', views.serverenable, name='serverenable'),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
]