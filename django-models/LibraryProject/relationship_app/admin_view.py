from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class AdminView(UserPassesTestMixin, TemplateView):
    template_name = "admin_view.html"
    login_url = "/custom-login/"  # Optional custom redirect

    def test_func(self):
        return hasattr(self.request.user, "userprofile") and self.request.user.userprofile.role == "Admin"