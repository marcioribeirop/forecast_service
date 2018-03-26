from pyramid.view import view_config
from forecast_service.utils.object_retriever import ModelRetriever
from forecast_service.web.views.error_views import generate_bad_request


@view_config(request_method='POST', route_name='base', renderer='json')
def base_view(request):

    try:
        from dbhelper.main.dbhelper import HelperRuntime
        import numpy as np
        import json

        inputs = request.json['inputs']

        helper = HelperRuntime()

        model_retrieved = ModelRetriever.get_model(app=request.matchdict.get("app"),
                                                   model_name=request.matchdict.get("model_name"),
                                                   version=request.matchdict.get("version"))

        model = model_retrieved.model
        io_template = model_retrieved.io_template

        template_inputs = eval(io_template["input"])

        outputs = model.predict(template_inputs)

        template_outputs = eval(io_template["output"])

        return {"output": template_outputs}

    except:
        response = generate_bad_request()
        return response


@view_config(request_method='POST', route_name='base.client', renderer='json')
def base_client_view(request):

    try:
        from dbhelper.main.dbhelper import HelperRuntime
        import numpy as np
        import json

        inputs = request.json['inputs']

        helper = HelperRuntime()

        model_retrieved = ModelRetriever.get_model(app=request.matchdict.get("app"),
                                                   model_name=request.matchdict.get("model_name"),
                                                   version=request.matchdict.get("version"),
                                                   client=request.matchdict.get("client"))

        model = model_retrieved.model
        io_template = model_retrieved.io_template

        template_inputs = eval(io_template["input"])

        outputs = model.predict(template_inputs)

        template_outputs = eval(io_template["output"])

        return {"output": template_outputs}

    except:
        response = generate_bad_request()
        return response


@view_config(request_method='POST',route_name='base.client.product', renderer='json')
def base_client_product_view(request):

    try:
        from dbhelper.main.dbhelper import HelperRuntime
        import numpy as np
        import json

        inputs = request.json['inputs']

        helper = HelperRuntime()

        model_retrieved = ModelRetriever.get_model(app=request.matchdict.get("app"),
                                                   model_name=request.matchdict.get("model_name"),
                                                   version=request.matchdict.get("version"),
                                                   client=request.matchdict.get("client"),
                                                   product=request.matchdict.get("product"))

        model = model_retrieved.model
        io_template = model_retrieved.io_template

        template_inputs = eval(io_template["input"])

        outputs = model.predict(template_inputs)

        template_outputs = eval(io_template["output"])

        return {"output": template_outputs}

    except:
        response = generate_bad_request()
        return response
