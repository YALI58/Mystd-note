# 并查集 - 路径压缩优化

## 算法描述

并查集（Disjoint Set Union，DSU）是一种树形的数据结构，用于处理一些不相交集合的合并及查询问题。并查集支持两种主要操作：查找（Find）和合并（Union）。

### 核心思想

1. **森林结构**：每个集合用一棵树表示，根节点作为集合的代表
2. **路径压缩**：在查找过程中，将查找路径上的所有节点直接连接到根节点
3. **按秩合并**：合并时总是将较小的树连接到较大的树的根节点下

## 复杂度分析

- **时间复杂度**：
  - 单次操作：O(α(n))（阿克曼函数的反函数，接近常数）
  - 总体：O(nα(n))
- **空间复杂度**：O(n) - 存储父节点数组和秩数组

## 伪代码

```
// 初始化并查集
函数 创建集合(n):
    对于 i = 0 到 n-1:
        父节点[i] = i
        秩[i] = 0

// 查找操作（带路径压缩）
函数 查找(x):
    如果 父节点[x] != x:
        父节点[x] = 查找(父节点[x])  // 路径压缩
    返回 父节点[x]

// 合并操作（按秩合并）
函数 合并(x, y):
    根节点X = 查找(x)
    根节点Y = 查找(y)
    如果 根节点X == 根节点Y:
        返回  // 已在同一集合
    
    如果 秩[根节点X] < 秩[根节点Y]:
        父节点[根节点X] = 根节点Y
    否则如果 秩[根节点X] > 秩[根节点Y]:
        父节点[根节点Y] = 根节点X
    否则:
        父节点[根节点Y] = 根节点X
        秩[根节点X]++
```

## C++实现

### 基础实现

```cpp
#include <iostream>
#include <vector>

class DisjointSetUnion {
private:
    std::vector<int> parent;  // 父节点数组
    std::vector<int> rank;    // 秩数组
    int count;                // 集合数量

public:
    // 构造函数
    DisjointSetUnion(int n) : count(n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;  // 初始时每个元素都是自己的根
        }
    }
    
    // 查找操作（带路径压缩）
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // 路径压缩
        }
        return parent[x];
    }
    
    // 合并操作（按秩合并）
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX == rootY) {
            return;  // 已在同一集合
        }
        
        // 按秩合并
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        
        count--;  // 集合数量减少
    }
    
    // 检查两个元素是否在同一集合
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
    
    // 获取集合数量
    int getCount() const {
        return count;
    }
    
    // 获取元素x所在集合的大小
    int getSize(int x) {
        int root = find(x);
        int size = 0;
        for (int i = 0; i < parent.size(); i++) {
            if (find(i) == root) {
                size++;
            }
        }
        return size;
    }
};
```

### 优化实现（带集合大小统计）

```cpp
class OptimizedDSU {
private:
    std::vector<int> parent;
    std::vector<int> rank;
    std::vector<int> size;  // 每个集合的大小
    int count;

public:
    OptimizedDSU(int n) : count(n) {
        parent.resize(n);
        rank.resize(n, 0);
        size.resize(n, 1);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX == rootY) {
            return;
        }
        
        // 按秩合并，同时更新集合大小
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
        } else {
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
            rank[rootX]++;
        }
        
        count--;
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
    
    int getCount() const {
        return count;
    }
    
    // O(1)时间复杂度获取集合大小
    int getSize(int x) {
        return size[find(x)];
    }
};
```

### 带权并查集实现

```cpp
class WeightedDSU {
private:
    std::vector<int> parent;
    std::vector<int> rank;
    std::vector<int> weight;  // 到父节点的权重

public:
    WeightedDSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        weight.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            int oldParent = parent[x];
            parent[x] = find(parent[x]);
            weight[x] += weight[oldParent];  // 更新权重
        }
        return parent[x];
    }
    
    // 合并操作，weight表示x到y的权重
    void unite(int x, int y, int w) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX == rootY) {
            return;
        }
        
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
            weight[rootX] = w - weight[x] + weight[y];
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
            weight[rootY] = -w + weight[x] - weight[y];
        } else {
            parent[rootY] = rootX;
            weight[rootY] = -w + weight[x] - weight[y];
            rank[rootX]++;
        }
    }
    
    // 获取x到y的权重差
    int getWeight(int x, int y) {
        if (find(x) != find(y)) {
            return -1;  // 不在同一集合
        }
        return weight[x] - weight[y];
    }
};
```

