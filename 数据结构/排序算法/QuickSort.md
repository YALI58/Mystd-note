# 快速排序 (Quick Sort)

## 算法描述

快速排序是一种高效的排序算法，使用分治策略。它选择一个"基准"元素，将数组分为两部分，使得左边部分的所有元素都小于基准，右边部分的所有元素都大于基准，然后递归地对这两部分进行排序。

**核心思想**：
- **分治策略**：将大问题分解为小问题
- **基准选择**：选择一个基准元素进行分区
- **分区操作**：将数组分为小于基准和大于基准的两部分
- **递归排序**：对分区后的子数组递归排序

## 复杂度分析

| 复杂度 | 时间复杂度 | 空间复杂度 |
|--------|------------|------------|
| 最好情况 | O(n log n) | O(log n) |
| 平均情况 | O(n log n) | O(log n) |
| 最坏情况 | O(n²) | O(n) |

**稳定性**：不稳定排序算法

## 伪代码

```
快速排序(A, 左边界, 右边界)
    如果 左边界 < 右边界
        基准位置 = 分区(A, 左边界, 右边界)
        快速排序(A, 左边界, 基准位置 - 1)
        快速排序(A, 基准位置 + 1, 右边界)

分区(A, 左边界, 右边界)
    基准值 = A[右边界]  // 选择最后一个元素作为基准
    i = 左边界 - 1      // 小于基准区域的边界
    
    对于 j = 左边界 到 右边界 - 1
        如果 A[j] <= 基准值
            i = i + 1
            交换 A[i] 和 A[j]
    
    交换 A[i + 1] 和 A[右边界]
    返回 i + 1
```

## C++ 实现

### 基础实现

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class QuickSort {
public:
    // 主排序函数
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        quickSort(arr, 0, arr.size() - 1);
    }

private:
    // 快速排序递归函数
    static void quickSort(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }
    
    // 分区函数
    static int partition(std::vector<int>& arr, int low, int high) {
        int pivot = arr[high];  // 选择最后一个元素作为基准
        int i = low - 1;        // 小于基准区域的边界
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }
};
```

### 优化实现（三数取中法）

```cpp
class OptimizedQuickSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        quickSort(arr, 0, arr.size() - 1);
    }

private:
    static void quickSort(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            // 使用三数取中法选择基准
            int mid = low + (high - low) / 2;
            medianOfThree(arr, low, mid, high);
            
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }
    
    // 三数取中法
    static void medianOfThree(std::vector<int>& arr, int low, int mid, int high) {
        if (arr[low] > arr[mid]) {
            std::swap(arr[low], arr[mid]);
        }
        if (arr[low] > arr[high]) {
            std::swap(arr[low], arr[high]);
        }
        if (arr[mid] > arr[high]) {
            std::swap(arr[mid], arr[high]);
        }
        // 将中位数放到high位置
        std::swap(arr[mid], arr[high]);
    }
    
    static int partition(std::vector<int>& arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }
};
```

### 双指针分区实现

```cpp
class DualPivotQuickSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        quickSort(arr, 0, arr.size() - 1);
    }

private:
    static void quickSort(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            // 双指针分区
            auto [leftPivot, rightPivot] = dualPivotPartition(arr, low, high);
            quickSort(arr, low, leftPivot - 1);
            quickSort(arr, leftPivot + 1, rightPivot - 1);
            quickSort(arr, rightPivot + 1, high);
        }
    }
    
    // 双指针分区
    static std::pair<int, int> dualPivotPartition(std::vector<int>& arr, int low, int high) {
        if (arr[low] > arr[high]) {
            std::swap(arr[low], arr[high]);
        }
        
        int leftPivot = arr[low];   // 左基准
        int rightPivot = arr[high]; // 右基准
        
        int less = low + 1;     // 小于左基准的区域
        int great = high - 1;    // 大于右基准的区域
        int k = less;            // 当前扫描位置
        
        while (k <= great) {
            if (arr[k] < leftPivot) {
                std::swap(arr[k], arr[less]);
                less++;
            } else if (arr[k] > rightPivot) {
                while (k < great && arr[great] > rightPivot) {
                    great--;
                }
                std::swap(arr[k], arr[great]);
                great--;
                
                if (arr[k] < leftPivot) {
                    std::swap(arr[k], arr[less]);
                    less++;
                }
            }
            k++;
        }
        
        less--;
        great++;
        
        std::swap(arr[low], arr[less]);
        std::swap(arr[high], arr[great]);
        
        return {less, great};
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
    
    // 使用基础快速排序
    QuickSort::sort(arr);
    
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
1. **平均效率高**：平均时间复杂度为 O(n log n)
2. **原地排序**：不需要额外的数组空间
3. **缓存友好**：对局部性原理友好
4. **适应性强**：对部分有序数据表现良好

### 缺点
1. **不稳定排序**：相同元素的相对位置可能改变
2. **最坏情况**：对于已经排序的数据，时间复杂度为 O(n²)
3. **递归开销**：递归调用可能导致栈溢出

## 优化策略

1. **基准选择优化**：
   - 三数取中法
   - 随机选择基准
   - 九数取中法

2. **小数组优化**：
   - 当数组长度小于某个阈值时使用插入排序

3. **重复元素优化**：
   - 三路快排处理大量重复元素

4. **尾递归优化**：
   - 减少递归调用次数

## 考研重点

1. **手写代码**：能够手写快速排序的核心代码
2. **复杂度分析**：理解最好、最坏、平均情况的时间复杂度
3. **基准选择**：理解不同基准选择策略的影响
4. **分区过程**：掌握分区算法的实现细节
5. **优化方法**：了解各种优化策略的原理 