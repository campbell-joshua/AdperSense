import tensorflow as tf
import numpy as np

from basic_script import *

n_features = 2
n_clusters = 3
n_samples_per_cluster = 500
seed = 700
embiggen_factor = 70


data_centroids, samples = create_samples(n_clusters, n_samples_per_cluster, n_features, embiggen_factor, seed)
centroids = choose_random_centroids(samples, n_clusters, seed=seed)

model = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(samples)
    for i in range(10):
        nearest_indices = assign_to_nearest(samples, centroids)
        centroids = update_centroids(samples, nearest_indices, n_clusters)
    sample_values = session.run(samples)
    updated_centroid_value = session.run(centroids)
    print(updated_centroid_value)

plot_clusters(sample_values, updated_centroid_value, n_samples_per_cluster)
