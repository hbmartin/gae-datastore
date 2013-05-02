#!/usr/bin/env python
#

import os
import logging
import wsgiref.handlers
import random, md5

from record import Record 
from baseHandler import BaseRequestHandler

class PutHandler(BaseRequestHandler):

  def post(self, key = None):
    record = None
    if not key:
      key = self.request.get('key')
    if key:
      record = Record.get_by_key_name(key)
    if not record:
      record = Record(key_name = key, value = self.request.get('value'))
    else:
      record.value = self.request.get('value')
    record.put()
    self.response.out.write(key)
