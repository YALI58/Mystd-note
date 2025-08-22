# 归并排序 (Merge Sort)

## 算法描述

归并排序是一种基于分治策略的排序算法。它将待排序的数组分成两个子数组，分别对这两个子数组进行排序，然后将两个有序子数组合并成一个有序数组。

**核心思想**：
- **分治**：将大问题分解为小问题
- **合并**：将两个有序数组合并为一个有序数组
- **递归**：对子数组重复执行分治过程

## 复杂度分析

| 复杂度 | 时间复杂度 | 空间复杂度 |
|--------|------------|------------|
| 最好情况 | O(n log n) | O(n) |
| 平均情况 | O(n log n) | O(n) |
| 最坏情况 | O(n log n) | O(n) |

**稳定性**：稳定排序算法

## 伪代码

```
归并排序(数组, 左边界, 右边界)
    如果 左边界 < 右边界
        中点 = (左边界 + 右边界) / 2
        归并排序(数组, 左边界, 中点)      // 递归排序左半部分
        归并排序(数组, 中点 + 1, 右边界) // 递归排序右半部分
        合并(数组, 左边界, 中点, 右边界)     // 合并两个有序数组

合并(数组, 左边界, 中点, 右边界)
    // 创建临时数组
    左数组[0...n1] = 数组[左边界...中点]
    右数组[0...n2] = 数组[中点+1...右边界]
    
    i = 0, j = 0, k = 左边界
    
    // 合并两个有序数组
    当 i < n1 且 j < n2
        如果 左数组[i] <= 右数组[j]
            数组[k] = 左数组[i]
            i = i + 1
        否则
            数组[k] = 右数组[j]
            j = j + 1
        k = k + 1
    
    // 复制剩余元素
    当 i < n1
        数组[k] = 左数组[i]
        i = i + 1
        k = k + 1
    
    当 j < n2
        数组[k] = 右数组[j]
        j = j + 1
        k = k + 1
```

## C++ 实现

### 基础实现

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class MergeSort {
public:
    // 主排序函数
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        mergeSort(arr, 0, arr.size() - 1);
    }

private:
    // 递归排序函数
    static void mergeSort(std::vector<int>& arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;  // 避免整数溢出
            
            // 递归排序左半部分
            mergeSort(arr, left, mid);
            // 递归排序右半部分
            mergeSort(arr, mid + 1, right);
            // 合并两个有序数组
            merge(arr, left, mid, right);
        }
    }
    
    // 合并两个有序数组
    static void merge(std::vector<int>& arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        // 创建临时数组
        std::vector<int> L(n1), R(n2);
        
        // 复制数据到临时数组
        for (int i = 0; i < n1; i++) {
            L[i] = arr[left + i];
        }
        for (int j = 0; j < n2; j++) {
            R[j] = arr[mid + 1 + j];
        }
        
        // 合并两个有序数组
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        
        // 复制剩余元素
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
};
```

### 优化实现（原地归并）

```cpp
class OptimizedMergeSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        
        // 创建临时数组，避免重复分配
        std::vector<int> temp(arr.size());
        mergeSort(arr, temp, 0, arr.size() - 1);
    }

