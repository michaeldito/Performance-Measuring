#!/bin/bash

# $1 is external IP address, passed as arg to script
# $2 has number of nodes we are testing

numNodes=$2

# declare our connections array
declare -a C=(10 20 50 100 200 500 700 1000 1200 1500 2000 2500 3000)

# run the test for all concurrency levels
for i in "${C[@]}"
do
	echo "Beginning Test for C = " $i
	# run the simulation with all values of C and redirect the output to a file
	ab -p payload.json -T application/json -m POST -c $i -n 10000 -s 10 -r http://$1/fibonacci >> result$i.txt
	# grep mean time per request, 98%, and longest request and redirect output to file
	grep 'Concurrency' result$i.txt >> "$numNodes-Results.txt"
	grep 'Time per request' result$i.txt >> "$numNodes-Results.txt"
	grep '98%' result$i.txt >> "$numNodes-Results.txt"
	grep 'longest request' result$i.txt >> "$numNodes-Results.txt"
	echo '--------------------------------------------' >> "$numNodes-Results.txt"
	echo 'End of Test for C = ' $i
	echo ''
done

# remove the temp test result files
rm result*.txt

# print the results without the extra mean we didn't want
cat $numNodes-Results.txt | sed '/(mean, across $numNodes- concurrent requests)/d'

# extract Mean Request Time, Longest Request Time, and 98%

# gets floats on any lines that say ‘(mean)’
grep '(mean)' $numNodes-Results.txt  | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' > $numNodes-mean.txt

# cut out $numNodes- values after %, extract float, remove leading whitespace
grep '98%' $numNodes-Results.txt | cut -d "%" -f 2 | sed 's/*%[^0-9]*//g' | sed 's/^ *//g' > $numNodes-98.txt 

# same as above but for longest request
grep 'longest request' $numNodes-Results.txt | cut -d "%" -f 2 | sed 's/*%[^0-9]*//g' | sed 's/^ *//g' > $numNodes-longest.txt

# make a directory for the data and move all files there
mkdir $numNodes-data
mv $numNodes*.txt $numNodes-data
