from django import forms

class HideShowInput(forms.PasswordInput):
    class Media:
        css =  {
            'all': ('css/hideShowPassword.css',) }
        js = ('js/hideShowPassword.min.js', 
              'js/hideshow_custom.js')