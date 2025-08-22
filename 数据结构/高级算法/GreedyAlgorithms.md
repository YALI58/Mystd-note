# 贪心算法 (Greedy Algorithms)

## 算法描述

贪心算法是一种在每一步选择中都采取当前状态下最好或最优的选择，从而希望导致结果是最好或最优的算法策略。贪心算法总是做出在当前看来最好的选择，不考虑全局最优解。

**核心思想**：
- **局部最优**：每一步都选择当前最优解
- **贪心选择性质**：通过局部最优选择达到全局最优
- **无后效性**：一旦做出选择，不再改变
- **简单高效**：通常实现简单，效率较高

## 复杂度分析

| 问题类型 | 时间复杂度 | 空间复杂度 | 正确性证明 |
|----------|------------|------------|------------|
| 活动选择 | O(n log n) | O(n) | 需要证明 |
| 霍夫曼编码 | O(n log n) | O(n) | 需要证明 |
| 最小生成树 | O(E log V) | O(V) | 需要证明 |
| 单源最短路径 | O(V²) | O(V) | 需要证明 |

## 伪代码

```
// 活动选择问题
活动选择器(开始时间数组, 结束时间数组)
    n = 开始时间数组.长度
    选择的活动集合 = {活动₁}
    k = 1
    对于 m = 2 到 n
        如果 开始时间数组[m] ≥ 结束时间数组[k]
            选择的活动集合 = 选择的活动集合 ∪ {活动ₘ}
            k = m
    返回 选择的活动集合

// 霍夫曼编码
霍夫曼编码(字符频率集合)
    n = |字符频率集合|
    优先队列 = 字符频率集合
    对于 i = 1 到 n - 1
        分配一个新节点 z
        z.左子节点 = x = 提取最小值(优先队列)
        z.右子节点 = y = 提取最小值(优先队列)
        z.频率 = x.频率 + y.频率
        插入(优先队列, z)
    返回 提取最小值(优先队列)
```

## C++ 实现

### 活动选择问题

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

struct Activity {
    int start;
    int finish;
    int id;
    
    Activity(int s, int f, int i) : start(s), finish(f), id(i) {}
    
    bool operator<(const Activity& other) const {
        return finish < other.finish;
    }
};

class ActivitySelection {
public:
    // 活动选择 - 按结束时间排序
    static std::vector<int> selectActivities(const std::vector<Activity>& activities) {
        std::vector<Activity> sortedActivities = activities;
        std::sort(sortedActivities.begin(), sortedActivities.end());
        
        std::vector<int> selected;
        if (sortedActivities.empty()) return selected;
        
        selected.push_back(sortedActivities[0].id);
        int lastFinish = sortedActivities[0].finish;
        
        for (size_t i = 1; i < sortedActivities.size(); i++) {
            if (sortedActivities[i].start >= lastFinish) {
                selected.push_back(sortedActivities[i].id);
                lastFinish = sortedActivities[i].finish;
            }
        }
        
        return selected;
    }
    
    // 活动选择 - 按开始时间排序（另一种贪心策略）
    static std::vector<int> selectActivitiesByStart(const std::vector<Activity>& activities) {
        std::vector<Activity> sortedActivities = activities;
        std::sort(sortedActivities.begin(), sortedActivities.end(), 
                  [](const Activity& a, const Activity& b) {
                      return a.start < b.start;
                  });
        
        std::vector<int> selected;
        if (sortedActivities.empty()) return selected;
        
        selected.push_back(sortedActivities[0].id);
        int lastFinish = sortedActivities[0].finish;
        
        for (size_t i = 1; i < sortedActivities.size(); i++) {
            if (sortedActivities[i].start >= lastFinish) {
                selected.push_back(sortedActivities[i].id);
                lastFinish = sortedActivities[i].finish;
            } else if (sortedActivities[i].finish < lastFinish) {
                // 替换为结束时间更早的活动
                selected.back() = sortedActivities[i].id;
                lastFinish = sortedActivities[i].finish;
            }
        }
        
        return selected;
    }
    
    // 打印选择的活动
    static void printSelectedActivities(const std::vector<Activity>& activities, 
                                     const std::vector<int>& selected) {
        std::cout << "选择的活动: ";
        for (int id : selected) {
            for (const Activity& activity : activities) {
                if (activity.id == id) {
                    std::cout << "(" << activity.start << "," << activity.finish << ") ";
                    break;
                }
            }
        }
        std::cout << std::endl;
    }
};
```

### 霍夫曼编码

```cpp
struct HuffmanNode {
    char data;
    int frequency;
    HuffmanNode* left;
    HuffmanNode* right;
    
