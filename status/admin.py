from django.contrib import admin

from status.models import Project, Contact
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)

        if request.user.is_superuser:
                return qs

        return qs.filter(owner=request.user)


    def save_model(self, request, obj, form, change):

        if(not change):
            obj.owner = request.user

        obj.save()


admin.site.register(Contact)
admin.site.register(Project, ProjectAdmin)
