$9 ~ /^technote[0-9]*.*\.pdf$/ {
	note = $9
	gsub(/technote/, "", note)
	gsub(/\.pdf/, "", note)
	kb[note] = ($5 + 1023) / 1024
}

$0 ~ /^TECHNICAL NOTE #[0-9].*/ {
	if (state == 4) {
		printf "</I><BR>\n"
		if (kb[note] > 0)
			printf "Download <A HREF=\"technote%s.pdf\">technote%s.pdf</A> (PDF - %d KB)\n", note, note, kb[note]
		else
			printf "<FONT COLOR=\"#a0a0a0\">Not yet available for download</FONT>\n"
		printf "</P>\n"
		state = 0
	}

	if (state != 0)
		printf "ERROR NOT IN STATE 0\n"

	note = $0
	gsub(/TECHNICAL NOTE #/, "", note)
	printf "\n"
	printf "<P>\n"
	#printf "<B><LI><A NAME=\"technote%s\">%s</A></LI></B><BR>\n", note, $0
	state = 1
	next
}

state == 1 {
	printf "<B><LI><A NAME=\"technote%s\">TN #%s - %s</A></LI></B><BR>\n", note, note, $0
	#printf "<B>%s</B><BR>\n", $0
	state = 2
	printf "<A HREF=\"#technote%s\">TN #%s - %s</A><BR>\n", note, note, $0 >"techlist.htm"
	next
}

state == 2 {
	printf "<I>%s</I><BR>\n", $0
	state = 3
	sep = ""
	next
}

state == 3 && ($0 ~ /No revisions/ || $0 ~ /Revised/ || $0 ~ /Supersedes/ || $0 ~ /Recovered/) {
	if (sep != "")
		printf "<BR>\n"
	printf "<I>%s", $0
	state = 4
	next
}

state == 3 {
	printf "%s%s", sep, $0
	sep = "\n"
}

state == 4 {
	printf " %s", $0
}

END {
	if (state == 3) {
		if (sep != "")
			printf "<BR>%s", sep
	}

	if (state == 4) {
		printf "</I><BR>\n"
	}

	if (state > 0)
	{
		if (kb[note] > 0)
			printf "Download <A HREF=\"technote%s.pdf\">technote%s.pdf</A> (PDF - %d KB)\n", note, note, kb[note]
		else
			printf "<FONT COLOR=\"#a0a0a0\">Not yet available for download</FONT>\n"
		printf "</P>\n"
		state = 0
	}

	printf "\n"
}
