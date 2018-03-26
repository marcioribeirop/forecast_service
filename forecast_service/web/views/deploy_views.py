from pyramid.view import view_config
from forecast_service.utils.object_retriever import ModelRetriever
from forecast_service.web.views.error_views import generate_bad_request


@view_config(request_method='GET', route_name='deploy_model', renderer='json')
def deploy_model_view(request):

    try:
        instance_info = request.matchdict

        ModelRetriever.search_model(app=instance_info['app'], model_name=instance_info['model_name'],
                                    version=instance_info['version'])

        return {"model": instance_info['model_name'],
                "version": instance_info['version'],
                "app": instance_info['app'],
                "status": "Ready"}

    except:
        response = generate_bad_request()
        return response


@view_config(request_method='GET', route_name='deploy_model.client', renderer='json')
def deploy_model_client_view(request):

    try:
        instance_info = request.matchdict

        ModelRetriever.search_model(app=instance_info['app'], model_name=instance_info['model_name'],
                                    version=instance_info['version'], client=instance_info['client'])

        return {"model": instance_info['model_name'],
                "version": instance_info['version'],
                "app": instance_info['app'],
                "client": instance_info['client'],
                "status": "Ready"}

    except:
        response = generate_bad_request()
        return response


@view_config(request_method='GET', route_name='deploy_model.client.product', renderer='json')
def deploy_model_client_product_view(request):

    try:
        instance_info = request.matchdict

        ModelRetriever.search_model(app=instance_info['app'], model_name=instance_info['model_name'],
                                    version=instance_info['version'], client=instance_info['client'],
                                    product=instance_info['product'])

        return {"model": instance_info['model_name'],
                "version": instance_info['version'],
                "app": instance_info['app'],
                "client": instance_info['client'],
                "product": instance_info['product'],
                "status": "Ready"}
    except:
        response = generate_bad_request()
        return response