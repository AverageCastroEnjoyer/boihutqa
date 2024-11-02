# cart/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItems
from bookstore.models import Book

def get_cart(session):
    # Helper function to retrieve or create a cart
    cart, created = Cart.objects.get_or_create(cart_session=session)
    return cart

def cart(request):
    session = request.session.session_key or request.session.create()
    cart_num = get_cart(session)  # Use the helper to get or create the cart
    cart_items = CartItems.objects.filter(cart=cart_num)
    total = sum(item.book.price * item.quantity for item in cart_items)
    
    return render(request, "cart.html", {"cart_items": cart_items, "total": total})

def add_to_cart(request, user_book):
    session = request.session.session_key or request.session.create()
    cart = get_cart(session)  # Retrieve or create cart
    
    book = get_object_or_404(Book, slug=user_book)
    cart_item, created = CartItems.objects.get_or_create(
        cart=cart, book=book,
        defaults={"quantity": 1, "is_active": True}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Update stock
    if book.stocks > 0:
        book.stocks -= 1
        book.save()
        
    return redirect('cart')

def update_cart_item(request, book_slug):
    session = request.session.session_key or request.session.create()
    cart = get_cart(session)  # Retrieve or create cart
    book = get_object_or_404(Book, slug=book_slug)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity < 1:
        return redirect('cart')
    
    cart_item = CartItems.objects.get(cart=cart, book=book)
    cart_item.quantity = quantity
    cart_item.save()
    
    return redirect('cart')

def delete_cart_item(request, book_slug):
    session = request.session.session_key or request.session.create()
    cart = get_cart(session)  # Retrieve or create cart
    book = get_object_or_404(Book, slug=book_slug)
    CartItems.objects.filter(cart=cart, book=book).delete()
    return redirect('cart')
