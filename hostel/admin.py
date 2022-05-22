from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.hostelInformationModel)
admin.site.register(models.hostelImagesModel)
admin.site.register(models.hostelMapModel)
admin.site.register(models.hostelAllocatedToYear)
admin.site.register(models.hostelPreferenceFirstYear)
admin.site.register(models.hostelPreferenceSecondYear)