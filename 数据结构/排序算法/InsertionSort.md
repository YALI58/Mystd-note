# 插入排序 (Insertion Sort)

## 算法描述

插入排序是一种简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

**核心思想**：
- **构建有序序列**：将数组分为已排序和未排序两部分
- **逐个插入**：从未排序部分取出元素，插入到已排序部分的正确位置
- **移动元素**：为了给新元素腾出位置，需要将已排序部分的部分元素向后移动

## 复杂度分析

| 复杂度 | 时间复杂度 | 空间复杂度 |
|--------|------------|------------|
| 最好情况 | O(n) | O(1) |
| 平均情况 | O(n²) | O(1) |
| 最坏情况 | O(n²) | O(1) |

**稳定性**：稳定排序算法

## 伪代码

```
插入排序(数组)
    对于 j = 2 到 数组.长度
        关键字 = 数组[j]
        // 将 数组[j] 插入到已排序序列 数组[1..j-1] 中
        i = j - 1
        当 i > 0 且 数组[i] > 关键字
            数组[i + 1] = 数组[i]
            i = i - 1
        数组[i + 1] = 关键字
```

## C++ 实现

### 基础实现

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class InsertionSort {
public:
    // 主排序函数
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            
            // 将 arr[i] 插入到已排序序列 arr[0..i-1] 中
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
};
```

### 优化实现（减少交换次数）

```cpp
class OptimizedInsertionSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 1; i < n; i++) {
            // 使用二分查找找到插入位置
            int key = arr[i];
            int insertPos = binarySearch(arr, 0, i - 1, key);
            
            // 移动元素
            for (int j = i; j > insertPos; j--) {
                arr[j] = arr[j - 1];
            }
            arr[insertPos] = key;
        }
    }

private:
    // 二分查找插入位置
    static int binarySearch(const std::vector<int>& arr, int left, int right, int key) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] <= key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
```

### 递归实现

```cpp
class RecursiveInsertionSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        insertionSortRecursive(arr, arr.size());
    }

