import yaml

CONFIG_FILE = './config'
def get_conf():
    conf = yaml.load(file(CONFIG_FILE))
    return conf

def get_services():
    conf = get_conf()
    return conf['services_list']

def get_service_conf(service):
    conf = get_conf()
    return conf[service]
def get_default():
    conf = get_conf()
    return conf['default']
if __name__ == "__main__":
    print get_conf()
