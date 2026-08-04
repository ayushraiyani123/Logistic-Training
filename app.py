from sklearn.datasets import make_blobs
import pandas as pd
import matplotlib.pyplot as plt
from kmeans import KMeans
import numpy as np

df = pd.read_csv('student_clustering.csv')
X=df.iloc[:,:].values
# y = df.iloc[:,1:].values

# Generate sample data (4 clusters)
# centeroids = [(-5, -5), (5, 5), (-2.5, 2.5), (2.5, -2.5)]
# cluster_std = [1.0, 1.0, 1.0, 1.0]
# X, y = make_blobs(n_samples=100, centers=centeroids,
#                   cluster_std=cluster_std, n_features=2, random_state=2)

# Visualize raw data
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1])
plt.title('Raw Data (4 Clusters)')
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.grid(True, alpha=0.3)

# Apply K-Means
km = KMeans(n_clusters=4, max_iter=200)
y_means = km.fit(X)

# Plot clustered data
plt.subplot(1, 2, 2)
colors = ['red', 'blue', 'yellow', 'green']
for i in range(4):
    mask = y_means == i
    if mask.sum() > 0:
        plt.scatter(X[mask, 0], X[mask, 1],
                   color=colors[i], label=f'Cluster {i}',
                   s=50, alpha=0.7)

# Plot centroids
plt.scatter(km.centroids[:, 0], km.centroids[:, 1],
           color='black', marker='X', s=200,
           label='Centroids', linewidths=2)

plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.title('K-Means Clustering (k=4)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Cluster sizes: {np.bincount(y_means)}")
print(f"Centroids:\n{km.centroids}")

#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_blobs
# from kmeans import KMeans
#
# # ============================================
# # STEP 1: Generate Sample Data
# # ============================================
#
# print("Generating sample data...")
# centers = [(-5, -5), (5, 5), (-2.5, 2.5)]
# X, y_true = make_blobs(n_samples=100, centers=centers,
#                        cluster_std=1.0, random_state=42)
#
# print("\n" + "="*50)
# print(f"Data shape: {X.shape}")
# print(f"Number of samples: {len(X)}")
#
# # ============================================
# # STEP 2: Find Optimal Number of Clusters (Elbow Method)
# # ============================================
#
# print("\n" + "="*50)
# print("Finding optimal number of clusters...")
# print("="*50)
#
# k_values = range(1, 11)
# inertias = []
#
# for k in k_values:
#     km = KMeans(n_clusters=k)
#     km.fit(X)
#     inertias.append(km.inertia_)
#     print(f"k={k}: inertia={km.inertia_:.0f}")
#
# # ============================================
# # STEP 3: Plot Elbow Curve
# # ============================================
#
# plt.figure(figsize=(15, 5))
#
# # Plot 1: Elbow Method
# plt.subplot(1, 3, 1)
# plt.plot(k_values, inertias, 'bo-', linewidth=2, markersize=8)
# plt.xlabel('Number of Clusters (k)')
# plt.ylabel('Inertia (WCSS)')
# plt.title('Elbow Method')
# plt.grid(True, alpha=0.3)
#
# # Mark the elbow point (k=3)
# optimal_k = 3
# plt.axvline(x=optimal_k, color='red', linestyle='--',
#             label=f'Optimal k={optimal_k}')
# plt.legend()
#
# # ============================================
# # STEP 4: Apply K-Means with Optimal k
# # ============================================
#
# print(f"\nApplying K-Means with k={optimal_k}...")
#
# km_final = KMeans(n_clusters=optimal_k)
# labels = km_final.fit(X)
#
# print(f"Cluster sizes: {np.bincount(labels)}")
# print(f"Final inertia: {km_final.inertia_:.0f}")
#
# # ============================================
# # STEP 5: Visualize Clustering Results
# # ============================================
#
# # Plot 2: Clustering Result
# plt.subplot(1, 3, 2)
# colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
#
# for i in range(optimal_k):
#     mask = labels == i
#     if mask.sum() > 0:
#         plt.scatter(X[mask, 0], X[mask, 1],
#                    color=colors[i % len(colors)],
#                    label=f'Cluster {i}', s=50, alpha=0.7)
#
# # Plot centroids
# plt.scatter(km_final.centroids[:, 0], km_final.centroids[:, 1],
#            color='black', marker='X', s=200,
#            label='Centroids', linewidths=2)
#
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.title(f'K-Means Clustering (k={optimal_k})')
# plt.legend()
# plt.grid(True, alpha=0.3)
#
# # Plot 3: Show True Clusters (for comparison)
# plt.subplot(1, 3, 3)
# for i in range(3):
#     mask = y_true == i
#     plt.scatter(X[mask, 0], X[mask, 1],
#                color=colors[i % len(colors)],
#                label=f'True Cluster {i}', s=50, alpha=0.7)
#
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.title('True Clusters (Ground Truth)')
# plt.legend()
# plt.grid(True, alpha=0.3)
#
# plt.tight_layout()
# plt.show()
#
# # ============================================
# # STEP 6: Test with New Data Point
# # ============================================
#
# print("\n" + "="*50)
# print("Testing with a new data point...")
# print("="*50)
#
# # Create a new data point
# new_point = np.array([[0, 0]])
# predicted_cluster = km_final.predict(new_point)
#
# print(f"New point: {new_point[0]}")
# print(f"Predicted cluster: {predicted_cluster[0]}")
# print(f"Centroids:\n{km_final.centroids}")
#
# # Visualize the new point
# plt.figure(figsize=(8, 6))
#
# # Plot existing clusters
# for i in range(optimal_k):
#     mask = labels == i
#     plt.scatter(X[mask, 0], X[mask, 1],
#                color=colors[i % len(colors)],
#                label=f'Cluster {i}', alpha=0.5)
#
# # Plot centroids
# plt.scatter(km_final.centroids[:, 0], km_final.centroids[:, 1],
#            color='black', marker='X', s=200, label='Centroids')
#
# # Plot new point
# plt.scatter(new_point[0, 0], new_point[0, 1],
#            color='red', marker='*', s=500,
#            label=f'New Point (Cluster {predicted_cluster[0]})',
#            edgecolors='black', linewidths=2)
#
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.title('Predicting Cluster for New Data Point')
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.show()
#
# # ============================================
# # STEP 7: Summary
# # ============================================
#
# print("\n" + "="*50)
# print("SUMMARY")
# print("="*50)
# print(f"✓ Dataset: 100 samples, 2 features")
# print(f"✓ Optimal clusters: {optimal_k}")
# print(f"✓ Cluster distribution: {np.bincount(labels)}")
# print(f"✓ Inertia: {km_final.inertia_:.0f}")
# print(f"✓ Centroids:\n{km_final.centroids}")