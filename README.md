# suspamsub

![alt tag](Check_Emails_Attachments_EXAMPLE.gif)
SHORT VERSION:
Go to "Windows7/Directory_Installer" and download the self-extracting exe. Follow the detailed instrucions in the README (briefly speaking, execute the self-extracting file in "C:\" and execute the "reg_addition.bat" file with administrator privileges; then just right click and select the Check_SPAM option).

In you do not trust an unknown exe (which is a very intelligente posture), review the Python code and use for your tests.
You can use py2exe and WinRAR to make your own executables.


DETAILED VERSION:
Just a PoC in Python to submit suspicious samples directly to VirusTotal, Hybrid-Analysis, Malwr and some others.

Once you execute this short program it will ask you for a file/attachment to evaluate. After you select that file, three common hashes (deprecated like MD5 or SHA1, and still in use like SHA256) will be calculated and your default browser will be open (if not yet open, in which case some new tabs will appear) pointing to VirusTotal and Hybrid-Analysis, among others, to check if a sample with those hashes has already been analyzed by these malware databases.

The point here is to show to our employees how simple could be to check a suspicious or unknown file before OPENING it.

This is needed because AntiVirus programs are not enough any more, and manual analysis conducted by the community should also be taken into account.

Opening unknown files or unexpected attachments in emails could ruin your company network (in case of cryptomalware).

Please, develop tools based on this concept and train your employees to check every unsolicited file. 

Routinary and automatic AntiVirus analysis of non-executable files like Microsoft Word/Excel or PDF documents, could include malicious code (macros or obfuscated JavaScript). Your employees should already know this.

Help your employees to develop a digital common sense.

Thanks.
