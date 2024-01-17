from typing import Any, Optional
import yaml
import logging
import json

class Analysis():
    def __init__(self, analysis_config:str):
        CONFIG_PATHS = ['system_config.yml', 'user_config.yml']
        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            try:
                with open('../configs/' + path, 'r') as f:
                    this_config = yaml.safe_load(f)
                    config.update(this_config)
            except FileNotFoundError:
                logging.error('File not found - ' + path)
                raise FileNotFoundError
                
        self.config = config
        self.data = {}
        self.analysis_output = {
            minForks: -1,
            maxForks: -1,
            sumForks: -1
        }
    
    def load_data(self):
        try:
            dataset_url = self.config['dataset_url'] 
            headers = {'Authorization': 'Bearer ' + self.config['token']}
        except KeyError:
            logging.error('Cannot find key in config') 
            raise KeyError
  
        get_request = requests.get(dataset_url, headers=headers)

        response_json = json.loads(get_request.text)
        
        if 'message' in response_json and response_json['message'] == 'Bad credentials':
            logging.error('Bad credentials')
        else:     
            self.data = response_json['items']
    
    # Calculate min, max, and sum of the value 'forks' from the data loaded through the API
    def compute_analysis(self):
        forksList = []
        for d in self.data:
            forksList.append(d['forks'])

        self.analysis_output = {
            minForks: min(forksList),
            maxForks: max(forksList),
            meanForks: sum(forksList)/len(forksList)
        }


        
