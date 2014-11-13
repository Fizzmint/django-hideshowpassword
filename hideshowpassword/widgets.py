from django.forms import widgets

class ShowHideInput(forms.PasswordInput):
    class Media:
        css =  {
            'all': ('css/hideShowPassword.css',) }
        js = ('js/hideShowPassword.min.js',)