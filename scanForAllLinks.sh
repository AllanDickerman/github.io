for f in *; do perl -ne 'while (/href="(.*?)"/g){$u{$1}=1}; END{for $l (grep(!/javascript/, sort keys %u)) {print "$l\n"}}' $f; done | sort | uniq > all_links.txt
