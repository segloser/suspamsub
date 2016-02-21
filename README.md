# suspamsub

Just a PoC in Python to submit suspicious samples directly to VirusTotal and Hybrid-Analysis.

Once you execute this short program it will ask you for a file/attachment to evaluate. After you select that file, a SHA256 hash will be calculated and your default browser will open (if not yet open, in which case two new tabs will appear) VirusTotal and Hybrid-Analysis pages to check if a sample with that hash has already been analyzed by these malware databases.

The point here is to show to our employees how simple could be to check a suspicious or unknown file before OPENING it.

This is needed because AntiVirus programs are not enough any more, and manual analysis conducted by the community should also be taken into account.

Opening unknown files or unexpected attachments in emails could ruin your company network (in case of cryptomalware).

Please, develop tools based on this concept and train your employees to check every unsolicited file. 

Routinary and automatic AntiVirus analysis of non-executable files like Microsoft Word/Excel or PDF documents, could include malicious code (macros or obfuscated JavaScript). Your employees should already know this.

Help your employees to develop a digital common sense.

Thanks.
