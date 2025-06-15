from rest_framework import viewsets
from cart.views       import CartView
from favorites.views  import FavoritesView
from contact.views    import ContactMessageView
from orders.views     import UserReviewsView

class SingleActionViewSet(viewsets.ViewSet):
    """
    Позволяет зарегистрировать APIView как ViewSet с одним действием.
    Указываем в router.basename нужный URL-путь.
    """
    view = None    # класс APIView

    def list(self, request, *args, **kwargs):
        # GET → UserReviewsView.get(), CartView.get() и т.д.
        return self.view.as_view({'get': 'get'})(request._request)

    def create(self, request, *args, **kwargs):
        # POST → ContactMessageView.post() и т.д.
        return self.view.as_view({'post': 'post'})(request._request)

class CartViewSet(SingleActionViewSet):
    view = CartView

class FavoritesViewSet(SingleActionViewSet):
    view = FavoritesView

class ContactViewSet(SingleActionViewSet):
    view = ContactMessageView

class ReviewsViewSet(SingleActionViewSet):
    view = UserReviewsView
