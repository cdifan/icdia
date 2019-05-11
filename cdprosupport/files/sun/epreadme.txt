**********************************************************************************  
                                  READ ME
**********************************************************************************


This is a  bug fix update of EP Assist.  

Changes to Mac, PC, and Sun:

Fixed a bug that would (on rare occasions) give you a read error 
at the end of the stream.  Since the bug occurred at the end reading
the file, all entrypoints (and any files generated) would be valid.

Mac only changes:

Fixed a bug in the Mac front end where you no longer are required to
have a '.' in the filename.  (Before, EP Assist would hang if you didn't have a '.'.) 
Also, dismiss the splash screen and about box early if you click on it.


No OS-9 update.