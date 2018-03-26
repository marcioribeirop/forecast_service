from pyramid.config import Configurator
from forecast_service.utils import generate_global


def add_product(config):
    config.add_route('base.client.product', '/{product}')


def add_client(config):
    config.add_route('base.client', '/{client}')
    config.include(add_product, route_prefix='/{client}')


def add_product_deploy(config):
    config.add_route('deploy_model.client.product', '/{product}')


def add_client_deploy(config):
    config.add_route('deploy_model.client', '/{client}')
    config.include(add_product_deploy, route_prefix='/{client}')


def add_product_template(config):
    config.add_route('data_template.client.product', '/{product}')


def add_client_template(config):
    config.add_route('data_template.client', '/{client}')
    config.include(add_product_template, route_prefix='/{client}')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    generate_global.init()

    config = Configurator(settings=settings)

    config.add_route('base', '/forecast/{app}/{model_name}/{version}')
    config.include(add_client, route_prefix='/forecast/{app}/{model_name}/{version}')

    config.add_route('deploy_model', '/deploy_model/{app}/{model_name}/{version}')
    config.include(add_client_deploy, route_prefix='/deploy_model/{app}/{model_name}/{version}')

    config.add_route('data_template', '/data_template/{app}/{model_name}/{version}')
    config.include(add_client_template, route_prefix='/data_template/{app}/{model_name}/{version}')

    config.scan()
    return config.make_wsgi_app()