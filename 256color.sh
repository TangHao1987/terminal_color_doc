#!/usr/bin/env bash
#Foreground
for clfg in {30..37} {90..97} 39 ; do
    #Formatting
    for attr in 0 1 2 4 5 7 ; do
        #Print the result
        echo -en "\e[${attr};${clfg}m ^[${attr};${clfg}m \e[0m"
    done
    echo #Newline
done

exit 0