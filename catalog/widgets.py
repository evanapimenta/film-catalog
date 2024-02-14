from django.forms import ClearableFileInput
from django.utils.safestring import mark_safe

class DefaultImageFileInput(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if not value:
            default_image_url = 'catalog/no-image.jpg'
            output += mark_safe(f'<img src="{default_image_url}" alt="Default Image" style="max-width: 100px; max-height: 100px;">')
        return output