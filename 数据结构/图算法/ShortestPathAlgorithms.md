# 最短路径算法 (Shortest Path Algorithms)

## 算法描述

最短路径算法用于在图中找到从一个顶点到另一个顶点的最短路径。根据图的类型（有向/无向、带权/无权、正权/负权）和需求，可以选择不同的算法。

**核心思想**：
- **Dijkstra算法**：适用于无负权边的单源最短路径
- **Floyd-Warshall算法**：适用于多源最短路径，可处理负权边
- **Bellman-Ford算法**：适用于有负权边的单源最短路径，可检测负环

## 复杂度分析

| 算法 | 时间复杂度 | 空间复杂度 | 适用场景 |
|------|------------|------------|----------|
| Dijkstra | O(V²) / O(E log V) | O(V) | 无负权边 |
| Floyd-Warshall | O(V³) | O(V²) | 多源最短路径 |
| Bellman-Ford | O(VE) | O(V) | 有负权边 |

## 伪代码

```
// Dijkstra算法
迪杰斯特拉(图, 源点)
    初始化单源最短路径(图, 源点)
    已访问集合 = 空集
    优先队列 = 图.所有顶点
    当 优先队列不为空
        u = 提取最小值(优先队列)
        已访问集合 = 已访问集合 ∪ {u}
        对于 每个顶点 v ∈ 图.邻接表[u]
            松弛(u, v, 权重)

// Floyd-Warshall算法
弗洛伊德-沃舍尔(权重矩阵)
    n = 权重矩阵.行数
    距离矩阵 = 权重矩阵
    对于 k = 1 到 n
        对于 i = 1 到 n
            对于 j = 1 到 n
                距离矩阵[i][j] = 最小值(距离矩阵[i][j], 距离矩阵[i][k] + 距离矩阵[k][j])
    返回 距离矩阵

// Bellman-Ford算法
贝尔曼-福特(图, 源点)
    初始化单源最短路径(图, 源点)
    对于 i = 1 到 |图.顶点数| - 1
        对于 每条边 (u, v) ∈ 图.边集
            松弛(u, v, 权重)
    对于 每条边 (u, v) ∈ 图.边集
        如果 v.距离 > u.距离 + 权重(u, v)
            返回 假
    返回 真
```

## C++ 实现

### 图的数据结构

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

// 图的邻接矩阵表示
class Graph {
private:
    std::vector<std::vector<int>> adjacencyMatrix;
    int vertices;
    
public:
    Graph(int V) : vertices(V) {
        adjacencyMatrix.resize(V, std::vector<int>(V, std::numeric_limits<int>::max()));
        for (int i = 0; i < V; i++) {
            adjacencyMatrix[i][i] = 0;
        }
    }
    
    void addEdge(int u, int v, int weight) {
        adjacencyMatrix[u][v] = weight;
    }
    
    int getWeight(int u, int v) const {
        return adjacencyMatrix[u][v];
    }
    
    int getVertices() const {
        return vertices;
    }
    
    const std::vector<std::vector<int>>& getMatrix() const {
        return adjacencyMatrix;
    }
};

// 图的邻接表表示
struct Edge {
    int destination;
    int weight;
    Edge(int dest, int w) : destination(dest), weight(w) {}
};

class AdjacencyListGraph {
private:
    std::vector<std::vector<Edge>> adjacencyList;
    int vertices;
    
public:
    AdjacencyListGraph(int V) : vertices(V) {
        adjacencyList.resize(V);
    }
    
    void addEdge(int u, int v, int weight) {
        adjacencyList[u].emplace_back(v, weight);
    }
    
    const std::vector<Edge>& getNeighbors(int u) const {
        return adjacencyList[u];
    }
    
    int getVertices() const {
        return vertices;
    }
};
```

### Dijkstra算法实现

```cpp
class DijkstraAlgorithm {
public:
    // 使用邻接矩阵的Dijkstra算法
    static std::vector<int> dijkstraMatrix(const Graph& graph, int source) {
        int V = graph.getVertices();
        std::vector<int> distance(V, std::numeric_limits<int>::max());
        std::vector<bool> visited(V, false);
        
        distance[source] = 0;
        
        for (int count = 0; count < V - 1; count++) {
            // 找到未访问的最小距离顶点
            int minDistance = std::numeric_limits<int>::max();
            int minIndex = -1;
            
            for (int v = 0; v < V; v++) {
                if (!visited[v] && distance[v] < minDistance) {
                    minDistance = distance[v];
                    minIndex = v;
                }
            }
            
            if (minIndex == -1) break;
            
            visited[minIndex] = true;
            
            // 更新相邻顶点的距离
            for (int v = 0; v < V; v++) {
                if (!visited[v] && 
                    graph.getWeight(minIndex, v) != std::numeric_limits<int>::max() &&
                    distance[minIndex] != std::numeric_limits<int>::max() &&
                    distance[minIndex] + graph.getWeight(minIndex, v) < distance[v]) {
                    distance[v] = distance[minIndex] + graph.getWeight(minIndex, v);
                }
            }
        }
        
        return distance;
    }
    
