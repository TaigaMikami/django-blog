from django.views import generic
from .models import Post

class IndexView(generic.ListView):
  # template_name = 'blog/post_list.html'
  model = Post

  def get_queryset(self):
    return Post.objects.order_by('-created_at')
