# 动态规划 (Dynamic Programming)

## 算法描述

动态规划是一种通过把原问题分解为相对简单的子问题来解决复杂问题的算法设计方法。它通过存储子问题的解来避免重复计算，从而显著提高算法效率。

**核心思想**：
- **最优子结构**：问题的最优解包含其子问题的最优解
- **重叠子问题**：子问题会被重复计算
- **状态转移**：通过状态转移方程求解
- **记忆化**：存储已计算的子问题结果

## 复杂度分析

| 问题类型 | 时间复杂度 | 空间复杂度 | 优化方法 |
|----------|------------|------------|----------|
| 背包问题 | O(nW) | O(nW) | 滚动数组 |
| LCS | O(mn) | O(mn) | 滚动数组 |
| 矩阵连乘 | O(n³) | O(n²) | 难以优化 |

## 伪代码

```
// 0-1背包问题
零一背包(价值数组, 重量数组, 容量)
    n = 价值数组.长度
    动态规划表[n+1][容量+1]
    对于 i = 0 到 n
        对于 w = 0 到 容量
            如果 i == 0 或 w == 0
                动态规划表[i][w] = 0
            否则如果 重量数组[i-1] <= w
                动态规划表[i][w] = 最大值(动态规划表[i-1][w], 动态规划表[i-1][w-重量数组[i-1]] + 价值数组[i-1])
            否则
                动态规划表[i][w] = 动态规划表[i-1][w]
    返回 动态规划表[n][容量]

// 最长公共子序列
最长公共子序列(字符串1, 字符串2)
    m = 字符串1.长度, n = 字符串2.长度
    动态规划表[m+1][n+1]
    对于 i = 0 到 m
        对于 j = 0 到 n
            如果 i == 0 或 j == 0
                动态规划表[i][j] = 0
            否则如果 字符串1[i-1] == 字符串2[j-1]
                动态规划表[i][j] = 动态规划表[i-1][j-1] + 1
            否则
                动态规划表[i][j] = 最大值(动态规划表[i-1][j], 动态规划表[i][j-1])
    返回 动态规划表[m][n]
```

## C++ 实现

### 0-1背包问题

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class KnapsackProblem {
public:
    // 0-1背包问题 - 基础实现
    static int knapsack01(const std::vector<int>& values, 
                          const std::vector<int>& weights, 
                          int capacity) {
        int n = values.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(capacity + 1, 0));
        
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (weights[i - 1] <= w) {
                    dp[i][w] = std::max(dp[i - 1][w], 
                                       dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }
        
        return dp[n][capacity];
    }
    
    // 0-1背包问题 - 空间优化（滚动数组）
    static int knapsack01Optimized(const std::vector<int>& values, 
                                   const std::vector<int>& weights, 
                                   int capacity) {
        int n = values.size();
        std::vector<int> dp(capacity + 1, 0);
        
        for (int i = 0; i < n; i++) {
            for (int w = capacity; w >= weights[i]; w--) {
                dp[w] = std::max(dp[w], dp[w - weights[i]] + values[i]);
            }
        }
        
        return dp[capacity];
    }
    
    // 完全背包问题
    static int unboundedKnapsack(const std::vector<int>& values, 
                                 const std::vector<int>& weights, 
                                 int capacity) {
        int n = values.size();
        std::vector<int> dp(capacity + 1, 0);
        
        for (int w = 0; w <= capacity; w++) {
            for (int i = 0; i < n; i++) {
                if (weights[i] <= w) {
                    dp[w] = std::max(dp[w], dp[w - weights[i]] + values[i]);
                }
            }
        }
        
        return dp[capacity];
    }
    
    // 多重背包问题
    static int multipleKnapsack(const std::vector<int>& values, 
                                const std::vector<int>& weights, 
                                const std::vector<int>& counts, 
                                int capacity) {
        int n = values.size();
        std::vector<int> dp(capacity + 1, 0);
        
        for (int i = 0; i < n; i++) {
            for (int w = capacity; w >= weights[i]; w--) {
                for (int k = 1; k <= counts[i] && k * weights[i] <= w; k++) {
                    dp[w] = std::max(dp[w], dp[w - k * weights[i]] + k * values[i]);
                }
            }
        }
        
        return dp[capacity];
    }
    
    // 重建最优解
    static std::vector<int> reconstructSolution(const std::vector<int>& values, 
                                               const std::vector<int>& weights, 
                                               int capacity) {
        int n = values.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(capacity + 1, 0));
        
        // 填充DP表
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (weights[i - 1] <= w) {
                    dp[i][w] = std::max(dp[i - 1][w], 
                                       dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }
        
        // 重建解
        std::vector<int> solution;
        int w = capacity;
        for (int i = n; i > 0; i--) {
            if (dp[i][w] != dp[i - 1][w]) {
                solution.push_back(i - 1);
                w -= weights[i - 1];
            }
        }
        
        std::reverse(solution.begin(), solution.end());
        return solution;
    }
};
```

### 最长公共子序列（LCS）

```cpp
class LongestCommonSubsequence {
public:
    // 计算LCS长度
    static int lcsLength(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
    
    // 重建LCS字符串
    static std::string lcsString(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        
        // 填充DP表
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // 重建LCS
        std::string lcs;
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                lcs = str1[i - 1] + lcs;
                i--;
                j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
        
        return lcs;
    }
    
    // 空间优化的LCS
    static int lcsOptimized(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        if (m < n) {
            std::swap(str1, str2);
            std::swap(m, n);
        }
        
        std::vector<int> dp(n + 1, 0);
        
        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (str1[i - 1] == str2[j - 1]) {
                    dp[j] = prev + 1;
                } else {
                    dp[j] = std::max(dp[j], dp[j - 1]);
                }
                prev = temp;
            }
        }
        
