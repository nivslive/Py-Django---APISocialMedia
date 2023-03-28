from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from comment.admin import Comment
from post.admin import Post
#
class MyAdminSite(AdminSite):
    site_title = 'Meu Site Admin'
    site_header = 'Yorus Admin'
    def __init__(self, name='admin'):
        super().__init__(name=name)
        # Registre a instância de UserAdmin com a instância personalizada do admin
        self.register(User, UserAdmin)
        self.register(Group, GroupAdmin)
        self.register(Permission)
        self.register(Comment)
        self.register(Post)

        