# coding=utf-8

###############################################################################
##
##  Copyright 2011 Tavendo GmbH
##
##  Note:
##
##  This code is a Python implementation of the algorithm
##
##            "Flexible and Economical UTF-8 Decoder"
##
##  by Bjoern Hoehrmann
##
##       bjoern@hoehrmann.de
##       http://bjoern.hoehrmann.de/utf-8/decoder/dfa/
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################


class Utf8Validator(object):

    def validate(self, ba):
        """
        Will return a boolean true/false if "ba" is a valid utf8 bytes object
        """
        try:
            ba.decode('utf8')
        except UnicodeDecodeError:
            return False
        else:
            return True
