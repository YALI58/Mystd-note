# 堆排序 (Heap Sort)

## 算法描述

堆排序是一种基于二叉堆数据结构的比较排序算法。它利用堆这种数据结构所设计的排序算法，是一种选择排序。

**核心思想**：
- **构建堆**：将待排序数组构建成最大堆（或最小堆）
- **堆化**：维护堆的性质，确保父节点总是大于（或小于）子节点
- **排序**：重复从堆顶取出最大（或最小）元素，放到数组末尾

## 复杂度分析

| 复杂度 | 时间复杂度 | 空间复杂度 |
|--------|------------|------------|
| 最好情况 | O(n log n) | O(1) |
| 平均情况 | O(n log n) | O(1) |
| 最坏情况 | O(n log n) | O(1) |

**稳定性**：不稳定排序算法

## 伪代码

```
堆排序(数组)
    构建最大堆(数组)           // 构建最大堆
    对于 i = 数组.长度 递减到 2
        交换 数组[1] 和 数组[i]  // 将最大值移到末尾
        数组.堆大小 = 数组.堆大小 - 1
        最大堆化(数组, 1)        // 维护堆性质

构建最大堆(数组)
    数组.堆大小 = 数组.长度
    对于 i = 数组.长度/2 递减到 1
        最大堆化(数组, i)

最大堆化(数组, i)
    l = 左子节点(i)     // 左子节点
    r = 右子节点(i)    // 右子节点
    最大值位置 = i
    
    如果 l <= 数组.堆大小 且 数组[l] > 数组[最大值位置]
        最大值位置 = l
    
    如果 r <= 数组.堆大小 且 数组[r] > 数组[最大值位置]
        最大值位置 = r
    
    如果 最大值位置 != i
        交换 数组[i] 和 数组[最大值位置]
        最大堆化(数组, 最大值位置)

左子节点(i)
    返回 2*i

右子节点(i)
    返回 2*i + 1
```

## C++ 实现

### 基础实现

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class HeapSort {
public:
    // 主排序函数
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        
        int n = arr.size();
        
        // 构建最大堆
        buildMaxHeap(arr);
        
        // 逐个从堆中取出元素
        for (int i = n - 1; i > 0; i--) {
            // 将最大值（根节点）移到末尾
            std::swap(arr[0], arr[i]);
            
            // 对剩余元素重新堆化
            maxHeapify(arr, 0, i);
        }
    }

private:
    // 构建最大堆
    static void buildMaxHeap(std::vector<int>& arr) {
        int n = arr.size();
        // 从最后一个非叶子节点开始，自底向上构建堆
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeapify(arr, i, n);
        }
    }
    
    // 维护最大堆性质
    static void maxHeapify(std::vector<int>& arr, int i, int heapSize) {
        int largest = i;
        int left = 2 * i + 1;    // 左子节点
        int right = 2 * i + 2;   // 右子节点
        
        // 找到最大值
        if (left < heapSize && arr[left] > arr[largest]) {
            largest = left;
        }
        
        if (right < heapSize && arr[right] > arr[largest]) {
            largest = right;
        }
        
        // 如果最大值不是当前节点，则交换并继续堆化
        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            maxHeapify(arr, largest, heapSize);
        }
    }
};
```

### 优化实现（迭代版本）

```cpp
class OptimizedHeapSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        
        int n = arr.size();
        buildMaxHeap(arr);
        
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            maxHeapifyIterative(arr, 0, i);
        }
    }

private:
    static void buildMaxHeap(std::vector<int>& arr) {
        int n = arr.size();
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeapifyIterative(arr, i, n);
        }
    }
    
    // 迭代版本的堆化函数，避免递归调用
    static void maxHeapifyIterative(std::vector<int>& arr, int i, int heapSize) {
        while (true) {
            int largest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            
            if (left < heapSize && arr[left] > arr[largest]) {
                largest = left;
            }
            
            if (right < heapSize && arr[right] > arr[largest]) {
                largest = right;
            }
            
            if (largest == i) {
                break;  // 堆性质已满足
            }
            
            std::swap(arr[i], arr[largest]);
            i = largest;
        }
    }
};
```

### 最小堆版本（降序排序）

```cpp
class MinHeapSort {
public:
    // 降序排序
    static void sortDescending(std::vector<int>& arr) {
        if (arr.empty()) return;
        
        int n = arr.size();
        buildMinHeap(arr);
        
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            minHeapify(arr, 0, i);
        }
    }