private:
    static void mergeSort(std::vector<int>& arr, std::vector<int>& temp, 
                         int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            
            mergeSort(arr, temp, left, mid);
            mergeSort(arr, temp, mid + 1, right);
            merge(arr, temp, left, mid, right);
        }
    }
    
    static void merge(std::vector<int>& arr, std::vector<int>& temp,
                     int left, int mid, int right) {
        int i = left, j = mid + 1, k = left;
        
        // 合并到临时数组
        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }
        
        // 复制剩余元素
        while (i <= mid) {
            temp[k++] = arr[i++];
        }
        while (j <= right) {
            temp[k++] = arr[j++];
        }
        
        // 复制回原数组
        for (int p = left; p <= right; p++) {
            arr[p] = temp[p];
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
    
    // 使用归并排序
    MergeSort::sort(arr);
    
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
1. **时间复杂度稳定**：无论输入数据如何，时间复杂度都是 O(n log n)
2. **稳定性好**：相等元素的相对位置不会改变
3. **适合外部排序**：可以处理无法全部加载到内存的大文件
4. **并行性好**：可以很容易地并行化

### 缺点
1. **空间复杂度较高**：需要额外的 O(n) 空间
2. **小数据效率低**：对于小规模数据，插入排序等简单算法可能更快
3. **缓存不友好**：访问模式不够局部化

## 测试用例

### 典型测试用例

```cpp
void testMergeSort() {
    // 测试用例1：普通数组
    std::vector<int> arr1 = {64, 34, 25, 12, 22, 11, 90};
    MergeSort::sort(arr1);
    assert(std::is_sorted(arr1.begin(), arr1.end()));
    
    // 测试用例2：已排序数组
    std::vector<int> arr2 = {1, 2, 3, 4, 5};
    MergeSort::sort(arr2);
    assert(std::is_sorted(arr2.begin(), arr2.end()));
    
    // 测试用例3：逆序数组
    std::vector<int> arr3 = {5, 4, 3, 2, 1};
    MergeSort::sort(arr3);
    assert(std::is_sorted(arr3.begin(), arr3.end()));
    
    // 测试用例4：包含重复元素
    std::vector<int> arr4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    MergeSort::sort(arr4);
    assert(std::is_sorted(arr4.begin(), arr4.end()));
    
    // 测试用例5：空数组
    std::vector<int> arr5;
    MergeSort::sort(arr5);
    assert(arr5.empty());
    
    // 测试用例6：单元素数组
    std::vector<int> arr6 = {42};
    MergeSort::sort(arr6);
    assert(arr6.size() == 1 && arr6[0] == 42);
    
    std::cout << "所有测试用例通过！" << std::endl;
}
```

### 边界测试用例

```cpp
void testEdgeCases() {
    // 测试大规模数据
    std::vector<int> largeArr(10000);
    for (int i = 0; i < 10000; i++) {
        largeArr[i] = 10000 - i;
    }
    MergeSort::sort(largeArr);
    assert(std::is_sorted(largeArr.begin(), largeArr.end()));
    
    // 测试相同元素
    std::vector<int> sameArr(1000, 42);
    MergeSort::sort(sameArr);
    assert(std::all_of(sameArr.begin(), sameArr.end(), 
                       [](int x) { return x == 42; }));
    
    std::cout << "边界测试用例通过！" << std::endl;
}
```

## 常见错误

### 1. 整数溢出
```cpp
// 错误写法
int mid = (left + right) / 2;  // 可能溢出

// 正确写法
int mid = left + (right - left) / 2;  // 避免溢出
```

### 2. 数组越界
```cpp
// 错误：没有检查边界条件
void mergeSort(vector<int>& arr, int left, int right) {
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

// 正确：添加边界检查
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {  // 重要：检查边界条件
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

### 3. 临时数组大小错误
```cpp
// 错误：临时数组大小不够
vector<int> temp(right - left);  // 大小应该是 right - left + 1

// 正确
vector<int> temp(right - left + 1);
```

## 算法变体

### 1. 自底向上归并排序
```cpp
class BottomUpMergeSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        std::vector<int> temp(n);
        
        // 从1开始，每次翻倍
        for (int size = 1; size < n; size = size * 2) {
            for (int left = 0; left < n - size; left += size * 2) {
                int mid = left + size - 1;
                int right = std::min(left + size * 2 - 1, n - 1);
                merge(arr, temp, left, mid, right);
            }
        }
    }
    
private:
    static void merge(std::vector<int>& arr, std::vector<int>& temp,
                     int left, int mid, int right) {
        // 合并逻辑与之前相同
        // ...
    }
};
```

### 2. 原地归并排序（复杂实现）
```cpp
class InPlaceMergeSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        inPlaceMergeSort(arr, 0, arr.size() - 1);
    }

private:
    static void inPlaceMergeSort(std::vector<int>& arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            inPlaceMergeSort(arr, left, mid);
            inPlaceMergeSort(arr, mid + 1, right);
            inPlaceMerge(arr, left, mid, right);
        }
    }
    
    // 原地合并（使用旋转操作）
    static void inPlaceMerge(std::vector<int>& arr, int left, int mid, int right) {
        // 实现较为复杂，使用旋转操作来避免额外空间
        // 这里省略具体实现
    }
};
```

## 优化技巧

### 1. 小数组使用插入排序
```cpp
static void mergeSort(std::vector<int>& arr, int left, int right) {
    // 对于小数组，使用插入排序
    if (right - left + 1 <= 10) {
        insertionSort(arr, left, right);
        return;
    }
    
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}
```

### 2. 避免不必要的合并
```cpp
static void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        // 如果左半部分的最大值小于等于右半部分的最小值，则不需要合并
        if (arr[mid] > arr[mid + 1]) {
            merge(arr, left, mid, right);
        }
    }
}
```

## 应用场景

1. **外部排序**：处理无法全部加载到内存的大文件
2. **链表排序**：归并排序特别适合链表结构
3. **并行计算**：可以很容易地并行化
4. **稳定排序需求**：需要保持相等元素相对位置时
5. **大规模数据排序**：当数据量很大且对稳定性有要求时

## 总结

归并排序是一种高效、稳定的排序算法，具有以下特点：

- **时间复杂度**：O(n log n) - 在所有情况下都稳定
- **空间复杂度**：O(n) - 需要额外空间
- **稳定性**：稳定排序算法
- **适用性**：特别适合外部排序和链表排序

虽然空间复杂度较高，但归并排序的稳定性和可预测的性能使其在许多场景下都是优秀的选择，特别是在需要稳定排序或处理大规模数据时。 