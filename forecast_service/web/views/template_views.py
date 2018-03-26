from pyramid.view import view_config
from forecast_service.utils.object_retriever import ModelRetriever
from forecast_service.web.views.error_views import generate_bad_request


@view_config(request_method='GET', route_name='data_template', renderer='json')
def data_template_view(request):

    try:
        from dbhelper.main.dbhelper import HelperRuntime

        helper = HelperRuntime()

        model_retrieved = ModelRetriever.get_model(app=request.matchdict.get("app"),
                                                   model_name=request.matchdict.get("model_name"),
                                                   version=request.matchdict.get("version"))

        return model_retrieved.io_template

    except:
        response = generate_bad_request()
        return response


@view_config(request_method='GET', route_name='data_template.client', renderer='json')
def data_template_client_view(request):

    try:
        from dbhelper.main.dbhelper import HelperRuntime

        helper = HelperRuntime()

        model_retrieved = ModelRetriever.get_model(app=request.matchdict.get("app"),
                                                   model_name=request.matchdict.get("model_name"),
                                                   version=request.matchdict.get("version"),
                                                   client=request.matchdict.get("client"))

        return model_retrieved.io_template

    except:
        response = generate_bad_request()
        return response


@view_config(request_method='GET',route_name='data_template.client.product', renderer='json')
def data_template_client_product_view(request):

    try:
        from dbhelper.main.dbhelper import HelperRuntime

        helper = HelperRuntime()

        model_retrieved = ModelRetriever.get_model(app=request.matchdict.get("app"),
                                                   model_name=request.matchdict.get("model_name"),
                                                   version=request.matchdict.get("version"),
                                                   client=request.matchdict.get("client"),
                                                   product=request.matchdict.get("product"))

        return model_retrieved.io_template

    except:
        response = generate_bad_request()
        return response