    HuffmanNode(char d, int freq) : data(d), frequency(freq), left(nullptr), right(nullptr) {}
    
    bool operator>(const HuffmanNode& other) const {
        return frequency > other.frequency;
    }
};

class HuffmanCoding {
private:
    struct CompareNodes {
        bool operator()(HuffmanNode* a, HuffmanNode* b) {
            return a->frequency > b->frequency;
        }
    };
    
public:
    // 构建霍夫曼树
    static HuffmanNode* buildHuffmanTree(const std::vector<std::pair<char, int>>& frequencies) {
        std::priority_queue<HuffmanNode*, std::vector<HuffmanNode*>, CompareNodes> pq;
        
        // 创建叶子节点并加入优先队列
        for (const auto& freq : frequencies) {
            pq.push(new HuffmanNode(freq.first, freq.second));
        }
        
        // 构建霍夫曼树
        while (pq.size() > 1) {
            HuffmanNode* left = pq.top(); pq.pop();
            HuffmanNode* right = pq.top(); pq.pop();
            
            HuffmanNode* parent = new HuffmanNode('\0', left->frequency + right->frequency);
            parent->left = left;
            parent->right = right;
            
            pq.push(parent);
        }
        
        return pq.top();
    }
    
    // 生成霍夫曼编码
    static std::map<char, std::string> generateHuffmanCodes(HuffmanNode* root) {
        std::map<char, std::string> codes;
        generateCodesRecursive(root, "", codes);
        return codes;
    }
    
private:
    static void generateCodesRecursive(HuffmanNode* node, std::string code, 
                                     std::map<char, std::string>& codes) {
        if (node == nullptr) return;
        
        // 如果是叶子节点
        if (node->left == nullptr && node->right == nullptr) {
            codes[node->data] = code;
            return;
        }
        
        // 递归处理左右子树
        generateCodesRecursive(node->left, code + "0", codes);
        generateCodesRecursive(node->right, code + "1", codes);
    }
    
public:
    // 编码字符串
    static std::string encode(const std::string& text, const std::map<char, std::string>& codes) {
        std::string encoded;
        for (char c : text) {
            if (codes.find(c) != codes.end()) {
                encoded += codes.at(c);
            }
        }
        return encoded;
    }
    
    // 解码字符串
    static std::string decode(const std::string& encoded, HuffmanNode* root) {
        std::string decoded;
        HuffmanNode* current = root;
        
        for (char bit : encoded) {
            if (bit == '0') {
                current = current->left;
            } else if (bit == '1') {
                current = current->right;
            }
            
            // 到达叶子节点
            if (current->left == nullptr && current->right == nullptr) {
                decoded += current->data;
                current = root;
            }
        }
        
        return decoded;
    }
    
    // 打印霍夫曼编码
    static void printHuffmanCodes(const std::map<char, std::string>& codes) {
        std::cout << "霍夫曼编码:" << std::endl;
        for (const auto& code : codes) {
            std::cout << code.first << ": " << code.second << std::endl;
        }
    }
};
```

### 最小生成树（Prim算法）

```cpp
class PrimAlgorithm {
public:
    // Prim算法实现
    static std::vector<std::pair<int, int>> primMST(const std::vector<std::vector<int>>& graph) {
        int V = graph.size();
        std::vector<bool> visited(V, false);
        std::vector<int> key(V, std::numeric_limits<int>::max());
        std::vector<int> parent(V, -1);
        
        // 使用优先队列存储 {权重, 顶点}
        std::priority_queue<std::pair<int, int>, 
                          std::vector<std::pair<int, int>>, 
                          std::greater<std::pair<int, int>>> pq;
        
        // 从顶点0开始
        key[0] = 0;
        pq.push({0, 0});
        
        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            
            if (visited[u]) continue;
            visited[u] = true;
            
            // 遍历相邻顶点
            for (int v = 0; v < V; v++) {
                if (graph[u][v] != 0 && !visited[v] && graph[u][v] < key[v]) {
                    key[v] = graph[u][v];
                    parent[v] = u;
                    pq.push({key[v], v});
                }
            }
        }
        