private:
    static void buildMinHeap(std::vector<int>& arr) {
        int n = arr.size();
        for (int i = n / 2 - 1; i >= 0; i--) {
            minHeapify(arr, i, n);
        }
    }
    
    static void minHeapify(std::vector<int>& arr, int i, int heapSize) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < heapSize && arr[left] < arr[smallest]) {
            smallest = left;
        }
        
        if (right < heapSize && arr[right] < arr[smallest]) {
            smallest = right;
        }
        
        if (smallest != i) {
            std::swap(arr[i], arr[smallest]);
            minHeapify(arr, smallest, heapSize);
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
    
    // 使用堆排序
    HeapSort::sort(arr);
    
    std::cout << "升序排序后: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // 降序排序
    std::vector<int> arr2 = {64, 34, 25, 12, 22, 11, 90};
    MinHeapSort::sortDescending(arr2);
    
    std::cout << "降序排序后: ";
    for (int num : arr2) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 算法特点

### 优点
1. **原地排序**：不需要额外的数组空间
2. **时间复杂度稳定**：无论输入数据如何，时间复杂度都是 O(n log n)
3. **适合外部排序**：可以处理无法全部加载到内存的大文件
4. **适合优先级队列**：堆结构天然适合优先级队列的实现

### 缺点
1. **不稳定排序**：相等元素的相对位置可能改变
2. **缓存不友好**：访问模式不够局部化
3. **小数据效率低**：对于小规模数据，插入排序等简单算法可能更快

## 测试用例

### 典型测试用例

```cpp
void testHeapSort() {
    // 测试用例1：普通数组
    std::vector<int> arr1 = {64, 34, 25, 12, 22, 11, 90};
    HeapSort::sort(arr1);
    assert(std::is_sorted(arr1.begin(), arr1.end()));
    
    // 测试用例2：已排序数组
    std::vector<int> arr2 = {1, 2, 3, 4, 5};
    HeapSort::sort(arr2);
    assert(std::is_sorted(arr2.begin(), arr2.end()));
    
    // 测试用例3：逆序数组
    std::vector<int> arr3 = {5, 4, 3, 2, 1};
    HeapSort::sort(arr3);
    assert(std::is_sorted(arr3.begin(), arr3.end()));
    
    // 测试用例4：包含重复元素
    std::vector<int> arr4 = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    HeapSort::sort(arr4);
    assert(std::is_sorted(arr4.begin(), arr4.end()));
    
    // 测试用例5：空数组
    std::vector<int> arr5;
    HeapSort::sort(arr5);
    assert(arr5.empty());
    
    // 测试用例6：单元素数组
    std::vector<int> arr6 = {42};
    HeapSort::sort(arr6);
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
    HeapSort::sort(largeArr);
    assert(std::is_sorted(largeArr.begin(), largeArr.end()));
    
    // 测试相同元素
    std::vector<int> sameArr(1000, 42);
    HeapSort::sort(sameArr);
    assert(std::all_of(sameArr.begin(), sameArr.end(), 
                       [](int x) { return x == 42; }));
    
    // 测试堆性质
    std::vector<int> testArr = {1, 2, 3, 4, 5, 6, 7};
    HeapSort::sort(testArr);
    assert(testArr[0] <= testArr[1] && testArr[1] <= testArr[2]);
    
    std::cout << "边界测试用例通过！" << std::endl;
}
```

## 常见错误

### 1. 堆化函数索引错误
```cpp
// 错误：使用错误的子节点索引
int left = 2 * i;      // 应该是 2 * i + 1
int right = 2 * i + 1; // 应该是 2 * i + 2

// 正确
int left = 2 * i + 1;
int right = 2 * i + 2;
```

### 2. 构建堆的起始位置错误
```cpp
// 错误：从最后一个元素开始
for (int i = n - 1; i >= 0; i--) {
    maxHeapify(arr, i, n);
}

// 正确：从最后一个非叶子节点开始
for (int i = n / 2 - 1; i >= 0; i--) {
    maxHeapify(arr, i, n);
}
```

### 3. 堆大小更新错误
```cpp
// 错误：没有正确更新堆大小
for (int i = n - 1; i > 0; i--) {
    std::swap(arr[0], arr[i]);
    maxHeapify(arr, 0, n);  // 应该使用 i 而不是 n
}

// 正确
for (int i = n - 1; i > 0; i--) {
    std::swap(arr[0], arr[i]);
    maxHeapify(arr, 0, i);  // 使用 i 作为堆大小
}
```

## 算法变体

### 1. 使用STL的堆操作
```cpp
class STLHeapSort {
public:
    static void sort(std::vector<int>& arr) {
        // 构建最大堆
        std::make_heap(arr.begin(), arr.end());
        
        // 逐个取出最大值
        for (auto it = arr.end(); it != arr.begin(); --it) {
            std::pop_heap(arr.begin(), it);
        }
    }
};
```

### 2. 优先级队列实现
```cpp
class PriorityQueueSort {
public:
    static void sort(std::vector<int>& arr) {
        std::priority_queue<int> pq;
        
        // 将所有元素加入优先级队列
        for (int num : arr) {
            pq.push(num);
        }
        
        // 逐个取出最大值
        for (int i = arr.size() - 1; i >= 0; i--) {
            arr[i] = pq.top();
            pq.pop();
        }
    }
};
```

## 优化技巧

### 1. 避免递归调用
```cpp
// 使用迭代版本避免栈溢出
static void maxHeapifyIterative(std::vector<int>& arr, int i, int heapSize) {
    while (true) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < heapSize && arr[left] > arr[largest]) {
            largest = left;
        }
        
        if (right < heapSize && arr[right] > arr[largest]) {
            largest = right;
        }
        
        if (largest == i) {
            break;
        }
        
        std::swap(arr[i], arr[largest]);
        i = largest;
    }
}
```

### 2. 小数组使用插入排序
```cpp
static void sort(std::vector<int>& arr) {
    if (arr.size() <= 10) {
        insertionSort(arr);
        return;
    }
    
    // 正常的堆排序逻辑
    // ...
}
```

## 应用场景

1. **优先级队列**：堆排序是优先级队列的基础
2. **Top K 问题**：找出数组中最大的 K 个元素
3. **外部排序**：处理无法全部加载到内存的大文件
4. **实时系统**：需要快速响应优先级变化时
5. **游戏开发**：AI 决策树、事件优先级处理

## 堆的其他操作

### 插入元素
```cpp
static void insert(std::vector<int>& heap, int value) {
    heap.push_back(value);
    int i = heap.size() - 1;
    
    // 向上调整
    while (i > 0 && heap[(i - 1) / 2] < heap[i]) {
        std::swap(heap[i], heap[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}
```

### 删除根节点
```cpp
static int extractMax(std::vector<int>& heap) {
    if (heap.empty()) {
        throw std::runtime_error("Heap is empty");
    }
    
    int max = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    
    if (!heap.empty()) {
        maxHeapify(heap, 0, heap.size());
    }
    
    return max;
}
```

## 总结

堆排序是一种高效、原地的排序算法，具有以下特点：

- **时间复杂度**：O(n log n) - 在所有情况下都稳定
- **空间复杂度**：O(1) - 原地排序
- **稳定性**：不稳定排序算法
- **适用性**：特别适合优先级队列和 Top K 问题

虽然不稳定，但堆排序的原地特性和稳定的时间复杂度使其在许多场景下都是优秀的选择，特别是在内存受限或需要优先级队列功能的场景中。 