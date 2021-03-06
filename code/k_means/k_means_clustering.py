import random
import statistics
from functools import partial
import math

def distance(num_dimensions,first_point,second_point):
    tmp = [math.pow((second_point[ind] - val),2) for ind,val in enumerate(first_point)]
    return math.sqrt(sum(tmp))

def central_tendency(new_point,current_mean,discount_factor):
    return [current_mean[ind] + (discount_factor*(new_point[ind] - current_mean[ind])) for ind in range(len(current_mean))]

def k_means(data,k=3,epsilon=1):
    #if mean is the same for two successive iterations I'm done
    means = [random.choice(data) for _ in range(k)]
    dist = partial(distance,len(data[0]))
    [data.remove(mean) for mean in means]
    num_data_points_per_mean = {}.fromkeys([i for i in range(len(means))],1)
    while True:
        for datum in data:
            smallest_distance = float("inf")
            mean_to_update = None
            for ind,mean in enumerate(means):
                d = dist(datum,mean)
                if d < smallest_distance:
                    smallest_distance = d
                    mean_to_update = ind
            num_data_points_per_mean[mean_to_update] += 1
            prev_val = means[mean_to_update]
            means[mean_to_update] = central_tendency(datum,means[mean_to_update],1/num_data_points_per_mean[mean_to_update])
            if all([abs(means[mean_to_update][ind] - prev_val[ind]) < epsilon for i in range(len(prev_val))]):
                return means

if __name__ == '__main__':
    
    data = [[random.randint(2,150) for x in range(10)] for y in range(1000)]
    print(k_means(data))