        // 构建MST边集
        std::vector<std::pair<int, int>> mst;
        for (int i = 1; i < V; i++) {
            if (parent[i] != -1) {
                mst.push_back({parent[i], i});
            }
        }
        
        return mst;
    }
    
    // 计算MST总权重
    static int calculateMSTWeight(const std::vector<std::vector<int>>& graph, 
                                 const std::vector<std::pair<int, int>>& mst) {
        int totalWeight = 0;
        for (const auto& edge : mst) {
            totalWeight += graph[edge.first][edge.second];
        }
        return totalWeight;
    }
    
    // 打印MST
    static void printMST(const std::vector<std::pair<int, int>>& mst) {
        std::cout << "最小生成树的边:" << std::endl;
        for (const auto& edge : mst) {
            std::cout << edge.first << " - " << edge.second << std::endl;
        }
    }
};
```

### 任务调度问题

```cpp
struct Task {
    int id;
    int deadline;
    int profit;
    
    Task(int i, int d, int p) : id(i), deadline(d), profit(p) {}
    
    bool operator<(const Task& other) const {
        return profit > other.profit;  // 按利润降序排序
    }
};

class TaskScheduling {
public:
    // 任务调度 - 贪心算法
    static std::vector<int> scheduleTasks(const std::vector<Task>& tasks) {
        std::vector<Task> sortedTasks = tasks;
        std::sort(sortedTasks.begin(), sortedTasks.end());
        
        // 找到最大截止时间
        int maxDeadline = 0;
        for (const Task& task : sortedTasks) {
            maxDeadline = std::max(maxDeadline, task.deadline);
        }
        
        std::vector<bool> slots(maxDeadline + 1, false);
        std::vector<int> scheduledTasks;
        
        for (const Task& task : sortedTasks) {
            // 从截止时间开始向前查找可用时间槽
            for (int i = task.deadline; i > 0; i--) {
                if (!slots[i]) {
                    slots[i] = true;
                    scheduledTasks.push_back(task.id);
                    break;
                }
            }
        }
        
        return scheduledTasks;
    }
    
    // 计算总利润
    static int calculateTotalProfit(const std::vector<Task>& tasks, 
                                   const std::vector<int>& scheduledTaskIds) {
        int totalProfit = 0;
        for (int taskId : scheduledTaskIds) {
            for (const Task& task : tasks) {
                if (task.id == taskId) {
                    totalProfit += task.profit;
                    break;
                }
            }
        }
        return totalProfit;
    }
    
    // 打印调度结果
    static void printSchedule(const std::vector<Task>& tasks, 
                            const std::vector<int>& scheduledTaskIds) {
        std::cout << "调度的任务: ";
        for (int taskId : scheduledTaskIds) {
            for (const Task& task : tasks) {
                if (task.id == taskId) {
                    std::cout << "任务" << taskId << "(利润:" << task.profit << ") ";
                    break;
                }
            }
        }
        std::cout << std::endl;
    }
};
```

### 硬币找零问题

```cpp
class CoinChange {
public:
    // 硬币找零 - 贪心算法（适用于某些硬币面值）
    static std::vector<int> greedyCoinChange(int amount, const std::vector<int>& coins) {
        std::vector<int> sortedCoins = coins;
        std::sort(sortedCoins.begin(), sortedCoins.end(), std::greater<int>());
        
        std::vector<int> result;
        int remaining = amount;
        
        for (int coin : sortedCoins) {
            while (remaining >= coin) {
                result.push_back(coin);
                remaining -= coin;
            }
        }
        
        if (remaining > 0) {
            std::cout << "无法找零，剩余: " << remaining << std::endl;
            return std::vector<int>();
        }
        
        return result;
    }
    
    // 检查贪心算法是否适用
    static bool isGreedyOptimal(const std::vector<int>& coins) {
        // 对于某些硬币面值组合，贪心算法可能不是最优的
        // 这里提供一个简单的检查方法
        std::vector<int> sortedCoins = coins;
        std::sort(sortedCoins.begin(), sortedCoins.end());
        
        // 检查是否每个硬币面值都是前一个的倍数
        for (size_t i = 1; i < sortedCoins.size(); i++) {
            if (sortedCoins[i] % sortedCoins[i-1] != 0) {
                return false;
            }
        }
        return true;
    }
    
