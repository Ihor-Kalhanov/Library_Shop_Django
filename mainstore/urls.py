from rest_framework.routers import SimpleRouter

from mainstore.views import BookViewSet, UserBooksRelationView, UserViewSet

router = SimpleRouter( )
router.register(r'books', BookViewSet)
router.register(r'book_relation', UserBooksRelationView)
router.register('users', UserViewSet)


urlpatterns = router.urls
