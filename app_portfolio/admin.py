from django.contrib import admin
from . models import *

from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.
class ContentView(admin.ModelAdmin):
    
    formfield_overrides = {
        
        models.TextField: {'widget': TinyMCE(
            attrs={'cols': 80, 'rows': 30},
            mce_attrs={
                'plugins': 'advlist autolink lists link image charmap print preview hr anchor pagebreak',
                'toolbar': 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | charmap | preview',
                'image_advtab': True,
                'media_alt_source': True,
                'content_css': '/static/css/custom-tinymce.css',
                'file_picker_types': 'file image media',
                'file_picker_callback': 'function(callback, value, meta) { tinymce.activeEditor.windowManager.open({ title: "File Manager", file: "/file-manager/tinymce5", width: 800, height: 600, resizable: "yes", close_previous: "no", onMessage: function(api, message) { callback(message.content); } }); }'
            }
        )}
    }
admin.site.register(About_me)
admin.site.register(Services)
admin.site.register(My_works)
admin.site.register(Post_type)
admin.site.register(Post, ContentView)
admin.site.register(Testimonial)
admin.site.register(Guest_message)
admin.site.register(Comment)