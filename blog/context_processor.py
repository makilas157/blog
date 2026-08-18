from .models import Category, SocialLink, AboutUs

def categories_processor(request):
    try:
        categories = Category.objects.all()
        return {'categories': categories}
    except:
        return {'categories': []}

def social_links_processor(request):
    try:
        social_links = SocialLink.objects.all()
        return {'social_links': social_links}
    except:
        return {'social_links': []}

def about_processor(request):
    try:
        about = AboutUs.objects.first()
        return {'about': about}
    except:
        return {'about': None}