## 使用示例

```cpp
int main() {
    // 基础并查集
    DisjointSetUnion dsu(10);
    
    // 合并操作
    dsu.unite(1, 2);
    dsu.unite(2, 3);
    dsu.unite(4, 5);
    dsu.unite(5, 6);
    
    // 查询操作
    std::cout << "1和3是否连通: " << (dsu.connected(1, 3) ? "是" : "否") << std::endl;
    std::cout << "1和4是否连通: " << (dsu.connected(1, 4) ? "是" : "否") << std::endl;
    std::cout << "集合数量: " << dsu.getCount() << std::endl;
    
    // 优化并查集
    OptimizedDSU odsu(10);
    odsu.unite(1, 2);
    odsu.unite(2, 3);
    std::cout << "集合1的大小: " << odsu.getSize(1) << std::endl;
    
    // 带权并查集
    WeightedDSU wdsu(10);
    wdsu.unite(1, 2, 5);  // 1到2的权重为5
    wdsu.unite(2, 3, 3);  // 2到3的权重为3
    std::cout << "1到3的权重差: " << wdsu.getWeight(1, 3) << std::endl;
    
    return 0;
}
```

## 算法特点

### 优点
- **高效性**：经过优化的并查集操作接近常数时间复杂度
- **简单性**：实现相对简单，易于理解
- **灵活性**：支持动态合并和查询操作
- **可扩展性**：可以添加权重、大小等额外信息

### 缺点
- **单向性**：不支持分离操作（只能合并，不能分离）
- **信息有限**：只能知道连通性，无法获取具体路径
- **内存开销**：需要额外的数组存储父节点和秩信息

## 测试用例

### 典型测试用例

```cpp
void testDSU() {
    // 测试用例1：基本操作
    DisjointSetUnion dsu(5);
    dsu.unite(0, 1);
    dsu.unite(1, 2);
    dsu.unite(3, 4);
    
    assert(dsu.connected(0, 2));
    assert(dsu.connected(3, 4));
    assert(!dsu.connected(0, 3));
    assert(dsu.getCount() == 2);
    
    // 测试用例2：路径压缩
    OptimizedDSU odsu(10);
    for (int i = 1; i < 10; i++) {
        odsu.unite(i-1, i);
    }
    assert(odsu.connected(0, 9));
    assert(odsu.getSize(0) == 10);
    
    // 测试用例3：带权并查集
    WeightedDSU wdsu(5);
    wdsu.unite(0, 1, 2);
    wdsu.unite(1, 2, 3);
    assert(wdsu.getWeight(0, 2) == 5);
    
    std::cout << "所有测试用例通过！" << std::endl;
}
```

### 边界测试用例

```cpp
void testEdgeCases() {
    // 单元素集合
    DisjointSetUnion dsu(1);
    assert(dsu.getCount() == 1);
    assert(dsu.connected(0, 0));
    
    // 空并查集
    DisjointSetUnion dsu2(0);
    assert(dsu2.getCount() == 0);
    
    // 重复合并
    DisjointSetUnion dsu3(3);
    dsu3.unite(0, 1);
    dsu3.unite(0, 1);  // 重复合并
    assert(dsu3.getCount() == 2);
}
```

## 常见错误

### 1. 路径压缩实现错误
```cpp
// 错误：没有正确实现路径压缩
int find(int x) {
    if (parent[x] != x) {
        return find(parent[x]);  // 错误：没有更新parent[x]
    }
    return x;
}
```

### 2. 按秩合并错误
```cpp
// 错误：没有按秩合并
void unite(int x, int y) {
    int rootX = find(x);
    int rootY = find(y);
    if (rootX != rootY) {
        parent[rootX] = rootY;  // 错误：没有考虑秩
    }
}
```