private:
    static void insertionSortRecursive(std::vector<int>& arr, int n) {
        // 基本情况：只有一个元素时已经排序
        if (n <= 1) return;
        
        // 递归排序前 n-1 个元素
        insertionSortRecursive(arr, n - 1);
        
        // 将第 n 个元素插入到已排序序列中
        int key = arr[n - 1];
        int j = n - 2;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
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
    
    // 使用插入排序
    InsertionSort::sort(arr);
    
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
4. **自适应**：对于已经部分排序的数组效率较高
5. **在线算法**：可以边接收数据边排序

### 缺点
1. **时间复杂度较高**：平均和最坏情况下都是 O(n²)
2. **不适合大规模数据**：当数据量很大时效率较低
3. **交换次数多**：需要频繁移动元素

## 测试用例

### 典型测试用例

```cpp
void testInsertionSort() {
    // 测试用例1：普通数组
    std::vector<int> arr1 = {64, 34, 25, 12, 22, 11, 90};
    InsertionSort::sort(arr1);
    assert(std::is_sorted(arr1.begin(), arr1.end()));
    
    // 测试用例2：已排序数组
    std::vector<int> arr2 = {1, 2, 3, 4, 5};
    InsertionSort::sort(arr2);
    assert(std::is_sorted(arr2.begin(), arr2.end()));
    
    // 测试用例3：逆序数组
    std::vector<int> arr3 = {5, 4, 3, 2, 1};
    InsertionSort::sort(arr3);
    assert(std::is_sorted(arr3.begin(), arr3.end()));
    
    // 测试用例4：包含重复元素
    std::vector<int> arr4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    InsertionSort::sort(arr4);
    assert(std::is_sorted(arr4.begin(), arr4.end()));
    
    // 测试用例5：空数组
    std::vector<int> arr5;
    InsertionSort::sort(arr5);
    assert(arr5.empty());
    
    // 测试用例6：单元素数组
    std::vector<int> arr6 = {42};
    InsertionSort::sort(arr6);
    assert(arr6.size() == 1 && arr6[0] == 42);
    
    std::cout << "所有测试用例通过！" << std::endl;
}
```

### 边界测试用例

```cpp
void testEdgeCases() {
    // 测试小规模数据
    std::vector<int> smallArr = {3, 1, 2};
    InsertionSort::sort(smallArr);
    assert(std::is_sorted(smallArr.begin(), smallArr.end()));
    
    // 测试相同元素
    std::vector<int> sameArr(100, 42);
    InsertionSort::sort(sameArr);
    assert(std::all_of(sameArr.begin(), sameArr.end(), 
                       [](int x) { return x == 42; }));
    
    // 测试部分排序的数组
    std::vector<int> partialArr = {1, 2, 3, 5, 4, 6, 7};
    InsertionSort::sort(partialArr);
    assert(std::is_sorted(partialArr.begin(), partialArr.end()));
    
    std::cout << "边界测试用例通过！" << std::endl;
}
```

## 常见错误

### 1. 数组越界
```cpp
// 错误：没有检查边界条件
for (int i = 1; i < n; i++) {
    int key = arr[i];
    int j = i - 1;
    while (arr[j] > key) {  // 可能越界
        arr[j + 1] = arr[j];
        j--;
    }
    arr[j + 1] = key;
}

// 正确：添加边界检查
for (int i = 1; i < n; i++) {
    int key = arr[i];
    int j = i - 1;
    while (j >= 0 && arr[j] > key) {  // 检查 j >= 0
        arr[j + 1] = arr[j];
        j--;
    }
    arr[j + 1] = key;
}
```

### 2. 插入位置错误
```cpp
// 错误：插入位置计算错误
while (j >= 0 && arr[j] > key) {
    arr[j + 1] = arr[j];
    j--;
}
arr[j] = key;  // 应该是 arr[j + 1] = key

// 正确
while (j >= 0 && arr[j] > key) {
    arr[j + 1] = arr[j];
    j--;
}
arr[j + 1] = key;  // 正确的位置
```

### 3. 循环条件错误
```cpp
// 错误：使用错误的比较条件
while (j >= 0 && arr[j] >= key) {  // 使用 >= 会破坏稳定性

// 正确：使用 > 保持稳定性
while (j >= 0 && arr[j] > key) {
    arr[j + 1] = arr[j];
    j--;
}
```

## 算法变体

### 1. 希尔排序（Shell Sort）
```cpp
class ShellSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        // 使用不同的间隔序列
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int key = arr[i];
                int j = i;
                
                while (j >= gap && arr[j - gap] > key) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                arr[j] = key;
            }
        }
    }
};
```

### 2. 二分插入排序
```cpp
class BinaryInsertionSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int insertPos = binarySearch(arr, 0, i - 1, key);
            
            // 移动元素
            for (int j = i; j > insertPos; j--) {
                arr[j] = arr[j - 1];
            }
            arr[insertPos] = key;
        }
    }

private:
    static int binarySearch(const std::vector<int>& arr, int left, int right, int key) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] <= key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
```

## 优化技巧

### 1. 减少交换次数
```cpp
// 优化版本：减少元素移动次数
static void sortOptimized(std::vector<int>& arr) {
    int n = arr.size();
    
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // 一次性找到插入位置，减少比较次数
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

### 2. 使用哨兵
```cpp
// 使用哨兵简化边界检查
static void sortWithSentinel(std::vector<int>& arr) {
    // 在数组开头添加一个很小的值作为哨兵
    arr.insert(arr.begin(), INT_MIN);
    
    int n = arr.size();
    for (int i = 2; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // 不需要检查 j >= 0，因为哨兵保证循环会停止
        while (arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    
    // 移除哨兵
    arr.erase(arr.begin());
}
```

## 应用场景

1. **小规模数据排序**：当数据量较小时，插入排序效率较高
2. **部分排序数据**：对于已经部分排序的数组，插入排序效率很高
3. **在线算法**：可以边接收数据边排序
4. **稳定排序需求**：需要保持相等元素相对位置时
5. **教学演示**：算法简单，适合教学和演示

## 与其他排序算法的比较

### 插入排序 vs 冒泡排序
- **插入排序**：O(n²) 但实际运行时间通常比冒泡排序快
- **冒泡排序**：O(n²) 且交换次数更多

### 插入排序 vs 选择排序
- **插入排序**：O(n²) 但对于已排序数据接近 O(n)
- **选择排序**：O(n²) 且对于已排序数据仍然是 O(n²)

### 插入排序 vs 快速排序
- **插入排序**：小规模数据（通常 n < 10）时更快
- **快速排序**：大规模数据时更快，但需要额外空间

## 总结

插入排序是一种简单、稳定、原地的排序算法，具有以下特点：

- **时间复杂度**：O(n²) 平均和最坏情况，O(n) 最好情况
- **空间复杂度**：O(1) - 原地排序
- **稳定性**：稳定排序算法
- **适用性**：特别适合小规模数据和部分排序的数据

虽然时间复杂度较高，但插入排序的简单性和在某些情况下的高效性使其在特定场景下仍然有用，特别是在小规模数据排序或作为其他高级排序算法的子算法时。 