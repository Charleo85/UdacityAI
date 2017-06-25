#!/bin/bash

for i in 1 2 3
do
  for (( j=1; j<=10; j++ ))
  do
  python run_search.py -p $i -s $j &
  TASK_PID=$!
  sleep 60
  kill $TASK_PID
done
done
