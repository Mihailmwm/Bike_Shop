# # bike_parts_shop/api_viewsets.py
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from cart.views import CartView
# from contact.views import ContactMessageView
# from orders.views import UserReviewsView

# class SingleActionViewSet(viewsets.ViewSet):
#     view = None
#     permission_classes = [IsAuthenticated]

#     def dispatch_view(self, request, method_name, *args, **kwargs):
#         view_func = self.view.as_view()
#         return view_func(request, *args, **kwargs)

#     def list(self, request, *args, **kwargs):
#         return self.dispatch_view(request, 'get', *args, **kwargs)

#     def create(self, request, *args, **kwargs):
#         return self.dispatch_view(request, 'post', *args, **kwargs)

#     def destroy(self, request, pk=None, *args, **kwargs):
#         request.parser_context = {'kwargs': {'product_pk': pk}}
#         return self.view.as_view()(request, product_pk=pk)

# class CartViewSet(SingleActionViewSet):
#     view = CartView

# class ContactViewSet(SingleActionViewSet):
#     view = ContactMessageView

# class ReviewsViewSet(SingleActionViewSet):
#     view = UserReviewsView

# bike_parts_shop/api_viewsets.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cart.views import CartView
from contact.views import ContactMessageView
from orders.views import UserReviewsView
from rest_framework.exceptions import MethodNotAllowed


class SingleActionViewSet(viewsets.ViewSet):
    """
    Обертка для подключения DRF APIView к ViewSet.
    """
    view = None
    permission_classes = [IsAuthenticated]

    def dispatch_view(self, request, method_name, *args, **kwargs):
        """
        Внутренний метод для вызова нужного метода APIView (get, post, delete и т.п.)
        """
        view_instance = self.view()
        handler = getattr(view_instance, method_name, None)

        if not handler:
            raise MethodNotAllowed(method_name.upper())

        return handler(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return self.dispatch_view(request, 'get', *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return self.dispatch_view(request, 'post', *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        # Для DELETE /api/cart/{product_pk}/
        return self.view().delete(request, product_pk=pk)


class CartViewSet(SingleActionViewSet):
    view = CartView


class ContactViewSet(SingleActionViewSet):
    view = ContactMessageView


class ReviewsViewSet(SingleActionViewSet):
    view = UserReviewsView
