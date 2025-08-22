# Dijkstra最短路径算法

## 1. 算法描述

Dijkstra算法是一种用于在带权图中找到从源点到所有其他顶点的最短路径的算法。它使用贪心策略，每次选择当前距离最小的未访问顶点进行扩展。

### 1.1 适用场景
- 带权有向图或无向图的最短路径问题
- 考研中图论算法的重要考点
- 网络路由、导航系统等实际应用

### 1.2 复杂度分析
| 指标            | 值               |
|-----------------|------------------|
| 时间复杂度      | O(V²) 或 O(E log V) |
| 空间复杂度      | O(V)             |
| 其中 V 为顶点数，E 为边数 |

---

## 2. 伪代码

```
Dijkstra(graph, source):
    // 初始化距离数组和访问数组
    dist[V] = {INF, INF, ..., INF}
    visited[V] = {false, false, ..., false}
    dist[source] = 0
    
    for i = 0 to V-1:
        // 找到未访问顶点中距离最小的
        u = findMinDistance(dist, visited)
        visited[u] = true
        
        // 更新通过u可达的顶点的距离
        for each neighbor v of u:
            if not visited[v] and dist[u] + weight(u,v) < dist[v]:
                dist[v] = dist[u] + weight(u,v)
    
    return dist
```

---

## 3. C++ 实现

```cpp
#include <vector>
#include <iostream>
#include <climits>
#include <queue>
#include <utility>

// 使用邻接矩阵表示的图
class Graph {
private:
    std::vector<std::vector<int>> adjMatrix;
    int V;
    
public:
    Graph(int vertices) : V(vertices) {
        adjMatrix.resize(V, std::vector<int>(V, 0));
    }
    
    void addEdge(int u, int v, int weight) {
        adjMatrix[u][v] = weight;
        adjMatrix[v][u] = weight;  // 无向图
    }
    
    std::vector<int> dijkstra(int source) {
        std::vector<int> dist(V, INT_MAX);
        std::vector<bool> visited(V, false);
        
        dist[source] = 0;
        
        for (int count = 0; count < V - 1; count++) {
            // 找到未访问顶点中距离最小的
            int u = findMinDistance(dist, visited);
            visited[u] = true;
            
            // 更新通过u可达的顶点的距离
            for (int v = 0; v < V; v++) {
                if (!visited[v] && adjMatrix[u][v] != 0 && 
                    dist[u] != INT_MAX && 
                    dist[u] + adjMatrix[u][v] < dist[v]) {
                    dist[v] = dist[u] + adjMatrix[u][v];
                }
            }
        }
        
        return dist;
    }
    
private:
    int findMinDistance(const std::vector<int>& dist, const std::vector<bool>& visited) {
        int minDist = INT_MAX;
        int minIndex = -1;
        
        for (int v = 0; v < V; v++) {
            if (!visited[v] && dist[v] <= minDist) {
                minDist = dist[v];
                minIndex = v;
            }
        }
        
        return minIndex;
    }
};

// 使用优先队列优化的Dijkstra算法
std::vector<int> dijkstraOptimized(const std::vector<std::vector<std::pair<int, int>>>& graph, int source) {
    int V = graph.size();
    std::vector<int> dist(V, INT_MAX);
    std::priority_queue<std::pair<int, int>, 
                       std::vector<std::pair<int, int>>, 
                       std::greater<std::pair<int, int>>> pq;
    
    dist[source] = 0;
    pq.push({0, source});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        
        if (d > dist[u]) continue;  // 跳过已处理的顶点
        
        for (const auto& neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    
    return dist;
}

// 测试函数
void TestDijkstra() {
    Graph g(6);
    
    // 添加边 (u, v, weight)
    g.addEdge(0, 1, 4);
    g.addEdge(0, 2, 2);
    g.addEdge(1, 2, 1);
    g.addEdge(1, 3, 5);
    g.addEdge(2, 3, 8);
    g.addEdge(2, 4, 10);
    g.addEdge(3, 4, 2);
    g.addEdge(3, 5, 6);
    g.addEdge(4, 5, 3);
    
    int source = 0;
    std::vector<int> distances = g.dijkstra(source);
    
    std::cout << "从顶点 " << source << " 到各顶点的最短距离：" << std::endl;
    for (int i = 0; i < distances.size(); i++) {
        if (distances[i] == INT_MAX) {
            std::cout << "顶点 " << i << ": 不可达" << std::endl;
        } else {
            std::cout << "顶点 " << i << ": " << distances[i] << std::endl;
        }
    }
}

int main() {
    TestDijkstra();
    return 0;
}
```

---

## 4. 注意事项

- **图的性质**：Dijkstra算法只适用于带非负权重的图
- **初始化**：源点距离初始化为0，其他顶点初始化为无穷大
- **贪心选择**：每次选择当前距离最小的未访问顶点
- **考研重点**：理解贪心策略和距离更新的逻辑

---

## 5. 测试用例

### 5.1 典型用例
- 输入：6个顶点的图，源点为0
- 输出：从顶点0到各顶点的最短距离

### 5.2 边界用例
- 输入：单个顶点的图
- 输出：距离为0
- 输入：存在负权边的图
- 输出：算法可能不正确（需要使用Bellman-Ford算法）

---

## 6. 常见错误与陷阱

- **负权边**：Dijkstra算法不能处理负权边
- **优先队列使用错误**：在优化版本中忘记跳过已处理的顶点
- **距离更新条件**：忘记检查当前距离是否为无穷大
- **考研易错点**：不理解贪心策略的正确性和距离更新的必要性

---

## 7. 变种算法

### 7.1 单源单目标最短路径
```cpp
int dijkstraSingleTarget(const std::vector<std::vector<std::pair<int, int>>>& graph, 
                         int source, int target) {
    int V = graph.size();
    std::vector<int> dist(V, INT_MAX);
    std::priority_queue<std::pair<int, int>, 
                       std::vector<std::pair<int, int>>, 
                       std::greater<std::pair<int, int>>> pq;
    
    dist[source] = 0;
    pq.push({0, source});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        
        if (u == target) return d;  // 找到目标顶点
        if (d > dist[u]) continue;
        
        for (const auto& neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    
    return dist[target];
}
```

### 7.2 路径重建
```cpp
std::vector<int> dijkstraWithPath(const std::vector<std::vector<std::pair<int, int>>>& graph, 
                                  int source, int target) {
    int V = graph.size();
    std::vector<int> dist(V, INT_MAX);
    std::vector<int> parent(V, -1);
    std::priority_queue<std::pair<int, int>, 
                       std::vector<std::pair<int, int>>, 
                       std::greater<std::pair<int, int>>> pq;
    
    dist[source] = 0;
    pq.push({0, source});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        
        if (d > dist[u]) continue;
        
        for (const auto& neighbor : graph[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }
    
    // 重建路径
    std::vector<int> path;
    for (int v = target; v != -1; v = parent[v]) {
        path.push_back(v);
    }
    std::reverse(path.begin(), path.end());
    
    return path;
}
```

---

## 8. 优化技巧

- **优先队列优化**：使用优先队列代替线性查找最小距离顶点
- **邻接表表示**：对于稀疏图，使用邻接表比邻接矩阵更高效
- **早期终止**：在单目标版本中，找到目标顶点后可以立即返回

---

通过以上内容，考研学生可以全面理解Dijkstra算法的原理、实现和优化方法，掌握贪心策略在图论算法中的应用。 