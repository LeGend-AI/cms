from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView

from .models import MemberProfile
from .forms import CreateUserForm

class MemberListView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'member_list'
  model = MemberProfile

class SignUpView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('members:login')
    form_class = CreateUserForm
    template_name = "member_sign_up_form.html"

    def form_valid(self, form):
        c = {'form': form, }
        user = form.save(commit=False)
        # Cleaned(normalized) data
        organization = form.cleaned_data['organization']
        title = form.cleaned_data['title']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()

        # Create UserProfile model
        UserProfile.objects.create(user=user, phone_number=phone_number, date_of_birth=date_of_birth)

        return super(CreateUserView, self).form_valid(form)
