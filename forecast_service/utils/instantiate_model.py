class ModelInstanceHolder(object):

    def __init__(self, app, model_name, version, client=None, product=None):
        from dbhelper.main.dbhelper import HelperRuntime

        helper = HelperRuntime()
        self.app = app
        self.model_name = model_name
        self.version = version
        self.client = client
        self.product = product

        self.model, self.io_template = helper.load(app, model_name, version, client, product)

    def __del__(self):
        raise ("The model {}/{}/{}/{}/{} was garbage collected".format(self.app, self.model_name, self.version,
                                                                       self.client, self.product))