    // 打印找零结果
    static void printCoinChange(const std::vector<int>& coins) {
        std::cout << "使用的硬币: ";
        for (int coin : coins) {
            std::cout << coin << " ";
        }
        std::cout << std::endl;
        std::cout << "硬币数量: " << coins.size() << std::endl;
    }
};
```

## 使用示例

```cpp
int main() {
    // 活动选择问题测试
    std::vector<Activity> activities = {
        Activity(1, 4, 1), Activity(3, 5, 2), Activity(0, 6, 3),
        Activity(5, 7, 4), Activity(3, 8, 5), Activity(5, 9, 6),
        Activity(6, 10, 7), Activity(8, 11, 8), Activity(8, 12, 9),
        Activity(2, 13, 10), Activity(12, 14, 11)
    };
    
    std::cout << "=== 活动选择问题 ===" << std::endl;
    std::vector<int> selectedActivities = ActivitySelection::selectActivities(activities);
    ActivitySelection::printSelectedActivities(activities, selectedActivities);
    
    // 霍夫曼编码测试
    std::vector<std::pair<char, int>> frequencies = {
        {'a', 5}, {'b', 9}, {'c', 12}, {'d', 13}, {'e', 16}, {'f', 45}
    };
    
    std::cout << "\n=== 霍夫曼编码 ===" << std::endl;
    HuffmanNode* root = HuffmanCoding::buildHuffmanTree(frequencies);
    std::map<char, std::string> codes = HuffmanCoding::generateHuffmanCodes(root);
    HuffmanCoding::printHuffmanCodes(codes);
    
    std::string text = "abcde";
    std::string encoded = HuffmanCoding::encode(text, codes);
    std::string decoded = HuffmanCoding::decode(encoded, root);
    
    std::cout << "原文: " << text << std::endl;
    std::cout << "编码: " << encoded << std::endl;
    std::cout << "解码: " << decoded << std::endl;
    
    // 最小生成树测试
    std::vector<std::vector<int>> graph = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };
    
    std::cout << "\n=== Prim算法 - 最小生成树 ===" << std::endl;
    std::vector<std::pair<int, int>> mst = PrimAlgorithm::primMST(graph);
    PrimAlgorithm::printMST(mst);
    int mstWeight = PrimAlgorithm::calculateMSTWeight(graph, mst);
    std::cout << "MST总权重: " << mstWeight << std::endl;
    
    // 任务调度测试
    std::vector<Task> tasks = {
        Task(1, 2, 100), Task(2, 1, 19), Task(3, 2, 27),
        Task(4, 1, 25), Task(5, 3, 15)
    };
    
    std::cout << "\n=== 任务调度问题 ===" << std::endl;
    std::vector<int> scheduledTasks = TaskScheduling::scheduleTasks(tasks);
    TaskScheduling::printSchedule(tasks, scheduledTasks);
    int totalProfit = TaskScheduling::calculateTotalProfit(tasks, scheduledTasks);
    std::cout << "总利润: " << totalProfit << std::endl;
    
    // 硬币找零测试
    std::vector<int> coins = {25, 10, 5, 1};
    int amount = 67;
    
    std::cout << "\n=== 硬币找零问题 ===" << std::endl;
    std::vector<int> change = CoinChange::greedyCoinChange(amount, coins);
    CoinChange::printCoinChange(change);
    
    return 0;
}
```

## 贪心算法特点

### 适用条件
1. **贪心选择性质**：局部最优选择导致全局最优解
2. **最优子结构**：问题的最优解包含子问题的最优解
3. **无后效性**：当前决策不影响之前的状态

### 解题步骤
1. **问题分析**：确定问题的贪心策略
2. **正确性证明**：证明贪心策略的正确性
3. **算法设计**：设计贪心算法
4. **复杂度分析**：分析时间和空间复杂度

### 常见问题
1. **活动选择**：按结束时间排序
2. **霍夫曼编码**：构建最优前缀码
3. **最小生成树**：Prim和Kruskal算法
4. **单源最短路径**：Dijkstra算法
5. **任务调度**：按利润或截止时间排序

## 考研重点

1. **贪心策略**：理解各种问题的贪心策略
2. **正确性证明**：能够证明贪心算法的正确性
3. **算法实现**：掌握经典贪心算法的实现
4. **复杂度分析**：分析贪心算法的时间空间复杂度
5. **应用场景**：理解贪心算法的适用场景
6. **局限性**：了解贪心算法的局限性 