from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    address = forms.CharField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass