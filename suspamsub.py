#!/usr/bin/python

###########################################  LICENSE  ################################################
"""All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
 provided that the following conditions are met:

	Redistributions of source code must retain the above copyright notice, 
	this list of conditions and the following disclaimer.
	Redistributions in binary form must reproduce the above copyright notice,
	this list of conditions and the following disclaimer in the documentation 
	and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
 SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF 
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."""
#######################################  END OF LICENSE TERMS  ########################################

__author__ = 'eorenes(typical symbol in emails)segloser-dot-com (Eduardo ORENES)'
__version__ = '0.1'
__copyright__ = 'SEGLOSER'
__license__ = 'All Rights Reserved'

import webbrowser
import hashlib
import re
import Tkinter as tk
from tkFileDialog import askopenfilename
import time
import urllib

# VirusTotal format: "https://www.virustotal.com/file/" + SHA256 + "/analysis/"
# Hybrid-Analysis format: "https://www.hybrid-analysis.com/sample/" + SHA256

# Opening a window to select a file to submit to Hybrid-Analysis
global sample
def sus_call():
	global sample
	file_to_open = askopenfilename()
	sample = file_to_open
	print sample
	print "Opening the online malware databases resources..."
	return sample

# Hashing (SHA256, SHA1 and MD5) the sample 
BLOCKSIZE = 65536
hasher_SHA256 = hashlib.sha256()
hasher_SHA1 = hashlib.sha1()
hasher_MD5 = hashlib.md5()

path = str(sus_call())
afile = open((path), 'rb')
buf = afile.read(BLOCKSIZE)
while len(buf) > 0:
    hasher_SHA256.update(buf)
    buf = afile.read(BLOCKSIZE)
SHA256 = (hasher_SHA256.hexdigest())
afile.close()

bfile = open((path), 'rb')
buf = bfile.read(BLOCKSIZE)
while len(buf) > 0:
    hasher_SHA1.update(buf)
    buf = bfile.read(BLOCKSIZE)
SHA1 = (hasher_SHA1.hexdigest())
bfile.close()

cfile = open((path), 'rb')
buf = cfile.read(BLOCKSIZE)
while len(buf) > 0:
    hasher_MD5.update(buf)
    buf = cfile.read(BLOCKSIZE)
MD5 = (hasher_MD5.hexdigest())
cfile.close()

# Search the sample hash in Google
# Google search format: https://www.google.es/search?q=<term_to_search>
webbrowser.open("https://www.google.es/search?q=" + SHA256)
# Pause to allow some time and open tabs instead of new browser sessions
time.sleep(1)
webbrowser.open("https://www.google.es/search?q=" + SHA1)
webbrowser.open("https://www.google.es/search?q=" + MD5)

# Opening a Valkyrie COMODO tab (MSOffice docs not supported
# webbrowser.open("https://valkyrie.comodo.com/get_info?sha1=" + SHA1)

# Malwr submission (registration needed to get your own api-key
api_value = {'api_key':"type your API here"} # DO NOT FORGET TO TYPE YOUR API
api_found = re.match(r'[A-Fa-f0-9]{32}', api_value['api_key'])
if api_found:
#if api_value['api_key'] != "type your API here":
    params = urllib.urlencode({'api_key': api_value['api_key'], 'shared': "yes", 'file': path})
    f = urllib.urlopen("https://malwr.com/api/analysis/add/", params)
    # This will save a local html file with malwr response to your request
    malwr_sub = open(("submission_" + SHA1 + ".html"), "w")
    malwr_sub.write(f.read())
    webbrowser.open("submission_" + SHA1 + ".html")
    f.close()
    malwr_sub.close()
else:
    print "You have to introduce your API for accessing www.malwr.com services"

# Vicheck format: https://www.vicheck.ca/md5query.php?hash=<md5>
webbrowser.open("https://www.vicheck.ca/md5query.php?hash=" + MD5)

# ThreatCrowd format: https://www.threatcrowd.org/malware.php?md5=<md5>
webbrowser.open("https://www.threatcrowd.org/malware.php?md5=" + MD5)

# Opening a VirusTotal tab
webbrowser.open("https://www.virustotal.com/file/" + SHA256 + "/analysis/")

# Opening a web browser tab or page in Hybrid-Analysis 
# to check if sample is already analyzed
webbrowser.open("https://www.hybrid-analysis.com/sample/" + SHA256)
