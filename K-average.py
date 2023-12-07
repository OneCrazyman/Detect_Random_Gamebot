import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import DBSCAN

displayWidth = 900 + 1
displayHeight = 1600 + 1
# #y700
# displayWidth = 1600 + 1
# displayHeight = 2560 + 1

FULL_RANGE = False

def loadTouchEventsFromFile(filename):
    loaded_touch_events = []
    with open(filename, "r") as file:
        for line in file:
            values = line.strip()[1:-1].split(", ")
            loaded_touch_events.append([int(values[0]), int(values[1])])
    return loaded_touch_events

def drawGraph(data,title = "Common Touch"):
    # 그래프 그리기
    x_coords = [x for [x, y] in data]
    y_coords = [y for [x, y] in data]

    if FULL_RANGE:
        plt.figure(figsize=(5, 10))
        plt.xlim(0, displayWidth - 1)
        plt.ylim(0, displayHeight - 1)
    plt.scatter(x_coords, y_coords, cmap='viridis', s=10)
    plt.title(title)
    plt.xlabel('x_coords')
    plt.ylabel('y_coords')
    plt.show()

def drawGraph_RED(data,title = "Common Touch"):
    # 그래프 그리기
    x_coords = [x for [x, y] in data]
    y_coords = [y for [x, y] in data]

    if FULL_RANGE:
        plt.figure(figsize=(5, 10))
        plt.xlim(0, displayWidth - 1)
        plt.ylim(0, displayHeight - 1)
    plt.scatter(x_coords, y_coords, c = 'r', s=10)
    plt.title(title)
    plt.xlabel('x_coords')
    plt.ylabel('y_coords')
    plt.show()


def drawClusterGraph(cluster_centers, cluster_labels, data, displayWidth, displayHeight):
    plt.figure(figsize=(5,10))
    for i in range(len(cluster_centers)):
        cluster_data = data[cluster_labels == i]
        x_coords = cluster_data[:, 0]
        y_coords = cluster_data[:, 1]
        plt.scatter(x_coords, y_coords, label=f'Cluster {i + 1}', s=1)

    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], color='red', label='Cluster Centers', s=5, marker='x')
    plt.title('Touch Coordinates - Clustered')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.xlim(0, displayWidth - 1)
    plt.ylim(0, displayHeight - 1)
    plt.show()

# 최적의 클러스터 수 찾기
def find_optimal_clusters_Elbow(data, max_k):
    sse = []
    for k in range(1, max_k):
        kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, max_k), sse, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('SSE')
    plt.show()

    return

def find_optimal_clusters_Silhouette(X, min_clusters=2, max_clusters=10):
    silhouette_scores = []
    for n_clusters in range(min_clusters, max_clusters + 1):
        # k-평균 모델 구성
        clusterer = KMeans(n_clusters=n_clusters, random_state=10)
        cluster_labels = clusterer.fit_predict(X)

        # 실루엣 스코어 계산
        silhouette_avg = silhouette_score(X, cluster_labels)
        silhouette_scores.append(silhouette_avg)

    best_silhouette_avg = max(silhouette_scores)
    best_k = silhouette_scores.index(best_silhouette_avg) + min_clusters

    # 최적의 k 값 출력
    print(f"The best silhouette_score is {best_silhouette_avg} for n_clusters = {best_k}")

    # 최적의 k 값으로 k-평균 모델 다시 실행
    optimal_clusterer = KMeans(n_clusters=best_k, random_state=10)
    optimal_cluster_labels = optimal_clusterer.fit_predict(X)

    cluster_labels = optimal_cluster_labels

    print("sihlouette 클러스터 레이블:", cluster_labels)

    return cluster_labels


# DBSCAN 모델 생성
def find_optimal_clusters_DBSCAN(data,eps=35,min_samples=1):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(data)

    # 클러스터링 결과 확인
    print("dbscan 클러스터 레이블:", dbscan.labels_)

    return dbscan.labels_

def view_clister(labels_,title="Clustering", s = 1 ):
    # 클러스터 시각화
    if FULL_RANGE:
        plt.figure(figsize=(5, 10))
        plt.xlim(0, displayWidth - 1)
        plt.ylim(0, displayHeight - 1)

    plt.scatter(data[:, 0], data[:, 1],c=labels_, cmap='viridis', s=s)
    plt.title(title)
    plt.xlabel('x_coords')
    plt.ylabel('y_coords')
    plt.show()

