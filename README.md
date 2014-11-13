django-hideshowpassword
=======================

Provides an easy to use field class for implementing CloudFour's
[hideShowPassowrd](https://github.com/cloudfour/hideShowPassword) jQuery
plugin.

Install
-------

Currently the package is not on PyPi, so you'll have to do it the long way:

```
pip install -e git+https://github.com/fizzmint/django-hideshowpassword#egg=hideshowpassword
```

Then add it to your INSTALLED_APPS tuple in settings.py:

```
INSTALLED_APPS = (
    ...
    'hideshowpassword',
    ...
)
```

Usage
-----

Just override a field input widget with the widget from hideshowpassword.widgets:

```
from django import forms
from hideshowpassword.widgets import HideShowInput

class MyUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':True}))
    password = forms.PasswordField(label="Let the world see my password!", widget=HideShowInput(render_value=True))
```

You'll also want to make sure to include the requisite form media in your
template using something like:

```
<form>
  {{form.media}}
  {{form.as_p}}
</form>
```

And that's it!

