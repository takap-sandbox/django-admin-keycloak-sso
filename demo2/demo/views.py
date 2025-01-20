from django.views.generic.base import View
from allauth.socialaccount.providers.openid_connect.views import OpenIDConnectOAuth2Adapter

class GoToAdminView(View):
    def get(self, *args, **kwargs):
        return OpenIDConnectOAuth2Adapter(self.request, provider_id='openid_connect').get_provider().redirect(self.request, process='login', next_url='/admin')
