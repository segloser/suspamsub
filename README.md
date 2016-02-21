# suspamsub

Just a PoC in Python to submit suspicious samples directly to VirusTotal and Hybrid-Analysis.

Once you execute this short program, your default browser will open (if not yet open, in which case two new tabs will appear) and will ask you for a sample to evaluate. After you select a file, a SHA256 hash will be calculated and submitted to VirusTotal and Hybrid-Analysis to check if a sample with that hash has already been analyzed by these malware databases.

The point here is to show to our employees how simple could be to check a suspicious or unknown file before OPENING it.

Opening unknown files or unexpected attachments in emails could ruin your company network (in case of cryptomalware).

Please, develop tools based on this concept and train your employees to check every unsolicited file.

Help your employees to develop a digital common sense.

Thanks.
