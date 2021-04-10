# MapReduce_AirlineData
This is an implementation of mapReduce on airline data using hadoop. The first mapReduce algorithm is used to get the best and worst airlines with respect to arrival delay time. The second mapReduce algorithm uses the three worst performing airlines to get the worst 15 fight routes for each with respect of to arrival delays. The third and final mapReduce algorithm is used to determine the most common reason for flight cancellations.

# How to run first algorithm (on time performance)
For "production" run this:
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file OnTimeMapper.py -mapper OnTimeMapper.py -file OnTimereducer.py -reducer OnTimeReducer.py -input 54785318_T_ONTIME_REPORTING_2021.csv -output on_time_output
then:
cat on_time_output/part-00000 | more | sort -nk2

For "testing/debugging" for this:
cat 54785318_T_ONTIME_REPORTING_2021.csv | ./OnTimeMapper.py | sort -k1,1 | ./OnTimeReducer.py | sort -nk2

# How to run second algorithm (worst routes)
For "production" run this:
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file routesMapper.py -mapper routesMapper.py -file routesReducer.py -reducer routesReducer.py -input 54785318_T_ONTIME_REPORTING_2021.csv -output routes_output
Then:
cat routes_output/part-00000 | more | sort -nk2

# How to run third algorithm (cancellation reasons)
For "production" run this:
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file reasonsMapper.py -mapper reasonsMapper.py -file reasonsReducer.py -reducer reasonsReducer.py -input 54785318_T_ONTIME_REPORTING_2021.csv -output reasons_output
Then:
cat reasons_output/part-00000 | more | sort -nk2
