from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from relationship_app.permissions import is_admin

class AdminView(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return is_admin(self.request.user)
