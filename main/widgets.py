from django.forms.widgets import Widget

class PlusMinusNumberInput(Widget):
    template_name = 'widgets/plusminusnumber.html'
    
    class Meta:
        css = {
            'all': ('css/plusminusnumber.css',)
        }
        js = ('js/plusminusnumber.js',)