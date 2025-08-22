# 冒泡排序 (Bubble Sort)

## 算法描述

冒泡排序是一种简单的排序算法，它重复地遍历要排序的数组，比较相邻的两个元素，如果它们的顺序错误就交换它们的位置。

**核心思想**：
- **相邻比较**：比较相邻的两个元素
- **交换位置**：如果顺序错误则交换它们的位置
- **重复遍历**：重复这个过程直到没有需要交换的元素

## 复杂度分析

| 复杂度 | 时间复杂度 | 空间复杂度 |
|--------|------------|------------|
| 最好情况 | O(n) | O(1) |
| 平均情况 | O(n²) | O(1) |
| 最坏情况 | O(n²) | O(1) |

**稳定性**：稳定排序算法

## 伪代码

```
冒泡排序(数组)
    n = 数组.长度
    对于 i = 1 到 n - 1
        已交换 = 假
        对于 j = 0 到 n - i - 1
            如果 数组[j] > 数组[j + 1]
                交换 数组[j] 和 数组[j + 1]
                已交换 = 真
        如果 未交换
            跳出循环
```

## C++ 实现

### 基础实现

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class BubbleSort {
public:
    // 主排序函数
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 0; i < n - 1; i++) {
            // 标记本轮是否发生交换
            bool swapped = false;
            
            // 比较相邻元素
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    std::swap(arr[j], arr[j + 1]);
                    swapped = true;
                }
            }
            
            // 如果没有发生交换，说明数组已经有序
            if (!swapped) {
                break;
            }
        }
    }
};
```

### 优化实现（记录最后交换位置）

```cpp
class OptimizedBubbleSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        int lastSwap = n - 1;  // 记录最后一次交换的位置
        
        while (lastSwap > 0) {
            int currentSwap = 0;  // 当前轮次最后一次交换的位置
            
            for (int j = 0; j < lastSwap; j++) {
                if (arr[j] > arr[j + 1]) {
                    std::swap(arr[j], arr[j + 1]);
                    currentSwap = j;
                }
            }
            
            lastSwap = currentSwap;
        }
    }
};
```

### 双向冒泡排序（鸡尾酒排序）

```cpp
class CocktailSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        bool swapped = true;
        int start = 0;
        int end = n - 1;
        
        while (swapped) {
            swapped = false;
            
            // 从左到右冒泡
            for (int i = start; i < end; i++) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
            
            end--;
            swapped = false;
            
            // 从右到左冒泡
            for (int i = end - 1; i >= start; i--) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            start++;
        }
    }
};
```

## 使用示例

```cpp
int main() {
    std::vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    
    std::cout << "原始数组: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // 使用冒泡排序
    BubbleSort::sort(arr);
    
    std::cout << "排序后数组: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 算法特点

### 优点
1. **简单直观**：算法逻辑简单，容易理解和实现
2. **原地排序**：不需要额外的数组空间
3. **稳定排序**：相等元素的相对位置不会改变
4. **自适应**：对于已经部分排序的数组，可以提前结束

### 缺点
1. **时间复杂度较高**：平均和最坏情况下都是 O(n²)
2. **交换次数多**：需要频繁交换相邻元素
3. **不适合大规模数据**：当数据量很大时效率很低

## 测试用例

### 典型测试用例

```cpp
void testBubbleSort() {
    // 测试用例1：普通数组
    std::vector<int> arr1 = {64, 34, 25, 12, 22, 11, 90};
    BubbleSort::sort(arr1);
    assert(std::is_sorted(arr1.begin(), arr1.end()));
    
    // 测试用例2：已排序数组
    std::vector<int> arr2 = {1, 2, 3, 4, 5};
    BubbleSort::sort(arr2);
    assert(std::is_sorted(arr2.begin(), arr2.end()));
    
    // 测试用例3：逆序数组
    std::vector<int> arr3 = {5, 4, 3, 2, 1};
    BubbleSort::sort(arr3);
    assert(std::is_sorted(arr3.begin(), arr3.end()));
    
    // 测试用例4：包含重复元素
    std::vector<int> arr4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    BubbleSort::sort(arr4);
    assert(std::is_sorted(arr4.begin(), arr4.end()));
    
    // 测试用例5：空数组
    std::vector<int> arr5;
    BubbleSort::sort(arr5);
    assert(arr5.empty());
    
    // 测试用例6：单元素数组
    std::vector<int> arr6 = {42};
    BubbleSort::sort(arr6);
    assert(arr6.size() == 1 && arr6[0] == 42);
    
    std::cout << "所有测试用例通过！" << std::endl;
}
```

### 边界测试用例

```cpp
void testEdgeCases() {
    // 测试小规模数据
    std::vector<int> smallArr = {3, 1, 2};
    BubbleSort::sort(smallArr);
    assert(std::is_sorted(smallArr.begin(), smallArr.end()));
    
    // 测试相同元素
    std::vector<int> sameArr(100, 42);
    BubbleSort::sort(sameArr);
    assert(std::all_of(sameArr.begin(), sameArr.end(), 
                       [](int x) { return x == 42; }));
    
    // 测试部分排序的数组
    std::vector<int> partialArr = {1, 2, 3, 5, 4, 6, 7};
    BubbleSort::sort(partialArr);
    assert(std::is_sorted(partialArr.begin(), partialArr.end()));
    
    std::cout << "边界测试用例通过！" << std::endl;
}
```

## 常见错误

### 1. 循环边界错误
```cpp
// 错误：循环边界不正确
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        if (arr[j] > arr[j + 1]) {
            std::swap(arr[j], arr[j + 1]);
        }
    }
}

// 正确：内层循环边界应该是 n - i - 1
for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            std::swap(arr[j], arr[j + 1]);
        }
    }
}
```

### 2. 缺少优化标志
```cpp
// 错误：没有提前结束的优化
for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            std::swap(arr[j], arr[j + 1]);
        }
    }
}

// 正确：添加优化标志
for (int i = 0; i < n - 1; i++) {
    bool swapped = false;
    for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            std::swap(arr[j], arr[j + 1]);
            swapped = true;
        }
    }
    if (!swapped) break;
}
```

### 3. 数组越界
```cpp
// 错误：可能越界
for (int j = 0; j < n - i; j++) {  // 应该是 n - i - 1
    if (arr[j] > arr[j + 1]) {
        std::swap(arr[j], arr[j + 1]);
    }
}

// 正确：确保不会越界
for (int j = 0; j < n - i - 1; j++) {
    if (arr[j] > arr[j + 1]) {
        std::swap(arr[j], arr[j + 1]);
    }
}
```

## 算法变体

### 1. 选择排序（类似冒泡但不同）
```cpp
class SelectionSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            
            // 找到最小元素的位置
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // 将最小元素放到正确位置
            if (minIndex != i) {
                std::swap(arr[i], arr[minIndex]);
            }
        }
    }
};
```

### 2. 奇偶排序
```cpp
class OddEvenSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        bool sorted = false;
        
        while (!sorted) {
            sorted = true;
            
            // 奇数索引比较
            for (int i = 1; i < n - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
            
            // 偶数索引比较
            for (int i = 0; i < n - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
        }
    }
};
```

## 优化技巧

### 1. 记录最后交换位置
```cpp
static void sortOptimized(std::vector<int>& arr) {
    int n = arr.size();
    int lastSwap = n - 1;
    
    while (lastSwap > 0) {
        int currentSwap = 0;
        
        for (int j = 0; j < lastSwap; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                currentSwap = j;
            }
        }
        
        lastSwap = currentSwap;
    }
}
```

### 2. 双向冒泡优化
```cpp
static void bidirectionalBubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    bool swapped = true;
    int start = 0;
    int end = n - 1;
    
    while (swapped) {
        swapped = false;
        
        // 正向冒泡
        for (int i = start; i < end; i++) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) break;
        
        end--;
        swapped = false;
        
        // 反向冒泡
        for (int i = end - 1; i >= start; i--) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
        
        start++;
    }
}
```

## 应用场景

1. **教学演示**：算法简单，适合教学和演示
2. **小规模数据**：当数据量很小时，冒泡排序可以接受
3. **稳定排序需求**：需要保持相等元素相对位置时
4. **硬件实现**：在某些硬件环境中实现简单
5. **调试和测试**：作为基准算法进行性能对比

## 与其他排序算法的比较

### 冒泡排序 vs 插入排序
- **冒泡排序**：O(n²) 但交换次数更多
- **插入排序**：O(n²) 但对于已排序数据接近 O(n)

### 冒泡排序 vs 选择排序
- **冒泡排序**：O(n²) 且交换次数多
- **选择排序**：O(n²) 但交换次数少

### 冒泡排序 vs 快速排序
- **冒泡排序**：O(n²) 且不适合大规模数据
- **快速排序**：O(n log n) 平均情况，适合大规模数据

## 性能分析

### 交换次数分析
```cpp
// 统计交换次数
static int sortWithCount(std::vector<int>& arr) {
    int n = arr.size();
    int swapCount = 0;
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
                swapCount++;
            }
        }
        
        if (!swapped) break;
    }
    
    return swapCount;
}
```

### 比较次数分析
```cpp
// 统计比较次数
static int sortWithComparisonCount(std::vector<int>& arr) {
    int n = arr.size();
    int comparisonCount = 0;
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            comparisonCount++;
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) break;
    }
    
    return comparisonCount;
}
```

## 总结

冒泡排序是一种简单、稳定、原地的排序算法，具有以下特点：

- **时间复杂度**：O(n²) 平均和最坏情况，O(n) 最好情况
- **空间复杂度**：O(1) - 原地排序
- **稳定性**：稳定排序算法
- **适用性**：主要适用于教学和小规模数据

虽然时间复杂度较高且交换次数多，但冒泡排序的简单性和稳定性使其在特定场景下仍然有用，特别是在教学、调试或作为其他算法的基准时。 