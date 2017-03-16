"""
* ********************************************************************
*  Project      Harman Car Multimedia System
*  (c) copyright 2009
*  Company      Harman/Becker Automotive Systems GmbH
*  All rights reserved
*  Secrecy Level STRICTLY CONFIDENTIAL
* ********************************************************************
@file         debug.py
@author       Vladimir Aleksandrov <valeksandrov@luxoft.com>
@date         01.07.2013
@brief        debugger and logger
"""

import gzip
import logging
import logging.handlers
import os
import sys

from .Singletonmixin import Singleton


class debug(logging.Logger, Singleton):
   """
   Class debug is implementation of the logger
   @see python logging module for more information
   """

   def __init__( self, logLevel = logging.NOTSET, logFileName = './logger.log', fileSize = 20000, filesCount = 5 ):
      """
      Constructor
      :param logLevel: debug messages level
      :param logFileName: name of the log file
      """
      logging.Logger.__init__( self, '', logLevel )
      fileHandler = gzRotatingFileHandler( logFileName, maxBytes = fileSize, backupCount = filesCount )
      fileHandler.setLevel( logLevel )
      # create formatter and add it to the handlers
      formatter = logging.Formatter( '%(asctime)s   [ %(levelname)s ]   [%(process)d]%(module)s::%(funcName)s:%(lineno)d #   %(message)s' )
      fileHandler.setFormatter( formatter )

      stderrHandler = logging.StreamHandler( sys.stderr )
      stderrHandler.setLevel( logging.ERROR )
      stderrFormatter = logging.Formatter( '%(asctime)s   [ %(levelname)s ]   [%(process)d]%(module)s::%(funcName)s:%(lineno)d #   %(message)s' )
      stderrHandler.setFormatter( stderrFormatter )

      # add the handlers to the logger
      self.addHandler( fileHandler )
      self.addHandler( stderrHandler )
      self.info( ":::::::::::::::::::: Logger created ::::::::::::::::::::" )


   @classmethod
   def log( self ):
      """
      Statis shortcut for the self.getInstance()
      :return: debug
      """
      return self.getInstance()

def log():
   return debug.log()

class gzRotatingFileHandler( logging.handlers.RotatingFileHandler ):

   def doRollover( self ):
      if self.stream:
         self.stream.close()
      if self.backupCount > 0:
         for i in range( self.backupCount - 1, 0, -1 ):
            sfn = "%s.%d.gz" % ( self.baseFilename, i )
            dfn = "%s.%d.gz" % ( self.baseFilename, i + 1 )
            if os.path.exists( sfn ):
               if os.path.exists( dfn ):
                  os.remove( dfn )
               os.rename( sfn, dfn )
         dfn = self.baseFilename + ".1.gz"
         if os.path.exists( dfn ):
            os.remove( dfn )
         with open( self.baseFilename ) as log:
            with gzip.open( dfn, 'wb' ) as comp_log:
               comp_log.writelines( log )
      self.mode = 'w'
      self.stream = self._open()
