from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import MemberProfile
from .forms import CreateUserForm

class MemberListView(generic.ListView):
  template_name = 'members/member_list.html'
  context_object_name = 'members'

  def get_queryset(self):
      return MemberProfile.objects.filter(user__is_active=True)

class SignUpView(CreateView):
    form_class = CreateUserForm
    template_name = "members/member_sign_up_form.html"
    success_url = reverse_lazy('members:list')

    def form_valid(self, form):
        c = {'form': form, }
        user = form.save(commit=False)
        # Cleaned(normalized) data
        organization = form.cleaned_data['organization']
        title = form.cleaned_data['title']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.is_active = False
        user.save()

        # Create UserProfile model
        MemberProfile.objects.create(user=user, organization=organization, title=title)

        return super(SignUpView, self).form_valid(form)
