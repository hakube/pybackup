import yaml

class Backup:
    def __init__(self, config):
        self.config = config

    def parse_yaml(self):
        with open(self.config) as f:
            self.config = yaml.safe_load(f)

    def echo(self):
        print(self.config)

    def run(self):
        pass