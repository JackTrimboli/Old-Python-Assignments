import random
import math
# import statistics
# import matplotlib.pyplot as plt


_lambda = 10
_num_events = 100
_event_num = []
_inter_event_times = []
_event_times = []
_event_time = 0

for i in range(_num_events):
    _event_num.append(i)
    # Get a random probability value from the uniform distribution's PDF
    n = random.random()

    # Generate the inter-event time from the exponential distribution's CDF using the Inverse-CDF technique
    _inter_event_time = -math.log(1.0 - n) / _lambda
    _inter_event_times.append(_inter_event_time)

    # Add the inter-event time to the running sum to get the next absolute event time
    _event_time = _event_time + _inter_event_time
    _event_times.append(math.ceil(_event_time))

dummy = 0
dummy2 = 1
# plot the absolute event times
# fig = plt.figure()
# fig.suptitle('Arrival time vs visitor index plot')
# plot, = plt.plot(_event_num, _event_times, 'ko', markersize=1.5)
# plt.legend(handles=[plot])
# plt.xlabel('Visitors')
# plt.ylabel('Arrival Time in Minutes')
# plt.show()
