import numpy as np
import random


class KMeans:
    def __init__(self, n_clusters=3, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None
        self.inertia_ = 0  # Initialize inertia_

    def fit(self, X):
        # Randomly pick initial centroids
        random_idx = random.sample(range(len(X)), self.n_clusters)
        self.centroids = X[random_idx]

        for _ in range(self.max_iter):
            # Assign points to nearest centroid
            clusters = self._assign_clusters(X)

            # Store old centroids for convergence check
            old_centroids = self.centroids.copy()

            # Update centroids
            self.centroids = self._update_centroids(X, clusters)

            # Check if converged
            if np.all(old_centroids == self.centroids):
                break

        # Calculate inertia (sum of squared distances)
        self.inertia_ = self._calculate_inertia(X, clusters)
        return clusters

    def _assign_clusters(self, X):
        labels = []
        for point in X:
            # Calculate distance to each centroid
            distances = [np.linalg.norm(point - c) for c in self.centroids]
            labels.append(np.argmin(distances))
        return np.array(labels)

    def _update_centroids(self, X, clusters):
        new_centroids = []
        for cluster_id in np.unique(clusters):
            cluster_points = X[clusters == cluster_id]
            new_centroids.append(cluster_points.mean(axis=0))
        return np.array(new_centroids)

    def _calculate_inertia(self, X, clusters):
        inertia = 0
        for i, point in enumerate(X):
            centroid = self.centroids[clusters[i]]
            inertia += np.sum((point - centroid) ** 2)
        return inertia

    def predict(self, X):
        """Predict cluster for new data points"""
        if self.centroids is None:
            raise ValueError("Model not fitted yet. Call fit() first.")

        labels = []
        for point in X:
            distances = [np.linalg.norm(point - c) for c in self.centroids]
            labels.append(np.argmin(distances))
        return np.array(labels)


# import random
# import numpy as np
#
#
# class KMeans:
#     def __init__(self, n_clusters=8, max_iter=100):
#         self.n_clusters = n_clusters
#         self.max_iter = max_iter
#         self.centroids = None
#
#     def fit(self, X):
#         random_index = random.sample(range(0, X.shape[0]), self.n_clusters)
#         self.centroids = X[random_index]
#
#         for i in range(self.max_iter):
#             # assign clusters
#             cluster_group = self.assign_clusters(X)
#             old_centroids = self.centroids.copy()  # Use copy to avoid reference issues
#             # move centroids
#             self.centroids = self.move_centroids(X, cluster_group)
#             # check finish
#             if (old_centroids == self.centroids).all():
#                 break
#
#         return cluster_group
#
#     def assign_clusters(self, X):
#         cluster_group = []
#         for row in X:
#             distances = []
#             for centroid in self.centroids:
#                 distances.append(np.sqrt(np.dot(row - centroid, row - centroid)))
#             min_distance = min(distances)
#             index_pos = distances.index(min_distance)
#             cluster_group.append(index_pos)
#         return np.array(cluster_group)
#
#     def move_centroids(self, X, cluster_group):
#         new_centroids = []  # Initialize empty list
#         cluster_type = np.unique(cluster_group)
#
#         for type in cluster_type:
#             # APPEND to the list, don't reassign
#             new_centroids.append(X[cluster_group == type].mean(axis=0))
#
#         return np.array(new_centroids)
#
#     def _update_centroids(self, X, clusters):
#         new_centroids = []
#         for cluster_id in np.unique(clusters):
#             cluster_points = X[clusters == cluster_id]
#             new_centroids.append(cluster_points.mean(axis=0))
#         return np.array(new_centroids)
#
#     def _calculate_inertia(self, X, clusters):
#         inertia = 0
#         for i, point in enumerate(X):
#             centroid = self.centroids[clusters[i]]
#             inertia += np.sum((point - centroid) ** 2)
#         return inertia
#
#     def predict(self, X):
#         """Predict cluster for new data points"""
#         labels = []
#         for point in X:
#             distances = [np.linalg.norm(point - c) for c in self.centroids]
#             labels.append(np.argmin(distances))
#         return np.array(labels)