#! /usr/sbin/perl
#
#                 maillog.cgi - Uses Server Side Includes
#                   Version 2.01   --   17 August 1996
#
#     Written by Walter Soldierer (webmaster@mecagoch.com), author of
#                          THE DIGITAL POSTCARD
#           A FREE service to increase your web site's exposure!
#                            Need more hits?
#      Check it out at http://www.mecagoch.com/postcard/postcard.htm
#
# maillog.cgi uses a code snipplet from Dan Schless
# Released to the public domain for free. Standard disclaimers apply.
#
# This script saves access date+time, the visitor's host name, his IP
# address and browser type, and the referring page (if any) to a log file
# on your server (default name = logfile.txt). This file will be automatically
# mailed to your mailbox. You can change the mailing interval according
# to your needs (default value is every 50 accesses to the page to be
# logged). The script will autocreate the logfile, if it does not exist.
#
#
# ----- BEGIN INSTALLATION INSTRUCTIONS -----
#  - Save this script to a file maillog.cgi
#  - Cut installation instructions (optional)
#  - Change the first script line, if your server's Perl executable
#    is not located in /usr/local/bin/perl
#  - Customize the settings below (*SETTINGS*)
#    * Change e-mail address for $recipient, otherwise I will receive
#      your logs ;-)   Don't forget to put add backslash (\) before
#      the "at" (@) character! (required for scripts using Perl 5).
#    * Set $log_page to 1 if you also want to log the page that
#      called this script. Recommended in case you want to log accesses
#      to more than one HTML page.
#    * Set $max_entries to your needs, if you want to have more or less
#      than 50 log entries mailed to your mailbox each time.
#    * Change filenames for log file, if necessary (default = logfile.txt)
#  - ASCII-upload maillog.cgi to your cgi directory (cgi-bin, cgi-local...) or
#    to any other directory. Make it executable (chmod maillog.cgi 755).
#  - add the following line (Server Sde Include) to the page(s) to be logged
#    (after the <body> tag):
#    <!--#exec cgi="/your-directory/maillog.cgi"-->
#    HTML pages with Server Side Includes often must have the
#    file extension .shtml !!!! (don't forget to update
#    all links to this page(s) accordingly)
#    (You should test the script with a test.shtml page first)
#  - Load the logged page(s) into your browser.
#  - View your new logfile in the script directory
#    It should look something like this:
#    
#    Time: 05/30/96 14:44:07 EDT
#    Host: your.host.and.domain
#    Addr: 123.45.67.89
#    With: Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)
#    Page: test.shtml
#    From: [no entry here, if you accessed your page directly (otherwise Yahoo etc.)]
#
#    If the script doesn't work and you want to contact me, please check
#    the following first:
#    - did you upload the script in ASCII mode (*not* binary)?
#    - did you chmod the script 755
#    - did you rename the html file to .shtml
#    - did you check the path to your server's Perl executable?
#    - did you escape the @ character in your email address (\@)?
#    - does your server support Server Side Includes?
#
#    If you still have a problem and you want me to help you, I need
#    the following:
#     - a detailed description of the problem
#     - your script's settings section
#     - your html code for the page to be logged
#     - script related error messages from your server's error logs
# ----- END INSTALLATION INSTRUCTIONS -----



# -----------------------------------------------------------------------
# *SETTINGS* to customize this script:

# Your email address (a backslash is required to escape the @):
$recipient = "toby\@advantage-computer.com";

# Do you want to log the .shtml page's file name?
# (recommended when more than one page is logged)
# 1 = the .shtml page that called this script will be logged
# 0 = the .shtml page that called this script will not be logged
$log_page = 1;

# Number of logged visits mailed to your mailbox at a time:
$max_entries = 5;

# Change logfile name if necessary:
$logfile = "support_log.txt";

# server's sendmail directory:
$mailprog = "/usr/sbin/sendmail";

# what visitors will not be logged in maillog.cgi?
@null_visitors = ("netins.net");
# -----------------------------------------------------------------------
if (grep ($ENV{REMOTE_HOST} =~ /$_/, @null_visitors)) {
    print "Content-type: text/html\n\nYou are not being logged as a visitor.\n";
    exit;
}
# create a date+time string
$shortdate = `date +"%D %T %Z"`; 
chop ($shortdate);
$datetime = "Time: $shortdate\n";

# Some of Perl's network info functions required here
# Here goes Dan's code to resolve host name from IP address
   $number = $ENV{REMOTE_ADDR};
   ($a,$b,$c,$d)=split(/\./,$number);
   $ipadr=pack("C4",$a,$b,$c,$d);
   ($name,$aliases,$addrtype,$length,@addrs)=(gethostbyaddr("$ipadr", 2));
# Thank you, Dan
$host = "Host: $name\n";
$IP = "IP  : $number\n";
$browser = "With: $ENV{'HTTP_USER_AGENT'}\n";
$page = "Page: $ENV{'DOCUMENT_URI'}\n";
$from = "From: $ENV{'HTTP_REFERER'}\n\n";


# Avoid "Malformed header from Script" error message
print "Content-type: text/plain\n\n ";

# open log file for output and append new log data
# if file doesn't exist yet, it will be created
open (FILE, ">>$logfile");
print FILE $page if $log_page;
print FILE "$datetime$host$IP$browser$from";
close (FILE);

# open log file for input and count log entries
open (FILE, $logfile);
@filetext = <FILE>;
if ($log_page) {
   $log_count = @filetext/7;
}
else {
   $log_count = @filetext/6;
}
close (FILE);


# if number of logs >= max. number of logs, mail file and overwrite it
if ($log_count >= $max_entries) {
   open (MAIL, "|$mailprog $recipient") || die "Can't open $mailprog!\n";
   print MAIL "Subject: Log File\n\n";
   print MAIL "@filetext\n";
   close MAIL;

   # open logfile for output (overwrite)
   open (FILE, ">$logfile");
   print "";
   close (FILE);
}

# end of script----------------------------------------------------------------------------
