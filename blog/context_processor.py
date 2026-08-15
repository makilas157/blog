from .models import Category, SocialLink

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