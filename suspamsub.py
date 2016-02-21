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

__author__ = 'info@segloser.com (Eduardo ORENES)'
__version__ = '0.1'
__copyright__ = 'SEGLOSER'
__license__ = 'All Rights Reserved'


import webbrowser
import hashlib
import Tkinter as tk
from tkFileDialog import askopenfilename
import time

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

# Hashing (SHA256) the sample 
BLOCKSIZE = 65536
hasher = hashlib.sha256()
path = str(sus_call())
afile = open((path), 'rb')
buf = afile.read(BLOCKSIZE)
while len(buf) > 0:
    hasher.update(buf)
    buf = afile.read(BLOCKSIZE)
SHA256 = (hasher.hexdigest())

# Opening a web browser tab or page in Hybrid-Analysis 
# to check if sample is already analyzed
webbrowser.open("https://www.hybrid-analysis.com/sample/" + SHA256)
time.sleep(3)
webbrowser.open("https://www.virustotal.com/file/" + SHA256 + "/analysis/")
