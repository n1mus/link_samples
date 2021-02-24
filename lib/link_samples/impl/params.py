




class Params:

    def __init__(self, params):
        self._validate(params)
        self.params = params


    def _validate(self, params):
        pass


    def get_links(self):
        links = self.params['links']
        return [(d['sample_name'], d['reads_upa']) for d in links]

    def __getitem__(self, k):
        return self.params[k]