### 3. 初始化错误
```cpp
// 错误：没有正确初始化
DisjointSetUnion(int n) {
    parent.resize(n);
    // 缺少rank数组初始化和parent数组初始化
}
```

## 算法变种

### 1. 可持久化并查集
```cpp
class PersistentDSU {
private:
    std::vector<std::vector<int>> parentHistory;
    std::vector<std::vector<int>> rankHistory;
    
public:
    void unite(int x, int y) {
        // 保存当前状态
        parentHistory.push_back(parent);
        rankHistory.push_back(rank);
        
        // 执行合并操作
        // ...
    }
    
    void rollback() {
        if (!parentHistory.empty()) {
            parent = parentHistory.back();
            rank = rankHistory.back();
            parentHistory.pop_back();
            rankHistory.pop_back();
        }
    }
};
```

### 2. 在线并查集
```cpp
class OnlineDSU {
private:
    std::vector<int> parent;
    std::vector<int> rank;
    std::vector<std::pair<int, int>> operations;
    
public:
    void unite(int x, int y) {
        operations.push_back({x, y});
        // 执行合并操作
    }
    
    void undo() {
        if (!operations.empty()) {
            // 撤销最后一次操作
            operations.pop_back();
            // 重新构建并查集
        }
    }
};
```

## 优化技巧

### 1. 内存优化
```cpp
// 使用更紧凑的数据结构
class CompactDSU {
private:
    static const int MAX_N = 100000;
    int parent[MAX_N];
    char rank[MAX_N];  // 使用char节省内存
    
public:
    CompactDSU(int n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }
};
```

### 2. 并行化优化
```cpp
// 支持并行操作的并查集
class ParallelDSU {
private:
    std::vector<int> parent;
    std::vector<int> rank;
    std::mutex mtx;
    
public:
    int find(int x) {
        std::lock_guard<std::mutex> lock(mtx);
        // 线程安全的查找操作
    }
    
    void unite(int x, int y) {
        std::lock_guard<std::mutex> lock(mtx);
        // 线程安全的合并操作
    }
};
```

### 3. 缓存优化
```cpp
// 使用缓存友好的数据结构
class CacheFriendlyDSU {
private:
    std::vector<std::pair<int, int>> data;  // {parent, rank}
    
public:
    CacheFriendlyDSU(int n) : data(n) {
        for (int i = 0; i < n; i++) {
            data[i] = {i, 0};
        }
    }
    
    int find(int x) {
        if (data[x].first != x) {
            data[x].first = find(data[x].first);
        }
        return data[x].first;
    }
};
```

## 应用场景

### 1. 图论算法
- **最小生成树**：Kruskal算法
- **连通分量**：计算无向图的连通分量
- **网络连接**：判断网络中的节点是否连通

### 2. 图像处理
- **连通区域标记**：图像分割算法
- **像素聚类**：相似像素的合并
- **边界检测**：连通区域的边界识别

### 3. 社交网络
- **好友关系**：判断两个用户是否在同一个社交圈
- **群组管理**：动态合并和查询群组
- **推荐系统**：基于连通性的推荐算法

### 4. 数据库系统
- **事务管理**：合并和查询事务集合
- **数据分区**：动态调整数据分区
- **索引优化**：维护索引的连通性

## 考研重点

### 1. 路径压缩优化
- 理解路径压缩的原理
- 掌握实现方法
- 分析时间复杂度

### 2. 按秩合并
- 理解按秩合并的必要性
- 掌握实现细节
- 分析优化效果

### 3. 时间复杂度分析
- 阿克曼函数及其反函数
- 均摊分析
- 最坏情况分析

### 4. 实际应用
- 最小生成树算法
- 连通性问题
- 动态图问题

## 总结

并查集是一种高效的数据结构，通过路径压缩和按秩合并优化，使得操作接近常数时间复杂度。在考研中，重点掌握路径压缩的实现和按秩合并的原理，以及在实际问题中的应用。 