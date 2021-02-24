

from .params import Params
from .kb_obj import SampleSet
from .config import app
from ..util.debug import dprint






def link_reads_to_samples(params):

    params = Params(params)

    sample_set = SampleSet(params['sample_set_upa'])
    links = params.get_links()

    for sample_name, reads_upa in links:
        node_id, version, sample_id = sample_set.get_sample_info(sample_name)
        params = dict(
            upa=reads_upa,
            id=sample_id,
            version=version,
            node=node_id,
            update=1,
        )
        ret = app.ss.create_data_link(
            params
        )

