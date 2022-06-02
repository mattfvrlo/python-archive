for COLOR in {0..255}
do
    TAG="\033[${STYLE};${COLOR}m"
    STR="String cheese!"
    echo -ne "${TAG}${STR}${NONE}\n"
done

for r in {0..255}
do
	for g in {0..255}
	do
		for b in {0..255}
		do
			TAG="\033[38;2;${r};${g};${b}m"
			STR="XXXX"
			echo -ne "${TAG}${STR}${NONE}"
		done
	done
done