# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from link_samples.link_samplesServer import MethodContext
from link_samples.authclient import KBaseAuth as _KBaseAuth
from installed_clients.WorkspaceClient import Workspace

from link_samples.link_samplesImpl import link_samples
from .data import *

class link_samplesTest(unittest.TestCase):

    def test_your_method(self):
        ret = self.serviceImpl.run_link_samples(
            self.ctx, {
                'workspace_name': self.wsName,
                'sample_set_upa': ReadLinkingTestSampleSet,
                'links': [
                    {'sample_name': '0408-FW021.46.11.27.12.10', 'reads_upa': rhodo_art_jgi_reads},
                    {'sample_name': '0408-FW021.7.26.12.02', 'reads_upa': rhodobacter_art_q50_SE_reads},
                    {'sample_name': '0408-FW021.46.11.27.12.02', 'reads_upa': Example_Reads_Libraries},
                ]
            })


    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('link_samples'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'link_samples',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = link_samples(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        cls.wsName = "test_ContigFilter_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

