from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProducerProfileForm, ProductForm
from .models import ProducerProfile, Product


def producer_required(view_func):
    """
    Allow only users with PRODUCER role.
    Customers are redirected to home. Unauthenticated users go to login.
    """
    @login_required
    def _wrapped(request, *args, **kwargs):
        if request.user.profile.role != 'PRODUCER':
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped

# Sprint 1 placeholder – real orders from Person C (orders app) in Sprint 2
DUMMY_ORDERS = [
    {
        'id': 1,
        'customer': 'Alice Smith',
        'product': 'Organic Carrots',
        'quantity': 2,
        'unit': 'kg',
        'total': '£5.00',
        'date': '2026-03-01',
        'status': 'Pending',
    },
    {
        'id': 2,
        'customer': 'Bob Jones',
        'product': 'Free Range Eggs',
        'quantity': 1,
        'unit': 'dozen',
        'total': '£3.50',
        'date': '2026-03-02',
        'status': 'Processing',
    },
    {
        'id': 3,
        'customer': 'Carol White',
        'product': 'Fresh Milk',
        'quantity': 3,
        'unit': 'litre',
        'total': '£6.00',
        'date': '2026-03-02',
        'status': 'Pending',
    },
    {
        'id': 4,
        'customer': 'David Brown',
        'product': 'Sourdough Bread',
        'quantity': 2,
        'unit': 'unit',
        'total': '£8.00',
        'date': '2026-03-03',
        'status': 'Completed',
    },
]


def _get_producer_profile(request):
    """Return the ProducerProfile for the logged-in user, or None."""
    try:
        return request.user.producer_profile
    except ProducerProfile.DoesNotExist:
        return None


@login_required
def producer_register(request):
    """TC-002: Producer registration form (PRODUCER role only)."""
    if request.user.profile.role != 'PRODUCER':
        return redirect('home')
    if _get_producer_profile(request):
        return redirect('producers:dashboard')

    if request.method == 'POST':
        form = ProducerProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # Flip the core profile role to PRODUCER
            request.user.profile.role = 'PRODUCER'
            request.user.profile.save()
            return redirect('producers:dashboard')
    else:
        form = ProducerProfileForm()

    return render(request, 'producers/producer_register.html', {'form': form})


@producer_required
def dashboard(request):
    """Producer dashboard overview."""
    producer_profile = _get_producer_profile(request)
    if not producer_profile:
        return redirect('producers:producer_register')

    product_count = Product.objects.filter(producer=producer_profile).count()
    return render(request, 'producers/dashboard.html', {
        'producer_profile': producer_profile,
        'product_count': product_count,
    })


@producer_required
def product_list(request):
    """TC-003: List producer's own products."""
    producer_profile = _get_producer_profile(request)
    if not producer_profile:
        return redirect('producers:producer_register')

    products = Product.objects.filter(producer=producer_profile).select_related('category')
    return render(request, 'producers/product_list.html', {
        'products': products,
        'producer_profile': producer_profile,
    })


@producer_required
def product_create(request):
    """TC-003: Create a new product listing."""
    producer_profile = _get_producer_profile(request)
    if not producer_profile:
        return redirect('producers:producer_register')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.producer = producer_profile
            product.save()
            return redirect('producers:product_list')
    else:
        form = ProductForm()

    return render(request, 'producers/product_form.html', {
        'form': form,
        'action': 'Create',
    })


@producer_required
def product_edit(request, pk):
    """Edit an existing product."""
    producer_profile = _get_producer_profile(request)
    if not producer_profile:
        return redirect('producers:producer_register')

    product = get_object_or_404(Product, pk=pk, producer=producer_profile)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('producers:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'producers/product_form.html', {
        'form': form,
        'action': 'Edit',
        'product': product,
    })


@producer_required
def product_delete(request, pk):
    """Delete a product (POST only)."""
    producer_profile = _get_producer_profile(request)
    if not producer_profile:
        return redirect('producers:producer_register')

    product = get_object_or_404(Product, pk=pk, producer=producer_profile)
    if request.method == 'POST':
        product.delete()
    return redirect('producers:product_list')


@producer_required
def incoming_orders(request):
    """TC-009: Producer views incoming orders (dummy data placeholder for Sprint 1)."""
    producer_profile = _get_producer_profile(request)
    if not producer_profile:
        return redirect('producers:producer_register')

    return render(request, 'producers/incoming_orders.html', {
        'orders': DUMMY_ORDERS,
        'producer_profile': producer_profile,
    })
