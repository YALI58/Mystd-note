# 深度优先搜索（Depth First Search）

## 1. 算法描述

深度优先搜索是一种用于遍历或搜索树或图的算法。它沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都已被探寻过，搜索将回溯到发现节点v的那条边的起始节点。

### 1.1 适用场景
- 图的遍历和连通性检测
- 拓扑排序
- 强连通分量查找
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
深度优先搜索(图, 起始点):
    已访问[顶点数] = {假, 假, ..., 假}
    深度优先搜索递归(图, 起始点, 已访问)

深度优先搜索递归(图, 顶点, 已访问):
    已访问[顶点] = 真
    输出 顶点
    
    对于 每个邻居 v 属于 顶点:
        如果 未访问[v]:
            深度优先搜索递归(图, v, 已访问)
```

---

## 3. C++ 实现

```cpp
#include <vector>
#include <iostream>
#include <stack>

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
    
    // 递归实现DFS
    void DFSRecursive(int start) {
        std::vector<bool> visited(V, false);
        std::cout << "DFS遍历结果（递归）：";
        DFSRecursiveUtil(start, visited);
        std::cout << std::endl;
    }
    
    // 迭代实现DFS
    void DFSIterative(int start) {
        std::vector<bool> visited(V, false);
        std::stack<int> stack;
        
        std::cout << "DFS遍历结果（迭代）：";
        
        stack.push(start);
        visited[start] = true;
        
        while (!stack.empty()) {
            int vertex = stack.top();
            stack.pop();
            std::cout << vertex << " ";
            
            for (int neighbor : adjList[vertex]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    stack.push(neighbor);
                }
            }
        }
        std::cout << std::endl;
    }
    
    // 连通分量计数
    int countConnectedComponents() {
        std::vector<bool> visited(V, false);
        int count = 0;
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                DFSRecursiveUtil(i, visited);
                count++;
            }
        }
        
        return count;
    }
    
    // 检测图中是否有环（无向图）
    bool hasCycle() {
        std::vector<bool> visited(V, false);
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (hasCycleUtil(i, visited, -1)) {
                    return true;
                }
            }
        }
        return false;
    }
    
private:
    void DFSRecursiveUtil(int vertex, std::vector<bool>& visited) {
        visited[vertex] = true;
        std::cout << vertex << " ";
        
        for (int neighbor : adjList[vertex]) {
            if (!visited[neighbor]) {
                DFSRecursiveUtil(neighbor, visited);
            }
        }
    }
    
    bool hasCycleUtil(int vertex, std::vector<bool>& visited, int parent) {
        visited[vertex] = true;
        
        for (int neighbor : adjList[vertex]) {
            if (!visited[neighbor]) {
                if (hasCycleUtil(neighbor, visited, vertex)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true;  // 找到回边
            }
        }
        return false;
    }
};

// 测试函数
void TestDFS() {
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
    
    g.DFSRecursive(0);
    g.DFSIterative(0);
    
    std::cout << "连通分量数量：" << g.countConnectedComponents() << std::endl;
    std::cout << "图中是否有环：" << (g.hasCycle() ? "是" : "否") << std::endl;
}

int main() {
    TestDFS();
    return 0;
}
```

---

## 4. 注意事项

- **访问标记**：必须使用访问数组避免重复访问
- **递归深度**：对于深度很大的图，递归可能导致栈溢出
- **遍历顺序**：DFS的遍历顺序取决于邻接表的存储顺序
- **考研重点**：理解递归思想和回溯机制

---

## 5. 测试用例

### 5.1 典型用例
- 输入：6个顶点的无向图
- 输出：DFS遍历序列

### 5.2 边界用例
- 输入：单个顶点的图
- 输出：只访问该顶点
- 输入：不连通的图
- 输出：需要多次调用DFS访问所有连通分量

---

## 6. 常见错误与陷阱

- **忘记标记访问**：导致无限递归
- **递归栈溢出**：对于深度很大的图
- **遍历不完整**：对于不连通图，只访问了一个连通分量
- **考研易错点**：不理解递归的调用栈和回溯过程

---

## 7. 变种算法

### 7.1 拓扑排序（有向无环图）
```cpp
std::vector<int> topologicalSort(const std::vector<std::vector<int>>& graph) {
    int V = graph.size();
    std::vector<bool> visited(V, false);
    std::vector<int> result;
    
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topologicalSortUtil(graph, i, visited, result);
        }
    }
    
    std::reverse(result.begin(), result.end());
    return result;
}

void topologicalSortUtil(const std::vector<std::vector<int>>& graph, 
                        int vertex, std::vector<bool>& visited, 
                        std::vector<int>& result) {
    visited[vertex] = true;
    
    for (int neighbor : graph[vertex]) {
        if (!visited[neighbor]) {
            topologicalSortUtil(graph, neighbor, visited, result);
        }
    }
    
    result.push_back(vertex);
}
```

### 7.2 强连通分量（Tarjan算法）
```cpp
void tarjanSCC(const std::vector<std::vector<int>>& graph) {
    int V = graph.size();
    std::vector<int> disc(V, -1);
    std::vector<int> low(V, -1);
    std::vector<bool> inStack(V, false);
    std::stack<int> stack;
    int time = 0;
    
    for (int i = 0; i < V; i++) {
        if (disc[i] == -1) {
            tarjanUtil(graph, i, disc, low, inStack, stack, time);
        }
    }
}

void tarjanUtil(const std::vector<std::vector<int>>& graph, int u,
                std::vector<int>& disc, std::vector<int>& low,
                std::vector<bool>& inStack, std::stack<int>& stack, int& time) {
    disc[u] = low[u] = ++time;
    stack.push(u);
    inStack[u] = true;
    
    for (int v : graph[u]) {
        if (disc[v] == -1) {
            tarjanUtil(graph, v, disc, low, inStack, stack, time);
            low[u] = std::min(low[u], low[v]);
        } else if (inStack[v]) {
            low[u] = std::min(low[u], disc[v]);
        }
    }
    
    if (low[u] == disc[u]) {
        std::cout << "强连通分量：";
        while (stack.top() != u) {
            int v = stack.top();
            stack.pop();
            inStack[v] = false;
            std::cout << v << " ";
        }
        int v = stack.top();
        stack.pop();
        inStack[v] = false;
        std::cout << v << std::endl;
    }
}
```

---

## 8. 优化技巧

- **迭代实现**：对于深度很大的图，使用栈的迭代实现避免栈溢出
- **访问优化**：在邻接表中按特定顺序存储邻居，影响遍历顺序
- **并行DFS**：对于大型图，可以使用并行算法加速遍历

---

通过以上内容，考研学生可以全面理解深度优先搜索的原理、实现和应用，掌握递归思想和图遍历的基本方法。 