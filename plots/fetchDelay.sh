#!/bin/bash

FILES1=/home/vkirany/mptcptests/mptcp/
for e in 'er3' 
do
for p in 1P 2P 1P+P
do
for x in 'tail20-20' 'tail20-30' 'tail30-20' 'tail20-120' 'tail120-20'
do
echo "ER $e and Scene $x and P $p"
f1=$FILES1$e'/'$x'/'$p'/'Run2'/'delay

 	cat $f1
	
done
done 
done
