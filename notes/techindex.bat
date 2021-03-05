ls -l *.pdf | d2u | gawk -f techindex.awk - techindex.txt >techindex.htm
u2d techlist.htm
u2d techindex.htm
cat index-pre.htm techlist.htm index-sep.htm techindex.htm index-post.htm >index.gen