#가장 많은점만 다른색으로 분류
def plot_most_common_cluster(labels,s=10):
    x_coords = [x for [x, y] in data]
    y_coords = [y for [x, y] in data]

    unique_labels, label_counts = np.unique(labels, return_counts=True)
    most_common_label = unique_labels[np.argmax(label_counts)]

    colors = ['r' if label == most_common_label else 'b' for label in labels]

    if FULL_RANGE:
        plt.figure(figsize=(5, 10))
        plt.xlim(0, displayWidth - 1)
        plt.ylim(0, displayHeight - 1)
    plt.scatter(x_coords, y_coords, c=colors, s=s)
    plt.title('Touch Coordinates')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def plot_most_common_cluster_ONLY(labels,s=10):
    x_coords = [x for [x, y] in data]
    y_coords = [y for [x, y] in data]

    unique_labels, label_counts = np.unique(labels, return_counts=True)
    most_common_label = unique_labels[np.argmax(label_counts)]

    x_coords_filtered = []
    y_coords_filtered = []

    for x, y, label in zip(x_coords, y_coords, labels):
        if label == most_common_label:
            x_coords_filtered.append(x)
            y_coords_filtered.append(y)

    if FULL_RANGE:
        plt.figure(figsize=(5, 10))
        plt.xlim(0, displayWidth - 1)
        plt.ylim(0, displayHeight - 1)
    plt.scatter(x_coords_filtered, y_coords_filtered, c='r' , s=s)
    plt.title('Touch Coordinates')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    touchevents = [[x, y] for x, y in zip(x_coords_filtered, y_coords_filtered)]
    saveTouchEventsToFile(touchevents,filename)

    return x_coords_filtered,y_coords_filtered

# 좌표들의 중심점과 거리 계산
def calculate_average_distance_from_center(x_coords, y_coords):
    center_x = np.mean(x_coords)
    center_y = np.mean(y_coords)

    distances = []
    for x, y in zip(x_coords, y_coords):
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        distances.append(distance)

    avg_distance = np.mean(distances)
    return avg_distance

import math

def calculate_relative_spread(x_coords, y_coords):
    min_x = min(x_coords)
    max_x = max(x_coords)
    width = max_x - min_x

    min_y = min(y_coords)
    max_y = max(y_coords)
    height = max_y - min_y

    mean_x = np.mean(x_coords)
    mean_y = np.mean(y_coords)

    sum_distance = 0
    for x, y in zip(x_coords, y_coords):
        distance = np.sqrt((x - mean_x)**2 + (y - mean_y)**2)
        sum_distance += distance

    diagonal_length = np.sqrt(width**2 + height**2)
    relative_spread = sum_distance / (len(x_coords) * diagonal_length)

    return relative_spread

def calculate_relative_spread_real(x_coords, y_coords):
    min_x = min(x_coords)
    max_x = max(x_coords)
    width = max_x - min_x

    min_y = min(y_coords)
    max_y = max(y_coords)
    height = max_y - min_y

    mean_x = np.mean(x_coords)
    mean_y = np.mean(y_coords)

    sum_distance_x = 0
    sum_distance_y = 0

    for x in x_coords:
        sum_distance_x += ((x - mean_x)**2)
    for y in y_coords:
        sum_distance_y += ((y - mean_y)**2)

    div_x = sum_distance_x / (width**2)
    div_y = sum_distance_y / (height**2)
    relative_spread = np.sqrt(div_x + div_y)

    return relative_spread

def saveTouchEventsToFile(touch_events, file_index):
    with open(f"{file_index[:-4]}_ONLY.txt", "w") as file:
        for event in touch_events:
            file.write(f'{event}\n')
        print(f"Touch events saved to file {file_index}_ONLY_REDDD.txt.txt.\n\n\n")

def imsi(labels,s=10,lanum=0):
    x_coords = [x for [x, y] in data]
    y_coords = [y for [x, y] in data]

    x_coords_filtered = []
    y_coords_filtered = []

    for x, y, label in zip(x_coords, y_coords, labels):
        if label == lanum:
            x_coords_filtered.append(x)
            y_coords_filtered.append(y)

    if FULL_RANGE:
        plt.figure(figsize=(5, 10))
        plt.xlim(0, displayWidth - 1)
        plt.ylim(0, displayHeight - 1)
    plt.scatter(x_coords_filtered, y_coords_filtered, c='r' , s=s)
    plt.title('Touch Coordinates')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    touchevents = [[x, y] for x, y in zip(x_coords_filtered, y_coords_filtered)]
    # saveTouchEventsToFile(touchevents,filename)

    return x_coords_filtered,y_coords_filtered



filename = "touch_events_log_human.txt"
#데이터 입력
touch_events = loadTouchEventsFromFile(filename)
data = np.array([[x, y] for [x, y] in touch_events])

bool_Cluster = True
if bool_Cluster:
    # drawGraph(data,"Human Touch")
    # #k값 구하는 알고리즘 두개
    dbscan_labels = find_optimal_clusters_DBSCAN(data,eps=22)
    x_coords,y_coords = imsi(dbscan_labels,lanum=2) #사람 야매 포인터

    # #뷰 클리스터
    view_clister(dbscan_labels,title="Human Clustering",s=10)
    # plot_most_common_cluster(dbscan_labels,s=10)
    # # 분석용 클리스터 분류
    # x_coords,y_coords = plot_most_common_cluster_ONLY(dbscan_labels,s=15)

else:
    x_coords = [touch[0] for touch in touch_events]
    y_coords = [touch[1] for touch in touch_events]
    drawGraph_RED(data,title="Touch Area")

avr_distance = calculate_average_distance_from_center(x_coords,y_coords)
print(avr_distance)
relative_spread = calculate_relative_spread(x_coords,y_coords)
print(fr"relative_spread: {relative_spread}")