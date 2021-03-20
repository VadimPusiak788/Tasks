from django.contrib import admin
from .models import Post, Comment
from django.http import HttpResponseRedirect


class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/post/rule/change_form.html'

    def response_change(self, request, obj):
        if "_make-delete" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(title=obj.title).exclude(pk=obj.id)
            matching_names_except_this.delete()
            Comment.objects.filter(post_comment_id=obj.id).delete()
            obj.save()
            self.message_user(request, "Delete all comments for this post")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)