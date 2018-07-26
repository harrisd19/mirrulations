import json
import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(filename='client.log', format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'CONFIG'}
logger = logging.getLogger('tcpserver')

def read_value(value):
    '''
    Reads a file from the configuration JSON file.
    :param value: Value to be read from the JSON
    :return: Value read from the JSON
    '''
    logger.warning('Calling Function: %s', 'read_value: Reading a value from the configuration file', extra=d)
    try:
        m = json.loads(open("../config.json","r").read())
    except:
        logger.warning('Exception: %s', 'read_value: Error opening/loading JSON', extra=d)

    try:
        result = m[value]
    except KeyError:
        logger.warning('Exception: %s', 'config: Caught KeyError, no value present for: ' + str(value) + '. Returning None.', extra=d)
        return None
    return result