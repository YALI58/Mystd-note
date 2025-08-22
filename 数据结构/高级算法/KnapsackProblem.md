# 背包问题（Knapsack Problem）

## 1. 算法描述

背包问题是动态规划中的经典问题。给定一组物品，每个物品有重量和价值，在不超过背包容量限制的前提下，选择物品使得总价值最大。

### 1.1 适用场景
- 资源分配问题
- 考研中动态规划的重要考点
- 优化问题中的经典案例

### 1.2 复杂度分析
| 指标            | 值               |
|-----------------|------------------|
| 时间复杂度      | O(n*W)           |
| 空间复杂度      | O(n*W)           |
| 其中 n 为物品数量，W 为背包容量 |

---

## 2. 伪代码

```
背包问题(重量数组, 价值数组, 物品数量, 容量):
    // 创建二维DP表
    动态规划表[物品数量+1][容量+1]
    
    // 初始化第一行和第一列为0
    对于 i = 0 到 物品数量:
        动态规划表[i][0] = 0
    对于 j = 0 到 容量:
        动态规划表[0][j] = 0
    
    // 填充DP表
    对于 i = 1 到 物品数量:
        对于 j = 1 到 容量:
            如果 重量数组[i-1] <= j:
                动态规划表[i][j] = 最大值(动态规划表[i-1][j], 动态规划表[i-1][j-重量数组[i-1]] + 价值数组[i-1])
            否则:
                动态规划表[i][j] = 动态规划表[i-1][j]
    
    返回 动态规划表[物品数量][容量]
```

---

## 3. C++ 实现

```cpp
#include <vector>
#include <iostream>
#include <algorithm>

// 0-1背包问题求解
int Knapsack(const std::vector<int>& weights, const std::vector<int>& values, int W) {
    int n = weights.size();
    
    // 创建二维DP表
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(W + 1, 0));
    
    // 填充DP表
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= W; j++) {
            if (weights[i-1] <= j) {
                // 可以选择放入或不放入第i个物品
                dp[i][j] = std::max(dp[i-1][j], 
                                   dp[i-1][j-weights[i-1]] + values[i-1]);
            } else {
                // 第i个物品太重，不能放入
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    
    return dp[n][W];
}

// 空间优化版本（使用一维数组）
int KnapsackOptimized(const std::vector<int>& weights, const std::vector<int>& values, int W) {
    int n = weights.size();
    std::vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < n; i++) {
        // 从后往前遍历，避免重复使用物品
        for (int j = W; j >= weights[i]; j--) {
            dp[j] = std::max(dp[j], dp[j - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}

// 测试函数
void TestKnapsack() {
    std::vector<int> weights = {2, 1, 3, 2};
    std::vector<int> values = {12, 10, 20, 15};
    int W = 5;
    
    std::cout << "物品重量：";
    for (int w : weights) {
        std::cout << w << " ";
    }
    std::cout << std::endl;
    
    std::cout << "物品价值：";
    for (int v : values) {
        std::cout << v << " ";
    }
    std::cout << std::endl;
    
    std::cout << "背包容量：" << W << std::endl;
    
    int result = Knapsack(weights, values, W);
    std::cout << "最大价值（二维DP）：" << result << std::endl;
    
    int result2 = KnapsackOptimized(weights, values, W);
    std::cout << "最大价值（一维DP）：" << result2 << std::endl;
}

int main() {
    TestKnapsack();
    return 0;
}
```

---

## 4. 注意事项

- **状态定义**：`dp[i][j]` 表示前i个物品在容量j下的最大价值
- **状态转移**：对于每个物品，可以选择放入或不放入
- **边界条件**：容量为0时价值为0，没有物品时价值为0
- **考研重点**：理解动态规划的状态转移方程和边界条件

---

## 5. 测试用例

### 5.1 典型用例
- 输入：weights = {2, 1, 3, 2}, values = {12, 10, 20, 15}, W = 5
- 输出：37

### 5.2 边界用例
- 输入：weights = {1}, values = {10}, W = 1
- 输出：10
- 输入：weights = {5}, values = {10}, W = 3
- 输出：0

---

## 6. 常见错误与陷阱

- **状态转移错误**：不理解为什么从后往前遍历可以避免重复使用物品
- **边界条件遗漏**：忘记初始化第一行和第一列
- **数组越界**：访问 `dp[i-1][j-weights[i-1]]` 时没有检查索引是否有效
- **考研易错点**：不理解动态规划的核心思想和状态定义

---

## 7. 变种算法

### 7.1 完全背包问题（物品可以重复使用）
```cpp
int CompleteKnapsack(const std::vector<int>& weights, const std::vector<int>& values, int W) {
    int n = weights.size();
    std::vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < n; i++) {
        // 从前往后遍历，允许重复使用物品
        for (int j = weights[i]; j <= W; j++) {
            dp[j] = std::max(dp[j], dp[j - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}
```

### 7.2 多重背包问题（每种物品有数量限制）
```cpp
int MultipleKnapsack(const std::vector<int>& weights, const std::vector<int>& values, 
                     const std::vector<int>& counts, int W) {
    int n = weights.size();
    std::vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < n; i++) {
        for (int j = W; j >= weights[i]; j--) {
            for (int k = 1; k <= counts[i] && k * weights[i] <= j; k++) {
                dp[j] = std::max(dp[j], dp[j - k * weights[i]] + k * values[i]);
            }
        }
    }
    
    return dp[W];
}
```

---

## 8. 优化技巧

- **空间优化**：使用一维数组代替二维数组
- **剪枝优化**：对于价值密度低的物品可以提前排除
- **记忆化搜索**：使用递归+记忆化的方式实现

---

通过以上内容，考研学生可以全面理解背包问题的原理、实现和变种算法，掌握动态规划在优化问题中的应用。 