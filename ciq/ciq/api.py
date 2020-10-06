from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, PostViewSet
from api.models import Author, Post
from rest_framework_extensions.routers import ( ExtendedSimpleRouter as SimpleRouter)
from rest_framework_extensions.routers import NestedRouterMixin
 
 
#router = DefaultRouter()
router = SimpleRouter()
 
router.register('authors', AuthorViewSet)
router.register('posts', PostViewSet)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

posts_router = router.register('posts', PostViewSet)
authors_router = router.register('authors', AuthorViewSet)
authors_router.register(
    'posts', 
   PostViewSet, 
   basename='posts', 
   parents_query_lookups=['author'])