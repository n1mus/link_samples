import os
from pathlib import Path

from installed_clients.SampleServiceClient import SampleService

from .config import app
from ..util.debug import dprint



class SampleSet:
    TYPE = 'KBaseSets.SampleSet'

    def __init__(self, upa):
        self.upa = upa

        obj = app.dfu.get_objects({
            'object_refs': [self.upa]
        })

        self.name = obj['data'][0]['info'][1]
        self.obj = obj['data'][0]['data']

        if 'run_dir' in app: # debug
            Path.touch(os.path.join(app.run_dir, '_' + self.name))

    def _get_index(self, sample_name):
        for i, d in enumerate(self.obj['samples']):
            if d['name'] == sample_name:
                return i
        raise Exception(name)
    
    def get_sample_info(self, sample_name):
        ind = self._get_index(sample_name)

        node_id = self.obj['samples'][ind]['name']
        ver = self.obj['samples'][ind]['version']
        sample_id = self.obj['samples'][ind]['id']

        return node_id, ver, sample_id