        return dp[n];
    }
};
```

### 矩阵连乘问题

```cpp
class MatrixChainMultiplication {
public:
    // 计算最优括号化方案
    static std::pair<int, std::vector<std::vector<int>>> matrixChainOrder(
        const std::vector<int>& dimensions) {
        int n = dimensions.size() - 1;
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        std::vector<std::vector<int>> s(n, std::vector<int>(n, 0));
        
        // 对角线为0
        for (int i = 0; i < n; i++) {
            dp[i][i] = 0;
        }
        
        // 按链长度递增计算
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i][j] = std::numeric_limits<int>::max();
                
                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k + 1][j] + 
                              dimensions[i] * dimensions[k + 1] * dimensions[j + 1];
                    if (cost < dp[i][j]) {
                        dp[i][j] = cost;
                        s[i][j] = k;
                    }
                }
            }
        }
        
        return {dp[0][n - 1], s};
    }
    
    // 打印最优括号化方案
    static void printOptimalParens(const std::vector<std::vector<int>>& s, 
                                  int i, int j) {
        if (i == j) {
            std::cout << "A" << i;
        } else {
            std::cout << "(";
            printOptimalParens(s, i, s[i][j]);
            printOptimalParens(s, s[i][j] + 1, j);
            std::cout << ")";
        }
    }
    
    // 计算矩阵乘法的最小代价
    static int minMatrixMultiplicationCost(const std::vector<int>& dimensions) {
        int n = dimensions.size() - 1;
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i][j] = std::numeric_limits<int>::max();
                
                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k + 1][j] + 
                              dimensions[i] * dimensions[k + 1] * dimensions[j + 1];
                    dp[i][j] = std::min(dp[i][j], cost);
                }
            }
        }
        
        return dp[0][n - 1];
    }
};
```

### 编辑距离

```cpp
class EditDistance {
public:
    // 计算编辑距离
    static int editDistance(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        
        // 初始化第一行和第一列
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + std::min({dp[i - 1][j],      // 删除
                                            dp[i][j - 1],      // 插入
                                            dp[i - 1][j - 1]}); // 替换
                }
            }
        }
        
        return dp[m][n];
    }
    
    // 空间优化的编辑距离
    static int editDistanceOptimized(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        if (m < n) {
            std::swap(str1, str2);
            std::swap(m, n);
        }
        
        std::vector<int> dp(n + 1);
        for (int j = 0; j <= n; j++) {
            dp[j] = j;
        }
        
        for (int i = 1; i <= m; i++) {
            int prev = dp[0];
            dp[0] = i;
            
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (str1[i - 1] == str2[j - 1]) {
                    dp[j] = prev;
                } else {
                    dp[j] = 1 + std::min({dp[j], dp[j - 1], prev});
                }
                prev = temp;
            }
        }
        
        return dp[n];
    }
};
```

## 使用示例

```cpp
int main() {
    // 0-1背包问题测试
    std::vector<int> values = {60, 100, 120};
    std::vector<int> weights = {10, 20, 30};
    int capacity = 50;
    
    std::cout << "=== 0-1背包问题 ===" << std::endl;
    int maxValue = KnapsackProblem::knapsack01(values, weights, capacity);
    std::cout << "最大价值: " << maxValue << std::endl;
    
    std::vector<int> solution = KnapsackProblem::reconstructSolution(values, weights, capacity);
    std::cout << "选择的物品: ";
    for (int item : solution) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
    
    // LCS测试
    std::string str1 = "ABCDGH";
    std::string str2 = "AEDFHR";
    
    std::cout << "\n=== 最长公共子序列 ===" << std::endl;
    int lcsLength = LongestCommonSubsequence::lcsLength(str1, str2);
    std::cout << "LCS长度: " << lcsLength << std::endl;
    
    std::string lcsString = LongestCommonSubsequence::lcsString(str1, str2);
    std::cout << "LCS字符串: " << lcsString << std::endl;
    
    // 矩阵连乘测试
    std::vector<int> dimensions = {10, 30, 5, 60};
    
    std::cout << "\n=== 矩阵连乘问题 ===" << std::endl;
    auto result = MatrixChainMultiplication::matrixChainOrder(dimensions);
    std::cout << "最小乘法次数: " << result.first << std::endl;
    
    std::cout << "最优括号化方案: ";
    MatrixChainMultiplication::printOptimalParens(result.second, 0, dimensions.size() - 2);
    std::cout << std::endl;
    
    // 编辑距离测试
    std::string s1 = "kitten";
    std::string s2 = "sitting";
    
    std::cout << "\n=== 编辑距离 ===" << std::endl;
    int distance = EditDistance::editDistance(s1, s2);
    std::cout << "编辑距离: " << distance << std::endl;
    
    return 0;
}
```

## 动态规划特点

### 适用条件
1. **最优子结构**：问题的最优解包含子问题的最优解
2. **重叠子问题**：子问题会被重复计算
3. **无后效性**：当前状态只与之前状态有关

### 解题步骤
1. **定义状态**：明确dp数组的含义
2. **状态转移**：写出状态转移方程
3. **初始化**：确定边界条件
4. **计算顺序**：确定计算顺序
5. **返回结果**：返回最终答案

### 优化技巧
1. **滚动数组**：减少空间复杂度
2. **状态压缩**：使用位运算优化
3. **记忆化搜索**：自顶向下的实现
4. **单调性优化**：利用单调性优化转移

## 考研重点

1. **经典问题**：掌握背包、LCS、矩阵连乘等经典问题
2. **状态定义**：能够正确定义状态和状态转移方程
3. **空间优化**：掌握滚动数组等优化技巧
4. **边界处理**：正确处理边界条件和初始化
5. **复杂度分析**：分析时间和空间复杂度
6. **应用场景**：理解动态规划的适用场景 

# 0-1背包问题的空间优化版本解析

这个优化版本使用了"滚动数组"技术，将二维DP表压缩为一维数组，显著减少了空间复杂度（从O(n*W)降到O(W)）。

## 关键优化点

1. **一维数组替代二维表**：
   - 原始版本用`dp[i][w]`表示前i个物品在容量w时的最大价值
   - 优化版本用`dp[w]`表示当前考虑物品时容量w的最大价值

2. **逆向遍历容量**：
   - 内层循环从大到小遍历（`w = capacity downto weights[i]`）
   - 这是为了避免重复计算（确保每个物品只被考虑一次）

## 逐步执行过程

继续使用之前的例子：
- 物品：{60,10}, {100,20}, {120,30}
- 容量：50

### 初始化
`dp = [0,0,0,...,0]`（长度51）

### 处理物品1（价值60，重量10）
```
w从50到10逆向更新：
dp[50] = max(dp[50], dp[40]+60) = max(0, 0+60) = 60
dp[49] = max(dp[49], dp[39]+60) = 60
...
dp[10] = max(dp[10], dp[0]+60) = 60
```
此时`dp`数组在w≥10的位置都变为60

### 处理物品2（价值100，重量20）
```
w从50到20逆向更新：
dp[50] = max(60, dp[30]+100) = max(60, 60+100) = 160
dp[49] = max(60, dp[29]+100) = 160
...
dp[30] = max(60, dp[10]+100) = 160
dp[29] = max(60, dp[9]+100) = 60 (因为dp[9]=0)
...
dp[20] = max(60, dp[0]+100) = 100
```
关键变化：
- w≥30的位置变为160
- w=20-29的位置变为100
- w<20的位置保持60或0

### 处理物品3（价值120，重量30）
```
w从50到30逆向更新：
dp[50] = max(160, dp[20]+120) = max(160, 100+120) = 220
dp[49] = max(160, dp[19]+120) = 160
...
dp[40] = max(160, dp[10]+120) = max(160, 60+120) = 180
dp[30] = max(160, dp[0]+120) = 160
```
最终`dp[50] = 220`

## 为什么逆向遍历？

正向遍历会导致同一物品被多次计算（变成完全背包问题）。例如：
- 如果w从小到大：
  - 计算dp[20]时可能装入物品i
  - 计算dp[40]时又可能装入同一个物品i（因为dp[20]已经包含它）

逆向遍历保证了每个物品只被考虑一次，符合0-1背包的特性。



# 完全背包问题解析

完全背包问题与0-1背包问题的区别在于：**每种物品可以无限次选取**。这个解法使用了动态规划的一维数组优化。

## 关键特点

1. **物品无限供应**：每种物品可以被重复选取
2. **正向遍历容量**：与0-1背包的逆向遍历不同，这里采用正向遍历
3. **内外循环交换**：外层循环容量，内层循环物品

## 逐步执行过程

继续使用之前的例子（但允许重复选取）：
- 物品：{60,10}, {100,20}, {120,30}
- 容量：50

### 初始化
`dp = [0,0,0,...,0]`（长度51）

### 容量w从0到50逐步计算

#### w=10时：
- 物品1(10)：dp[10] = max(0, dp[0]+60) = 60
- 物品2(20)：跳过（20>10）
- 物品3(30)：跳过（30>10）
最终dp[10]=60

#### w=20时：
- 物品1(10)：dp[20] = max(0, dp[10]+60) = 120
- 物品2(20)：dp[20] = max(120, dp[0]+100) = 120
- 物品3(30)：跳过
最终dp[20]=120

#### w=30时：
- 物品1(10)：dp[30] = max(0, dp[20]+60) = 180
- 物品2(20)：dp[30] = max(180, dp[10]+100) = 180
- 物品3(30)：dp[30] = max(180, dp[0]+120) = 180
最终dp[30]=180

#### w=40时：
- 物品1(10)：dp[40] = max(0, dp[30]+60) = 240
- 物品2(20)：dp[40] = max(240, dp[20]+100) = 240
- 物品3(30)：dp[40] = max(240, dp[10]+120) = 180
最终dp[40]=240

#### w=50时：
- 物品1(10)：dp[50] = max(0, dp[40]+60) = 300
- 物品2(20)：dp[50] = max(300, dp[30]+100) = 300
- 物品3(30)：dp[50] = max(300, dp[20]+120) = 240
最终dp[50]=300

## 最优解分析

最终结果300的组成：
- 5个物品1（5×60=300，重量50）
比0-1背包的220更高，因为允许重复选取

## 为什么正向遍历？

正向遍历（从小到大）允许同一物品被多次选取：
- 计算dp[w]时，dp[w-weight[i]]可能已经包含物品i
- 这与完全背包的特性一致

## 复杂度
- 时间复杂度：O(n×capacity)
- 空间复杂度：O(capacity)