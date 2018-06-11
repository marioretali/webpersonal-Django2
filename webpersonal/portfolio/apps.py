from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    name = 'portfolio'
    verbose_name = 'Portafolio' #es el nombre publico que va a aparecer(para que funcione luego hay que ir al archivo settings y en la parte de INSTALLED_APPS modificar la app portfolio por: 'portfolio.apss.PortfolioConfig',)
