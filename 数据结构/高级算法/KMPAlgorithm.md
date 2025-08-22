# KMP算法 - 字符串匹配

## 算法描述

KMP（Knuth-Morris-Pratt）算法是一种高效的字符串匹配算法，用于在一个文本串中查找模式串的位置。KMP算法的核心思想是利用已经部分匹配的结果，避免重复比较已经匹配过的字符。

### 核心思想

1. **预处理模式串**：计算模式串的next数组（也称为失配函数）
2. **利用next数组**：当匹配失败时，利用next数组快速移动模式串，避免重复比较
3. **线性时间复杂度**：预处理O(m)，匹配O(n)，总体O(n+m)

## 复杂度分析

- **时间复杂度**：O(n + m)
  - 预处理模式串：O(m)
  - 匹配过程：O(n)
- **空间复杂度**：O(m) - 存储next数组

## 伪代码

```
// 计算next数组
函数 计算Next数组(模式串):
    next[0] = -1
    i = 0, j = -1
    当 i < 模式串.长度 - 1:
        如果 j == -1 或 模式串[i] == 模式串[j]:
            i++
            j++
            next[i] = j
        否则:
            j = next[j]

// KMP匹配算法
函数 KMP匹配(文本, 模式串):
    next = 计算Next数组(模式串)
    i = 0, j = 0
    当 i < 文本.长度 且 j < 模式串.长度:
        如果 j == -1 或 文本[i] == 模式串[j]:
            i++
            j++
        否则:
            j = next[j]
    
    如果 j == 模式串.长度:
        返回 i - j  // 找到匹配
    否则:
        返回 -1     // 未找到匹配
```

## C++实现

### 基础实现

```cpp
#include <iostream>
#include <vector>
#include <string>

class KMPAlgorithm {
public:
    // 计算next数组
    static std::vector<int> computeNext(const std::string& pattern) {
        int m = pattern.length();
        std::vector<int> next(m);
        next[0] = -1;
        
        int i = 0, j = -1;
        while (i < m - 1) {
            if (j == -1 || pattern[i] == pattern[j]) {
                i++;
                j++;
                next[i] = j;
            } else {
                j = next[j];
            }
        }
        
        return next;
    }
    
    // KMP匹配算法
    static int search(const std::string& text, const std::string& pattern) {
        if (pattern.empty()) return 0;
        if (text.empty()) return -1;
        
        int n = text.length();
        int m = pattern.length();
        
        std::vector<int> next = computeNext(pattern);
        
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (j == -1 || text[i] == pattern[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
        }
        
        if (j == m) {
            return i - j;  // 找到匹配
        } else {
            return -1;     // 未找到匹配
        }
    }
    
    // 查找所有匹配位置
    static std::vector<int> findAll(const std::string& text, const std::string& pattern) {
        std::vector<int> positions;
        if (pattern.empty()) return positions;
        
        int n = text.length();
        int m = pattern.length();
        
        std::vector<int> next = computeNext(pattern);
        
        int i = 0, j = 0;
        while (i < n) {
            if (j == -1 || text[i] == pattern[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
            
            if (j == m) {
                positions.push_back(i - j);
                j = next[j - 1];  // 继续查找下一个匹配
            }
        }
        
        return positions;
    }
};
```

### 优化实现（改进的next数组）

```cpp
class OptimizedKMP {
public:
    // 优化的next数组计算
    static std::vector<int> computeNextOptimized(const std::string& pattern) {
        int m = pattern.length();
        std::vector<int> next(m);
        next[0] = -1;
        
        int i = 0, j = -1;
        while (i < m - 1) {
            if (j == -1 || pattern[i] == pattern[j]) {
                i++;
                j++;
                // 优化：如果当前字符与前缀字符相同，则继续回退
                if (pattern[i] != pattern[j]) {
                    next[i] = j;
                } else {
                    next[i] = next[j];
                }
            } else {
                j = next[j];
            }
        }
        
        return next;
    }
    
    // 优化的KMP匹配
    static int searchOptimized(const std::string& text, const std::string& pattern) {
        if (pattern.empty()) return 0;
        if (text.empty()) return -1;
        
        int n = text.length();
        int m = pattern.length();
        
        std::vector<int> next = computeNextOptimized(pattern);
        
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (j == -1 || text[i] == pattern[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
        }
        
        return (j == m) ? i - j : -1;
    }
};
```

## 使用示例

```cpp
int main() {
    std::string text = "ABABCABCABAB";
    std::string pattern = "ABCAB";
    
    // 基础KMP
    int pos = KMPAlgorithm::search(text, pattern);
    if (pos != -1) {
        std::cout << "找到匹配，位置：" << pos << std::endl;
    } else {
        std::cout << "未找到匹配" << std::endl;
    }
    
    // 查找所有匹配
    std::vector<int> positions = KMPAlgorithm::findAll(text, pattern);
    std::cout << "所有匹配位置：";
    for (int pos : positions) {
        std::cout << pos << " ";
    }
    std::cout << std::endl;
    
    // 优化KMP
    int pos2 = OptimizedKMP::searchOptimized(text, pattern);
    std::cout << "优化KMP结果：" << pos2 << std::endl;
    
    return 0;
}
```

## 算法特点

