import argparse
from pathlib import Path
import os
import sys


def main(token, env, installed_clients):
    sys.path.append(installed_clients)
    from WorkspaceClient import Workspace

    ws = Workspace(
        token=token, 
        url='https://%skbase.us/services/ws' % (env + '.' if env != 'prod' else '')
    )

    home = Path('by_dataset_input')
    home.mkdir()

    dataset0 = home / 'SampleMetaData.tsv_sample_set'
    dataset1 = home / 'Example_Reads_Libraries'








def parse_args():
    parser = argparse.ArgumentParser(                                                               
        description=(                                                                               
            "Generate I/O files to mock in during kb-sdk tests"                                      
        )                                                                                           
    )                                                                                               
    parser.add_argument(                                                                            
        '--token',                                                                               
        required=True,                                                                              
        help='Token'                                                     
    )  
    parser.add_argument(
        '--env',
        required=True,
        help="Environment, e.g., from ['ci', 'appdev', 'prod']"
    )
    parser.add_argument(
        '--installed-clients',
        required=True,
        help='Folder containing WorkspaceClient.py'
    )

    parser.parse_args()


if __name__ == '__main__':
    a = parse_args()
    
    main(a.token, a.env, a.installed_clients)

