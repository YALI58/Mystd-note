# 二分查找（Binary Search）

## 1. 算法描述

二分查找是一种在有序数组中查找特定元素的高效算法。通过将搜索范围不断减半，最终找到目标元素或确定其不存在。

### 1.1 适用场景
- 在有序数组中查找特定元素
- 考研中常用于考察分治思想和边界处理
- 时间复杂度要求较高的查找问题

### 1.2 复杂度分析
| 指标            | 值               |
|-----------------|------------------|
| 时间复杂度      | O(log n)         |
| 空间复杂度      | O(1)             |
| 前提条件        | 数组必须有序     |

---

## 2. 伪代码

```
二分查找(数组, 目标值):
    左边界 = 0
    右边界 = 数组.长度 - 1
    
    当 左边界 <= 右边界:
        中点 = 左边界 + (右边界 - 左边界) / 2
        
        如果 数组[中点] == 目标值:
            返回 中点
        否则如果 数组[中点] < 目标值:
            左边界 = 中点 + 1
        否则:
            右边界 = 中点 - 1
    
    返回 -1  // 未找到
```

---

## 3. C++ 实现

```cpp
#include <vector>
#include <iostream>

// 二分查找函数
int BinarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        // 避免整数溢出的写法
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;  // 找到目标值
        } else if (arr[mid] < target) {
            left = mid + 1;  // 在右半部分查找
        } else {
            right = mid - 1;  // 在左半部分查找
        }
    }
    
    return -1;  // 未找到目标值
}

// 测试函数
void TestBinarySearch() {
    std::vector<int> arr = {1, 3, 5, 7, 9, 11, 13, 15};
    int target = 7;
    
    std::cout << "数组：";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    int result = BinarySearch(arr, target);
    if (result != -1) {
        std::cout << "找到目标值 " << target << " 在位置 " << result << std::endl;
    } else {
        std::cout << "未找到目标值 " << target << std::endl;
    }
}

int main() {
    TestBinarySearch();
    return 0;
}
```

---

## 4. 注意事项

- **数组必须有序**：二分查找的前提是数组已经排序
- **整数溢出**：使用 `left + (right - left) / 2` 而不是 `(left + right) / 2` 避免溢出
- **边界条件**：注意 `left <= right` 的循环条件
- **考研重点**：理解二分查找的核心思想和边界处理

---

## 5. 测试用例

### 5.1 典型用例
- 输入：`{1, 3, 5, 7, 9, 11, 13, 15}`, target = 7
- 输出：3

### 5.2 边界用例
- 输入：`{1, 2, 3}`, target = 1 (第一个元素)
- 输出：0
- 输入：`{1, 2, 3}`, target = 3 (最后一个元素)
- 输出：2
- 输入：`{1, 2, 3}`, target = 4 (不存在)
- 输出：-1

---

## 6. 常见错误与陷阱

- **数组未排序**：忘记检查数组是否有序
- **整数溢出**：使用 `(left + right) / 2` 可能导致溢出
- **边界错误**：循环条件写错或更新边界时出错
- **考研易错点**：不理解二分查找的终止条件和边界更新逻辑

---

## 7. 变种算法

### 7.1 查找第一个等于目标值的位置
```cpp
int BinarySearchFirst(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] >= target) {
            if (arr[mid] == target) {
                result = mid;
            }
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return result;
}
```

### 7.2 查找最后一个等于目标值的位置
```cpp
int BinarySearchLast(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] <= target) {
            if (arr[mid] == target) {
                result = mid;
            }
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

---

通过以上内容，考研学生可以全面理解二分查找的原理、实现和变种算法，掌握分治思想在查找中的应用。 