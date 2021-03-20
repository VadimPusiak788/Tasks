from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post, Comment
from django.http import HttpResponseForbidden
from .forms import PostForm, CommentForm
from django.http import Http404


class PostCreateView(CreateView):
    template_name = 'post/create_post.html'
    form_class = PostForm
    success_url = '../posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'post/list_post.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()

        if self.request.user.is_authenticated:
            context['form'] = CommentForm(instance=self.request.user)
            context['list_comment'] = Comment.objects.select_related("post_comment").filter(post_comment_id=self.object.pk)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        new_comment = Comment(
            comments=request.POST.get('comments'),
            author=self.request.user,
            post_comment=self.get_object()
        )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class CommentView(CreateView):
    template_name = 'post/post_detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.object.pk


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'photo', 'description']
    template_name_suffix = '_update_form'

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author != self.request.user:
            raise Http404("Don't permission")
        return obj