    // 使用优先队列的Dijkstra算法（更高效）
    static std::vector<int> dijkstraPriorityQueue(const AdjacencyListGraph& graph, int source) {
        int V = graph.getVertices();
        std::vector<int> distance(V, std::numeric_limits<int>::max());
        
        // 使用优先队列存储 {距离, 顶点}
        std::priority_queue<std::pair<int, int>, 
                          std::vector<std::pair<int, int>>, 
                          std::greater<std::pair<int, int>>> pq;
        
        distance[source] = 0;
        pq.push({0, source});
        
        while (!pq.empty()) {
            int currentDistance = pq.top().first;
            int currentVertex = pq.top().second;
            pq.pop();
            
            // 如果当前距离大于已知距离，跳过
            if (currentDistance > distance[currentVertex]) {
                continue;
            }
            
            // 遍历相邻顶点
            for (const Edge& edge : graph.getNeighbors(currentVertex)) {
                int neighbor = edge.destination;
                int weight = edge.weight;
                
                if (distance[currentVertex] + weight < distance[neighbor]) {
                    distance[neighbor] = distance[currentVertex] + weight;
                    pq.push({distance[neighbor], neighbor});
                }
            }
        }
        
        return distance;
    }
    
    // 打印最短路径
    static void printShortestPaths(const std::vector<int>& distances, int source) {
        std::cout << "从顶点 " << source << " 到各顶点的最短距离：" << std::endl;
        for (int i = 0; i < distances.size(); i++) {
            if (distances[i] == std::numeric_limits<int>::max()) {
                std::cout << "顶点 " << i << ": 不可达" << std::endl;
            } else {
                std::cout << "顶点 " << i << ": " << distances[i] << std::endl;
            }
        }
    }
};
```

### Floyd-Warshall算法实现

```cpp
class FloydWarshallAlgorithm {
public:
    // Floyd-Warshall算法实现
    static std::vector<std::vector<int>> floydWarshall(const Graph& graph) {
        int V = graph.getVertices();
        std::vector<std::vector<int>> distance = graph.getMatrix();
        
        // 三重循环：k是中间顶点
        for (int k = 0; k < V; k++) {
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++) {
                    // 避免整数溢出
                    if (distance[i][k] != std::numeric_limits<int>::max() &&
                        distance[k][j] != std::numeric_limits<int>::max() &&
                        distance[i][k] + distance[k][j] < distance[i][j]) {
                        distance[i][j] = distance[i][k] + distance[k][j];
                    }
                }
            }
        }
        
        return distance;
    }
    
    // 检测负环
    static bool hasNegativeCycle(const std::vector<std::vector<int>>& distance) {
        int V = distance.size();
        for (int i = 0; i < V; i++) {
            if (distance[i][i] < 0) {
                return true;
            }
        }
        return false;
    }
    
    // 打印所有顶点对之间的最短距离
    static void printAllPairsShortestPaths(const std::vector<std::vector<int>>& distance) {
        int V = distance.size();
        std::cout << "所有顶点对之间的最短距离：" << std::endl;
        
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (distance[i][j] == std::numeric_limits<int>::max()) {
                    std::cout << "∞ ";
                } else {
                    std::cout << distance[i][j] << " ";
                }
            }
            std::cout << std::endl;
        }
    }
};
```

### Bellman-Ford算法实现

```cpp
class BellmanFordAlgorithm {
public:
    // Bellman-Ford算法实现
    static std::vector<int> bellmanFord(const AdjacencyListGraph& graph, int source) {
        int V = graph.getVertices();
        std::vector<int> distance(V, std::numeric_limits<int>::max());
        distance[source] = 0;
        
        // 进行V-1次松弛操作
        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (const Edge& edge : graph.getNeighbors(u)) {
                    int v = edge.destination;
                    int weight = edge.weight;
                    
                    if (distance[u] != std::numeric_limits<int>::max() &&
                        distance[u] + weight < distance[v]) {
                        distance[v] = distance[u] + weight;
                    }
                }
            }
        }
        
        // 检测负环
        for (int u = 0; u < V; u++) {
            for (const Edge& edge : graph.getNeighbors(u)) {
                int v = edge.destination;
                int weight = edge.weight;
                
                if (distance[u] != std::numeric_limits<int>::max() &&
                    distance[u] + weight < distance[v]) {
                    std::cout << "图中存在负环！" << std::endl;
                    return std::vector<int>();
                }
            }
        }
        
        return distance;
    }
    
    // 带路径重建的Bellman-Ford算法
    static std::pair<std::vector<int>, std::vector<int>> bellmanFordWithPath(
        const AdjacencyListGraph& graph, int source) {
        int V = graph.getVertices();
        std::vector<int> distance(V, std::numeric_limits<int>::max());
        std::vector<int> predecessor(V, -1);
        
        distance[source] = 0;
        
        // 进行V-1次松弛操作
        for (int i = 0; i < V - 1; i++) {
            for (int u = 0; u < V; u++) {
                for (const Edge& edge : graph.getNeighbors(u)) {
                    int v = edge.destination;
                    int weight = edge.weight;
                    
                    if (distance[u] != std::numeric_limits<int>::max() &&
                        distance[u] + weight < distance[v]) {
                        distance[v] = distance[u] + weight;
                        predecessor[v] = u;
                    }
                }
            }
        }
        
        return {distance, predecessor};
    }
    
    // 重建最短路径
    static std::vector<int> reconstructPath(const std::vector<int>& predecessor, 
                                          int source, int destination) {
        std::vector<int> path;
        
        if (predecessor[destination] == -1 && source != destination) {
            return path;  // 没有路径
        }
        
        int current = destination;
        while (current != -1) {
            path.push_back(current);
            current = predecessor[current];
        }
        
        std::reverse(path.begin(), path.end());
        return path;
    }
};
```

## 使用示例

```cpp
int main() {
    // 创建测试图
    Graph graph(5);
    graph.addEdge(0, 1, 4);
    graph.addEdge(0, 2, 2);
    graph.addEdge(1, 2, 1);
    graph.addEdge(1, 3, 5);
    graph.addEdge(2, 3, 8);
    graph.addEdge(2, 4, 10);
    graph.addEdge(3, 4, 2);
    
    // Dijkstra算法测试
    std::cout << "=== Dijkstra算法 ===" << std::endl;
    std::vector<int> dijkstraResult = DijkstraAlgorithm::dijkstraMatrix(graph, 0);
    DijkstraAlgorithm::printShortestPaths(dijkstraResult, 0);
    
    // Floyd-Warshall算法测试
    std::cout << "\n=== Floyd-Warshall算法 ===" << std::endl;
    std::vector<std::vector<int>> floydResult = FloydWarshallAlgorithm::floydWarshall(graph);
    FloydWarshallAlgorithm::printAllPairsShortestPaths(floydResult);
    
    // Bellman-Ford算法测试
    std::cout << "\n=== Bellman-Ford算法 ===" << std::endl;
    AdjacencyListGraph adjGraph(5);
    adjGraph.addEdge(0, 1, 4);
    adjGraph.addEdge(0, 2, 2);
    adjGraph.addEdge(1, 2, 1);
    adjGraph.addEdge(1, 3, 5);
    adjGraph.addEdge(2, 3, 8);
    adjGraph.addEdge(2, 4, 10);
    adjGraph.addEdge(3, 4, 2);
    
    auto bellmanResult = BellmanFordAlgorithm::bellmanFordWithPath(adjGraph, 0);
    DijkstraAlgorithm::printShortestPaths(bellmanResult.first, 0);
    
    // 重建路径
    std::vector<int> path = BellmanFordAlgorithm::reconstructPath(bellmanResult.second, 0, 4);
    std::cout << "从0到4的最短路径: ";
    for (int vertex : path) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 算法特点

### Dijkstra算法
- **优点**：效率高，适用于稠密图
- **缺点**：不能处理负权边
- **应用**：路由算法、网络分析

### Floyd-Warshall算法
- **优点**：可以处理负权边，求多源最短路径
- **缺点**：时间复杂度较高
- **应用**：任意两点间最短路径

### Bellman-Ford算法
- **优点**：可以处理负权边，检测负环
- **缺点**：时间复杂度较高
- **应用**：网络路由、负环检测

## 考研重点

1. **算法选择**：根据问题特点选择合适的算法
2. **复杂度分析**：理解各算法的时间空间复杂度
3. **负权边处理**：掌握处理负权边的方法
4. **路径重建**：能够重建最短路径
5. **负环检测**：理解负环检测的原理
6. **实现细节**：掌握各种实现的细节 