### 优点
- **高效性**：时间复杂度O(n+m)，比暴力匹配O(nm)更优
- **预处理**：next数组只需计算一次，可重复使用
- **线性时间**：匹配过程是线性的，不会退化

### 缺点
- **预处理开销**：需要O(m)时间和空间计算next数组
- **理解复杂**：next数组的概念相对复杂
- **实现细节**：边界条件处理需要特别注意

## 测试用例

### 典型测试用例

```cpp
void testKMP() {
    // 测试用例1：基本匹配
    std::string text1 = "ABABCABCABAB";
    std::string pattern1 = "ABCAB";
    assert(KMPAlgorithm::search(text1, pattern1) == 2);
    
    // 测试用例2：多个匹配
    std::string text2 = "AABAACAADAABAABA";
    std::string pattern2 = "AABA";
    auto positions = KMPAlgorithm::findAll(text2, pattern2);
    assert(positions.size() == 3);
    
    // 测试用例3：无匹配
    std::string text3 = "ABCDEF";
    std::string pattern3 = "XYZ";
    assert(KMPAlgorithm::search(text3, pattern3) == -1);
    
    // 测试用例4：空字符串
    assert(KMPAlgorithm::search("", "ABC") == -1);
    assert(KMPAlgorithm::search("ABC", "") == 0);
    
    std::cout << "所有测试用例通过！" << std::endl;
}
```

### 边界测试用例

```cpp
void testEdgeCases() {
    // 单字符匹配
    assert(KMPAlgorithm::search("A", "A") == 0);
    
    // 相同字符串
    assert(KMPAlgorithm::search("ABC", "ABC") == 0);
    
    // 模式串比文本串长
    assert(KMPAlgorithm::search("AB", "ABC") == -1);
    
    // 重复字符
    std::string text = "AAAAA";
    std::string pattern = "AAA";
    auto positions = KMPAlgorithm::findAll(text, pattern);
    assert(positions.size() == 3);
}
```

## 常见错误

### 1. next数组计算错误
```cpp
// 错误：没有正确处理j == -1的情况
while (i < m - 1) {
    if (pattern[i] == pattern[j]) {  // 缺少j == -1的判断
        i++;
        j++;
        next[i] = j;
    } else {
        j = next[j];
    }
}
```

### 2. 边界条件处理错误
```cpp
// 错误：没有检查空字符串
static int search(const std::string& text, const std::string& pattern) {
    // 缺少空字符串检查
    int n = text.length();
    int m = pattern.length();
    // ...
}
```

### 3. 匹配位置计算错误
```cpp
// 错误：匹配位置计算
if (j == m) {
    return i;  // 错误：应该是i - j
}
```

## 算法变种

### 1. Boyer-Moore算法
```cpp
// Boyer-Moore算法的简化版本
class BoyerMoore {
public:
    static int search(const std::string& text, const std::string& pattern) {
        // 实现Boyer-Moore算法
        // 从右到左比较，利用坏字符规则和好后缀规则
    }
};
```

### 2. Sunday算法
```cpp
// Sunday算法的简化版本
class Sunday {
public:
    static int search(const std::string& text, const std::string& pattern) {
        // 实现Sunday算法
        // 利用文本串中模式串右边界下一个字符的信息
    }
};
```

## 优化技巧

### 1. next数组优化
```cpp
// 优化next数组计算，减少不必要的比较
if (pattern[i] != pattern[j]) {
    next[i] = j;
} else {
    next[i] = next[j];  // 避免重复比较
}
```

### 2. 内存优化
```cpp
// 使用更紧凑的数据结构
class CompactKMP {
private:
    static const int MAX_PATTERN_LEN = 1000;
    int next[MAX_PATTERN_LEN];
    
public:
    int search(const std::string& text, const std::string& pattern) {
        // 使用固定大小数组，避免动态内存分配
    }
};
```

### 3. 并行化优化
```cpp
// 多模式串并行匹配
class ParallelKMP {
public:
    static std::vector<int> searchMultiple(
        const std::string& text, 
        const std::vector<std::string>& patterns) {
        // 并行处理多个模式串
    }
};
```

## 应用场景

### 1. 文本编辑器
- 查找和替换功能
- 语法高亮
- 代码搜索

### 2. 生物信息学
- DNA序列匹配
- 蛋白质序列分析
- 基因识别

### 3. 网络安全
- 入侵检测
- 病毒特征匹配
- 网络流量分析

### 4. 数据压缩
- LZ77/LZ78算法
- 重复模式识别
- 数据去重

## 考研重点

### 1. next数组计算
- 理解next数组的含义
- 掌握计算过程
- 能够手动计算简单例子

### 2. 时间复杂度分析
- 预处理阶段：O(m)
- 匹配阶段：O(n)
- 总体：O(n+m)

### 3. 与其他算法的比较
- 暴力匹配：O(nm)
- KMP：O(n+m)
- Boyer-Moore：O(n/m)平均情况

### 4. 实际应用
- 字符串处理
- 模式识别
- 文本搜索

## 总结

KMP算法是字符串匹配的重要算法，其核心在于next数组的预处理和利用。虽然理解起来有一定难度，但掌握后能够高效解决字符串匹配问题。在考研中，重点掌握next数组的计算过程和算法的时间复杂度分析。 