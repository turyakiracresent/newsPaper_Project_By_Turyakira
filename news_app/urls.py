from django .urls import path
# from .views  import newsView
from .views import HomePageView, AboutPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Maps the root URL to the newsView function
    path('about/', AboutPageView.as_view(), name='about'),  # Maps the about URL to the AboutPageView
]