from django.contrib import admin


from .models import Article, Comment, Tag
# Register your models here.

'''
def changetitle(modeladmin, request, queryset):
    queryset.update(title='lalala')    message_bit = 1
    self.message_user(request, "%s successfully marked as published." % message_bit)
changetitle.short_description = 'Başlığı lalala et!'
'''
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'created_date')
    list_filter = ('created_date','tags')
    autocomplete_fields =['author']
    search_fields = ['^title','author__username']
    #actions = [changetitle]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','author', 'created_date')
    list_filter = ('created_date',)
    autocomplete_fields =['author','article']
    search_fields = ['^article','author__username']

admin.site.register(Tag)