from .models import SeoSettings, SiteSettings, SocialNetworks, TelegramBotConfig

def seo_settings(request):
    try:
        seo = SeoSettings.objects.last()
    except SeoSettings.DoesNotExist:
        seo = None
    return {
        'seo_settings': seo
    }

def site_settings(request):
    try:
        site = SiteSettings.objects.last()
    except SiteSettings.DoesNotExist:
        site = None
    return {
        'site_settings': site
    }

def social_networks(request):
    networks = SocialNetworks.objects.all()
    return {
        'social_networks': networks
    }

def telegram_bot_config(request):
    try:
        bot_config = TelegramBotConfig.objects.last()
    except TelegramBotConfig.DoesNotExist:
        bot_config = None
    return {
        'telegram_bot_config': bot_config
    }
