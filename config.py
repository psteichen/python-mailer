"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

from datetime import datetime

# file settings
LOG_FILENAME        = '/tmp/pymailer.log'
CSV_RETRY_FILENAME  = '/tmp/pymailer.csv'
STATS_FILE          = '/tmp/pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# smtp settings
SMTP_HOST     = 'localhost'
SMTP_PORT     = '25'
SMTP_USER     = '' # Leave empty if not needed
SMTP_PASSWORD = '' # Leave empty if not needed
ENCRYPT_MODE  = 'starttls' # Choose between 'none', 'ssl' and 'starttls'

# the address and name the email comes from
FROM_NAME = 'SECURITYMADEIN.LU'
FROM_EMAIL = 'events@securitymadein.lu'

# The number of emails to send to each recipient
NB_EMAILS_PER_RECIPIENT = 1

# test recipients list
TEST_RECIPIENTS = [
    {'name': 'Pascal Steichen', 'email': 'pst@secin.lu'},
    {'name': 'Emilie Muller', 'email': 'emilie.muller@smile.public.lu'},
]
