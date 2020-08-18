from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _
from . import forms


PLACEHOLDER_SIGN_IN = ["email", "password"]
PLACEHOLDER_SIGN_UP = ["email", "mobile", "password", "password-confirm"]
PLACEHOLDER_PASSWORD_RESET = ["password", "password-new", "password-new-confirm"]
PLACEHOLDER_PASSWORD_FORGOT = ["email"]
PLACEHOLDER_UPDATE_INFORMATION = ["email", "mobile", "id_365", "password_365"]
SELECT_UPDATE_INFORMATION = ["role"]


class SignInView(FormView):
    form = forms.SignInForm
    template_name = 'account/sign_in.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        # apply automatic translation according to user language
        for field in form:
            if field.label in PLACEHOLDER_SIGN_IN:
                form.fields[field.name].widget.attrs['placeholder'] = _(
                    form.fields[field.name].widget.attrs['placeholder'])

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(initial=request.POST)

        if form.is_valid():
            # update using the data received through the post of the request
            # TODO: update using the data received through the post of the request
            pass

        return HttpResponseRedirect(reverse('account:profile'))


class PasswordResetView(FormView):
    form = forms.PasswordResetForm
    template_name = 'account/password_reset.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        # apply automatic translation according to user language
        for field in form:
            if field.label in PLACEHOLDER_PASSWORD_RESET:
                form.fields[field.name].widget.attrs['placeholder'] = _(
                    form.fields[field.name].widget.attrs['placeholder'])

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(initial=request.POST)

        if form.is_valid():
            # update using the data received through the post of the request
            # TODO: update using the data received through the post of the request
            # TODO: create a temporary password and change the password
            # TODO: send temporary password and password reset url by e-mail
            pass

        return HttpResponseRedirect(reverse('account:sign_in'))


class PasswordForgotView(FormView):
    form = forms.PasswordForgotForm
    template_name = 'account/password_forgot.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        # apply automatic translation according to user language
        for field in form:
            if field.label in PLACEHOLDER_PASSWORD_FORGOT:
                form.fields[field.name].widget.attrs['placeholder'] = _(
                    form.fields[field.name].widget.attrs['placeholder'])

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(initial=request.POST)

        if form.is_valid():
            # update using the data received through the post of the request
            # TODO: update using the data received through the post of the request
            pass

        return HttpResponseRedirect(reverse('account:sign_in'))


class ProfileUpdateView(FormView):
    form = forms.UpdateProfileForm
    # get data from user and set into initial
    # TODO: get data form user and set into initial
    initial = {'first_name': 'First Name'}
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        # check permission and change 'disabled' attribute of each fields
        # TODO: check permission and change 'disabled' attribute of each fields
        # form.fields['permission_connectivity'].disabled = False
        # form.fields['role'].disabled = True
        # apply automatic translation according to user language
        for field in form:
            if field.label in PLACEHOLDER_UPDATE_INFORMATION:
                form.fields[field.name].widget.attrs['placeholder'] = _(
                    form.fields[field.name].widget.attrs['placeholder'])

        return render(request, self.template_name,
                      {'form': form, 'placehold_fields': ",".join(PLACEHOLDER_UPDATE_INFORMATION),
                       'select_fields': ",".join(SELECT_UPDATE_INFORMATION)})

    def post(self, request, *args, **kwargs):
        form = self.form()

        for param in request.POST:
            if "permission" in param:
                permission_list = request.POST.getlist(param)
                for permission_type in permission_list:
                    print("permission", param, permission_type)
            elif "csrfmiddlewaretoken" in param:
                pass
            else:
                print("not permission", param, request.POST[param])

        if form.is_valid():
            # update using the data received through the post of the request
            # TODO: update using the data received through the post of the request
            print(request.POST)

        return HttpResponseRedirect(reverse('account:profile'))


class ProflieCreateView(FormView):
    form = forms.SignUpForm
    template_name = 'account/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        # apply automatic translation according to user language
        for field in form:
            if field.label in PLACEHOLDER_PASSWORD_FORGOT:
                form.fields[field.name].widget.attrs['placeholder'] = _(
                    form.fields[field.name].widget.attrs['placeholder'])

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form()

        if form.is_valid():
            # update using the data received through the post of the request
            # TODO: update using the data received through the post of the request
            print(request.POST)

        return HttpResponseRedirect(reverse('account:sign_in'))
