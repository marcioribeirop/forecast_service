import gc
from forecast_service.utils.instantiate_model import ModelInstanceHolder
from forecast_service.utils import generate_global


class ModelRetriever(object):

    @classmethod
    def get_model(cls, app, model_name, version, client=None, product=None):
        requested_model = None

        for obj in generate_global.models_list:
            if isinstance(obj, ModelInstanceHolder):
                if obj.app == app:
                    if obj.model_name == model_name:
                        if obj.version == version:
                            if obj.client == client:
                                if obj.product == product:
                                    requested_model = obj

        if requested_model == None:
            requested_model = ModelInstanceHolder(app=app, model_name=model_name, version=version, client=client,
                                                                   product=product)
            generate_global.models_list.append(requested_model)

            return requested_model

        else:
            return requested_model

    @classmethod
    def search_model(cls, app, model_name, version, client=None, product=None):

        requested_model = cls.get_model(app=app, model_name=model_name, version=version, client=client, product=product)

        return requested_model

