# 广度优先搜索（Breadth First Search）

## 1. 算法描述

广度优先搜索是一种用于遍历或搜索树或图的算法。它从根节点开始，逐层遍历所有相邻节点，先访问所有相邻节点，再访问下一层的节点。

### 1.1 适用场景
- 图的层次遍历
- 最短路径问题（无权图）
- 连通性检测
- 考研中图论算法的基础考点

### 1.2 复杂度分析
| 指标            | 值               |
|-----------------|------------------|
| 时间复杂度      | O(V + E)         |
| 空间复杂度      | O(V)             |
| 其中 V 为顶点数，E 为边数 |

---

## 2. 伪代码

```
BFS(graph, start):
    visited[V] = {false, false, ..., false}
    queue = empty queue
    visited[start] = true
    queue.enqueue(start)
    
    while queue is not empty:
        vertex = queue.dequeue()
        print vertex
        
        for each neighbor v of vertex:
            if not visited[v]:
                visited[v] = true
                queue.enqueue(v)
```

---

## 3. C++ 实现

```cpp
#include <vector>
#include <iostream>
#include <queue>

class Graph {
private:
    std::vector<std::vector<int>> adjList;
    int V;
    
public:
    Graph(int vertices) : V(vertices) {
        adjList.resize(V);
    }
    
    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u);  // 无向图
    }
    
    // BFS遍历
    void BFS(int start) {
        std::vector<bool> visited(V, false);
        std::queue<int> queue;
        
        std::cout << "BFS遍历结果：";
        
        visited[start] = true;
        queue.push(start);
        
        while (!queue.empty()) {
            int vertex = queue.front();
            queue.pop();
            std::cout << vertex << " ";
            
            for (int neighbor : adjList[vertex]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.push(neighbor);
                }
            }
        }
        std::cout << std::endl;
    }
    
    // 计算从起点到所有顶点的最短距离（无权图）
    std::vector<int> shortestPath(int start) {
        std::vector<int> distance(V, -1);
        std::queue<int> queue;
        
        distance[start] = 0;
        queue.push(start);
        
        while (!queue.empty()) {
            int vertex = queue.front();
            queue.pop();
            
            for (int neighbor : adjList[vertex]) {
                if (distance[neighbor] == -1) {
                    distance[neighbor] = distance[vertex] + 1;
                    queue.push(neighbor);
                }
            }
        }
        
        return distance;
    }
    
    // 检测图中是否有环（无向图）
    bool hasCycleBFS() {
        std::vector<bool> visited(V, false);
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (hasCycleBFSUtil(i, visited)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // 层次遍历（返回每层的节点）
    std::vector<std::vector<int>> levelOrderTraversal(int start) {
        std::vector<std::vector<int>> levels;
        std::vector<bool> visited(V, false);
        std::queue<int> queue;
        
        visited[start] = true;
        queue.push(start);
        
        while (!queue.empty()) {
            int levelSize = queue.size();
            std::vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                int vertex = queue.front();
                queue.pop();
                currentLevel.push_back(vertex);
                
                for (int neighbor : adjList[vertex]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        queue.push(neighbor);
                    }
                }
            }
            levels.push_back(currentLevel);
        }
        
        return levels;
    }
    
private:
    bool hasCycleBFSUtil(int start, std::vector<bool>& visited) {
        std::queue<std::pair<int, int>> queue;  // {vertex, parent}
        
        visited[start] = true;
        queue.push({start, -1});
        
        while (!queue.empty()) {
            int vertex = queue.front().first;
            int parent = queue.front().second;
            queue.pop();
            
            for (int neighbor : adjList[vertex]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.push({neighbor, vertex});
                } else if (neighbor != parent) {
                    return true;  // 找到回边
                }
            }
        }
        return false;
    }
};

// 测试函数
void TestBFS() {
    Graph g(6);
    
    // 添加边
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    g.addEdge(3, 5);
    
    std::cout << "图结构：" << std::endl;
    std::cout << "0 -- 1 -- 3 -- 5" << std::endl;
    std::cout << "|    |    |" << std::endl;
    std::cout << "2 -- 4" << std::endl;
    std::cout << std::endl;
    
    g.BFS(0);
    
    std::vector<int> distances = g.shortestPath(0);
    std::cout << "从顶点0到各顶点的最短距离：" << std::endl;
    for (int i = 0; i < distances.size(); i++) {
        if (distances[i] == -1) {
            std::cout << "顶点 " << i << ": 不可达" << std::endl;
        } else {
            std::cout << "顶点 " << i << ": " << distances[i] << std::endl;
        }
    }
    
    std::cout << "图中是否有环：" << (g.hasCycleBFS() ? "是" : "否") << std::endl;
    
    std::vector<std::vector<int>> levels = g.levelOrderTraversal(0);
    std::cout << "层次遍历结果：" << std::endl;
    for (int i = 0; i < levels.size(); i++) {
        std::cout << "第" << i << "层：";
        for (int vertex : levels[i]) {
            std::cout << vertex << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    TestBFS();
    return 0;
}
```

