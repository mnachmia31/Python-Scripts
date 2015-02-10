# This script is used to make a connection to a JIRA server to make updates
# to JIRA issues. This script takes three command line arguments:
# jira_server - JIRA Server URL
# jira_user - JIRA user
# jira_password - JIRA user's password

__author__ = 'michaelnachmias'

from jira.client import JIRA
import sys
import logging

def connect_jira(log, jira_server, jira_user, jira_password):
    # Connect to JIRA. Return None on error
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        # Disable SSL Certificate Verification
        jira_options = {'server': jira_server, 'verify': False}
        jira = JIRA(options=jira_options,
                    # Note the tuple
                    basic_auth=(jira_user, 
                                jira_password))
        log.info("Successfully connceted to JIRA: %s" % jira_server)
        return jira
    except Exception as e:
        log.error("Failed to connect to JIRA: %s" % e)
        return None

if  __name__ =='__main__':
    # create logger
    logger = logging.getLogger('jira_server')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # Create JIRA connection
    connect_jira(logger, sys.argv[1], sys.argv[2], sys.argv[3])
