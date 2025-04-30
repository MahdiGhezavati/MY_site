from django.contrib import messages


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.add_message(self.request , messages.SUCCESS , "Check your email and use the password reset link" , extra_tags="succ")

        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
