from django.contrib import admin
from django import forms
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from api.models import ObjectType, ResourceType, Country,Object, Website,Result
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from urllib.parse import urlparse
admin.site.register(ObjectType)


class ChapterCountry(admin.ModelAdmin):
    search_fields=['name']


admin.site.register(Country,ChapterCountry)    
admin.site.register(ResourceType)
class BookResource(resources.ModelResource):
    class Meta:
        model = Object


class ResultInline(admin.StackedInline):
    model = Result
    exclude = ['user']
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

class YourInlineFormset(forms.models.BaseInlineFormSet):
    def save_new(self, form, commit=True):
        obj = super(YourInlineFormset, self).save_new(form, commit=False)
        # here you can add anything you need from the request
        obj.user = self.request.user
        if commit:
            obj.save()
        return obj
class WebsiteInline(admin.StackedInline):
    model = Website
    formset = YourInlineFormset
    fields=['url','rtype','user']
    readonly_fields=['user']
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(WebsiteInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

    def has_change_permission(self, request, obj=None):
         has_class_permission = super(WebsiteInline, self).has_change_permission(request, obj)
         if not has_class_permission:
             return False
         if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
             return False
         return True
    def has_delete_permission(self, request, obj=None):
        #has_class_permission = super(WebsiteInline, self).has_delete_permission(request, obj)
        #if not has_class_permission:
            #return False
        
        return False



class ResInline(admin.StackedInline):
    model = Result
    formset = YourInlineFormset
    readonly_fields=['user']

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(ResInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset
    def has_delete_permission(self, request, obj=None):
        has_class_permission = super(ResInline, self).has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True




class ChapterResult(admin.ModelAdmin):
    #readonly_fields=('html_stripped',)
    search_fields=['website__url']
    exclude = ['user']
    list_filter=['user','website__object__country__name','positive','created_at']
    list_display=['website','user','positive','created_at','updated_at']
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    def has_delete_permission(self, request, obj=None):
        has_class_permission = super(ChapterResult, self).has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True
    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(ChapterResult, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
    #         return False
    #     return True
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    # def get_form(self, request, obj=None, **kwargs):
    #     if request.user.is_superuser:
    #         fields = ['approved']
    #         if self.declared_fieldsets:
    #             fields += flatten_fieldsets(self.declared_fieldsets)

    #         # Update the keyword args as needed to allow the parent to build 
    #         # and return the ModelForm instance you require for the user given their perms
    #         kwargs.update({'fields': fields})
    #     return super(PostAdmin, self).get_form(request, obj=None, **kwargs)
    
class MyArticleAdminForm(forms.ModelForm):
    def clean_url(self):
        url = self.cleaned_data['url']
        if Website.objects.filter(url=urlparse(url).netloc).exists():
         raise forms.ValidationError('Bu sayt kiritilgan!')
        if urlparse(url).netloc=='':
         raise forms.ValidationError("Noto'g'ri sayt!")

        return url  


class ChapterWebsite(admin.ModelAdmin):
    inlines=[ResInline]
    search_fields=['url']
    exclude = ['user']
    form=MyArticleAdminForm
    list_filter=['user','object__country__name','rtype__name','object__obtype__name','created_at']
    list_display=['url','country','user','rtype','created_at']
    autocomplete_fields=['country']
    def country(self, obj):
        return obj.object.country
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.url=urlparse(obj.url).netloc
            print("URLLLLLLLLLLLLLLLLLL")
            print(obj.url)
        else:
            obj.url=urlparse(obj.url).netloc
        obj.save()
    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(ChapterWebsite, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
    #         return False
    #     return True
    def has_delete_permission(self, request, obj=None):
        has_class_permission = super(ChapterWebsite, self).has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True
class MyArticleAdminForm(forms.ModelForm):
    def clean_url(self):
        
        return self.cleaned_data["url"]

class ChapterAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_filter=['created_at','obtype']
    resource_class = BookResource
    inlines = [WebsiteInline]
    form = MyArticleAdminForm
    list_display = ('country', 'obtype','name','user','created_at','updated_at')
    def name(self):
        return 'Davlat'
    name.short_description='Davlat'
    exclude = ['user']
    def get_queryset(self, request):
       # if request.user.is_superuser:
            return Object.objects.all()
       # return Object.objects.filter(user=request.user)
    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(ChapterAdmin, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
    #         return False
    #     return True
    def has_delete_permission(self, request, obj=None):
         has_class_permission = super(ChapterAdmin, self).has_delete_permission(request, obj)
         if not has_class_permission:
             return False
         if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
             return False
         return True
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

    


admin.site.register(Object,ChapterAdmin)
admin.site.register(Website,ChapterWebsite)
admin.site.register(Result,ChapterResult)
#admin.site.register(Object,BookAdmin)
# Register your models here.
