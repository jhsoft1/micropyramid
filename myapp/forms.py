from django import forms
from django.forms.models import modelformset_factory
from myapp.models import User, Group


class UserForm(forms.ModelForm):
    # birth_date = forms.DateField()  # widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}))

    class Meta:
        model = User
        exclude = ()

    def __init__(self, *args, **kwargs):
        self.businessprofile_id = kwargs.pop('businessprofile_id')
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['user_group'].queryset = Group.objects.filter(business_profile_id=self.businessprofile_id)


BaseUserFormSet = modelformset_factory(User, form=UserForm, extra=1, can_delete=True)


class UserFormSet(BaseUserFormSet):

    def __init__(self, *args, **kwargs):
        #  create a user attribute and take it out from kwargs
        # so it doesn't messes up with the other formset kwargs
        self.businessprofile_id = kwargs.pop('businessprofile_id')
        super(UserFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

    def _construct_form(self, *args, **kwargs):
        # inject user in each form on the formset
        kwargs['businessprofile_id'] = self.businessprofile_id
        return super(UserFormSet, self)._construct_form(*args, **kwargs)
