from liblo import *
import sys
import time
import json
import requests

current_freq_url = 'https://koan-cbd22.firebaseio.com/detailedprofiles.json'
rel_payload = {'user_id': 'skywalker'}

class MuseServer(ServerThread):
   #listen for messages on port 5000
   def __init__(self):
      ServerThread.__init__(self, 5000)

    # receive EEG data
   @make_method('/muse/eeg/quantization', 'iiiiii')
   def eeg_timesamp_callback(self, path, args):
      timestamp = float(str(args[4]) + '.' + str(args[5]))
      rel_payload['timestamp'] = timestamp
      print "timestamp %d " % timestamp

    # alpha relitave
   @make_method('/muse/elements/alpha_relative', 'ffff')
   def alpha_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      rel_payload['alpha'] = average
      print "alpha: %f" % average

    # beta relitave
   @make_method('/muse/elements/beta_relative', 'ffff')
   def beta_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      rel_payload['beta'] = average
      print "beta:  %f" % average

   # delta relitave
   @make_method('/muse/elements/delta_relative', 'ffff')
   def delta_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      rel_payload['delta'] = average
      print "delta: %f" % average

   # gama relative
   @make_method('/muse/elements/gamma_relative', 'ffff')
   def gamma_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      rel_payload['gamma'] = average
      print "gamma  %f" % average

   #theta relitave and POST point
   @make_method('/muse/elements/theta_relative', 'ffff')
   def theta_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      rel_payload['theta'] = average

      r_relative = requests.post(current_freq_url, json=rel_payload)
      print rel_payload
      print "theta  %f\n" % average

   #handle unexpected messages
   @make_method(None, None)
   def fallback(self, path, args, types, src):

      pass
      # print "Unknown message \
      # \n\t Source: '%s' \
      # \n\t Address: '%s' \
      # \n\t Types: '%s ' \
      # \n\t Payload: '%s'" \
      # % (src.url, path, types, args)

try:
   server = MuseServer()
except ServerError, err:
   print str(err)
   sys.exit()

server.start()

if __name__ == "__main__":
   while 1:
      time.sleep(1)

