import urllib2
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from fabric.api import *