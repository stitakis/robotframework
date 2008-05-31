#  Copyright 2008 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from model import TestSuiteData
from rawdata import RawData
from resourcefile import ResourceFile
from robot.conf.settings import RobotSettings
from robot.output.systemlogger import SystemLogger


def TestSuite(*datasources, **options):
    """Creates and returns a parsed test suite object.
    
    Data sources are paths to files and directories, similarly as when running
    pybot/jybot from command line. Options are given as keywords arguments and
    their names are same as long command line options without hyphens. 
    """
    settings = RobotSettings(options)
    try:
        syslog = options['syslog'] 
    except KeyError: 
        syslog = SystemLogger(settings)
    return TestSuiteData(datasources, settings, syslog, 
                         options.get('process_curdir', True))