---

## 4. 注意事项

- **队列使用**：BFS使用队列保证先进先出的访问顺序
- **访问标记**：必须使用访问数组避免重复访问
- **层次概念**：BFS天然具有层次性，适合层次遍历
- **考研重点**：理解队列在BFS中的作用和层次遍历的概念

---

## 5. 测试用例

### 5.1 典型用例
- 输入：6个顶点的无向图
- 输出：BFS遍历序列和层次结构

### 5.2 边界用例
- 输入：单个顶点的图
- 输出：只访问该顶点
- 输入：链状图
- 输出：按层次顺序访问所有顶点

---

## 6. 常见错误与陷阱

- **忘记标记访问**：导致重复访问节点
- **队列使用错误**：使用栈而不是队列
- **层次计算错误**：在计算最短距离时层次计算错误
- **考研易错点**：不理解BFS的层次性和队列的作用

---

## 7. 变种算法

### 7.1 双向BFS（用于搜索优化）
```cpp
int bidirectionalBFS(const std::vector<std::vector<int>>& graph, int start, int target) {
    if (start == target) return 0;
    
    std::queue<int> queue1, queue2;
    std::vector<int> visited1(graph.size(), -1), visited2(graph.size(), -1);
    
    queue1.push(start);
    queue2.push(target);
    visited1[start] = 0;
    visited2[target] = 0;
    
    while (!queue1.empty() && !queue2.empty()) {
        // 从起点扩展
        int size1 = queue1.size();
        for (int i = 0; i < size1; i++) {
            int vertex = queue1.front();
            queue1.pop();
            
            for (int neighbor : graph[vertex]) {
                if (visited1[neighbor] == -1) {
                    visited1[neighbor] = visited1[vertex] + 1;
                    queue1.push(neighbor);
                    
                    if (visited2[neighbor] != -1) {
                        return visited1[neighbor] + visited2[neighbor];
                    }
                }
            }
        }
        
        // 从终点扩展
        int size2 = queue2.size();
        for (int i = 0; i < size2; i++) {
            int vertex = queue2.front();
            queue2.pop();
            
            for (int neighbor : graph[vertex]) {
                if (visited2[neighbor] == -1) {
                    visited2[neighbor] = visited2[vertex] + 1;
                    queue2.push(neighbor);
                    
                    if (visited1[neighbor] != -1) {
                        return visited1[neighbor] + visited2[neighbor];
                    }
                }
            }
        }
    }
    
    return -1;  // 不可达
}
```

### 7.2 0-1 BFS（用于边权为0或1的图）
```cpp
int zeroOneBFS(const std::vector<std::vector<std::pair<int, int>>>& graph, int start) {
    int V = graph.size();
    std::vector<int> distance(V, INT_MAX);
    std::deque<int> deque;
    
    distance[start] = 0;
    deque.push_back(start);
    
    while (!deque.empty()) {
        int vertex = deque.front();
        deque.pop_front();
        
        for (const auto& edge : graph[vertex]) {
            int neighbor = edge.first;
            int weight = edge.second;
            
            if (distance[vertex] + weight < distance[neighbor]) {
                distance[neighbor] = distance[vertex] + weight;
                
                if (weight == 0) {
                    deque.push_front(neighbor);
                } else {
                    deque.push_back(neighbor);
                }
            }
        }
    }
    
    return distance;
}
```

---

## 8. 优化技巧

- **双向BFS**：对于搜索问题，从起点和终点同时开始BFS
- **0-1 BFS**：对于边权为0或1的图，使用双端队列优化
- **层次优化**：在层次遍历中记录每层的大小

---

通过以上内容，考研学生可以全面理解广度优先搜索的原理、实现和应用，掌握队列在图遍历中的作用和层次遍历的概念。 