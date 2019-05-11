Installation of ddinits and new startnet file           11/93



1.) Copy ddinits.tar to /h0/CMDS

2.) Extract the contents of ddinits.tar (tar -xvf ddinits.tar)

3.) Rename /h0/startnet to /h0/startnet.old

4.) Copy the new startnet (from the BBS) to /h0 as /h0/startnet

5.) Use uMacs to edit startnet and change the "le0" internet address

to match the address in startnet.old.  Save the file, <ESCAPE> <Z>.

6.) Reset the 605 and goto CD-RTOS.  Run startnet.







Note:  If you didn't download the new startnet file, you may edit the existing

file on /h0 by:



1.) Use Umacs to edit startnet.

2.) Add the folowing line AFTER the "le0" line:



        load -d /h0/cmds/init.dd.60x



3.) Save the file, <ESCAPE> <Z>.
