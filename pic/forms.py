from django.forms import ModelForm, widgets
from .models import Pic, Review

class PicForm(ModelForm):
    class Meta:
        model = Pic
        fields = ['title', 'image' , 'description']
 
    def __init__(self, *args, **kwargs):
        super(PicForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm):
    class Meta:
        model =Review
        fields = ['value', 'body']
    
        labels = {
            'value':'Place your Vote',
            'body':'Add a comment with your vote'
        }
    def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})       