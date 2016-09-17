from liblo import *

import sys
import time


class MuseServer(ServerThread):
   #listen for messages on port 5000
   def __init__(self):
      ServerThread.__init__(self, 5000)

    # receive EEG data
   @make_method('/muse/eeg/quantization', 'iiiiii')
   def eeg_timesamp_callback(self, path, args):
      timestamp = args[4]
      print "timestamp %d \n" % timestamp

      # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

    # alpha relitave
   @make_method('/muse/elements/alpha_relative', 'ffff')
   def alpha_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      print "alpha: %f" % average
      # l_ear, l_forehead, r_forehead, r_ear = args
      # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

    # beta relitave
   @make_method('/muse/elements/beta_relative', 'ffff')
   def beta_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      print "beta:  %f" % average
      # l_ear, l_forehead, r_forehead, r_ear = args
      # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

   # delta relitave
   @make_method('/muse/elements/delta_relative', 'ffff')
   def delta_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      print "delta: %f" % average
      # l_ear, l_forehead, r_forehead, r_ear = args
      # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

   # gama relative
   @make_method('/muse/elements/gamma_relative', 'ffff')
   def gamma_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      print "gamma  %f" % average
      # l_ear, l_forehead, r_forehead, r_ear = args
      # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

   #theta relitave
   @make_method('/muse/elements/theta_relative', 'ffff')
   def theta_rel_callack(self, path, args):
      average =  sum(args) / len(args)
      print "theta  %f" % average
      # l_ear, l_forehead, r_forehead, r_ear = args
      # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)


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

