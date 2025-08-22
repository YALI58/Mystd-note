# 哈希查找 (Hash Search)

## 算法描述

哈希查找是一种基于哈希表的查找算法，通过哈希函数将关键字映射到数组的特定位置，实现快速查找。哈希表是一种以键值对形式存储数据的数据结构，支持高效的插入、删除和查找操作。

**核心思想**：
- **哈希函数**：将关键字映射到数组索引
- **冲突解决**：处理不同关键字映射到同一位置的情况
- **动态扩容**：当负载因子过高时重新分配空间
- **快速访问**：平均情况下 O(1) 的查找时间

## 复杂度分析

| 操作 | 平均时间复杂度 | 最坏时间复杂度 | 空间复杂度 |
|------|----------------|----------------|------------|
| 查找 | O(1) | O(n) | O(n) |
| 插入 | O(1) | O(n) | O(n) |
| 删除 | O(1) | O(n) | O(n) |

**负载因子**：α = n/m，其中 n 是元素个数，m 是哈希表大小

## 伪代码

```
哈希查找(哈希表, 关键字)
    i = 0
    重复
        j = 哈希函数(关键字, i)
        如果 哈希表[j] == 空
            返回 空
        否则如果 哈希表[j].键 == 关键字
            返回 哈希表[j]
        否则 i = i + 1
    直到 i == 表大小
    错误 "哈希表溢出"

哈希插入(哈希表, 元素)
    i = 0
    重复
        j = 哈希函数(元素.键, i)
        如果 哈希表[j] == 空
            哈希表[j] = 元素
            返回 j
        否则 i = i + 1
    直到 i == 表大小
    错误 "哈希表溢出"
```

## C++ 实现

### 基础哈希表实现（链地址法）

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <string>

template<typename K, typename V>
class HashTable {
private:
    struct Node {
        K key;
        V value;
        Node(K k, V v) : key(k), value(v) {}
    };
    
    std::vector<std::list<Node>> table;
    size_t size;
    size_t capacity;
    static constexpr double LOAD_FACTOR_THRESHOLD = 0.75;
    
    // 哈希函数
    size_t hashFunction(const K& key) const {
        return std::hash<K>{}(key) % capacity;
    }
    
    // 重新哈希
    void rehash() {
        std::vector<std::list<Node>> oldTable = table;
        capacity *= 2;
        table.clear();
        table.resize(capacity);
        size = 0;
        
        for (const auto& bucket : oldTable) {
            for (const auto& node : bucket) {
                insert(node.key, node.value);
            }
        }
    }
    
public:
    HashTable(size_t initialCapacity = 16) 
        : capacity(initialCapacity), size(0) {
        table.resize(capacity);
    }
    
    // 插入键值对
    void insert(const K& key, const V& value) {
        if (static_cast<double>(size) / capacity >= LOAD_FACTOR_THRESHOLD) {
            rehash();
        }
        
        size_t index = hashFunction(key);
        
        // 检查是否已存在相同的键
        for (auto& node : table[index]) {
            if (node.key == key) {
                node.value = value;  // 更新值
                return;
            }
        }
        
        // 插入新节点
        table[index].emplace_back(key, value);
        size++;
    }
    
    // 查找值
    V* find(const K& key) {
        size_t index = hashFunction(key);
        
        for (auto& node : table[index]) {
            if (node.key == key) {
                return &node.value;
            }
        }
        
        return nullptr;  // 未找到
    }
    
    // 删除键值对
    bool remove(const K& key) {
        size_t index = hashFunction(key);
        
        auto& bucket = table[index];
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->key == key) {
                bucket.erase(it);
                size--;
                return true;
            }
        }
        
        return false;  // 未找到要删除的键
    }
    
    // 获取大小
    size_t getSize() const {
        return size;
    }
    
    // 检查是否为空
    bool isEmpty() const {
        return size == 0;
    }
};
```

### 开放定址法实现

```cpp
template<typename K, typename V>
class OpenAddressingHashTable {
private:
    struct Entry {
        K key;
        V value;
        bool isOccupied;
        bool isDeleted;
        
        Entry() : isOccupied(false), isDeleted(false) {}
        Entry(const K& k, const V& v) : key(k), value(v), isOccupied(true), isDeleted(false) {}
    };
    
    std::vector<Entry> table;
    size_t size;
    size_t capacity;
    static constexpr double LOAD_FACTOR_THRESHOLD = 0.7;
    
    // 线性探测哈希函数
    size_t hashFunction(const K& key, size_t i) const {
        return (std::hash<K>{}(key) + i) % capacity;
    }
    
    // 二次探测哈希函数
    size_t quadraticHashFunction(const K& key, size_t i) const {
        return (std::hash<K>{}(key) + i * i) % capacity;
    }
    
    // 双重哈希函数
    size_t doubleHashFunction(const K& key, size_t i) const {
        size_t h1 = std::hash<K>{}(key);
        size_t h2 = 1 + (h1 % (capacity - 1));
        return (h1 + i * h2) % capacity;
    }
    
    void rehash() {
        std::vector<Entry> oldTable = table;
        capacity *= 2;
        table.clear();
        table.resize(capacity);
        size = 0;
        
        for (const auto& entry : oldTable) {
            if (entry.isOccupied && !entry.isDeleted) {
                insert(entry.key, entry.value);
            }
        }
    }
    
public:
    OpenAddressingHashTable(size_t initialCapacity = 16) 
        : capacity(initialCapacity), size(0) {
        table.resize(capacity);
    }
    
    // 插入键值对
    bool insert(const K& key, const V& value) {
        if (static_cast<double>(size) / capacity >= LOAD_FACTOR_THRESHOLD) {
            rehash();
        }
        
        for (size_t i = 0; i < capacity; i++) {
            size_t index = hashFunction(key, i);
            
            if (!table[index].isOccupied || table[index].isDeleted) {
                table[index] = Entry(key, value);
                size++;
                return true;
            } else if (table[index].key == key) {
                table[index].value = value;  // 更新值
                return true;
            }
        }
        
        return false;  // 表已满
    }
    
    // 查找值
    V* find(const K& key) {
        for (size_t i = 0; i < capacity; i++) {
            size_t index = hashFunction(key, i);
            
            if (!table[index].isOccupied) {
                return nullptr;  // 未找到
            } else if (!table[index].isDeleted && table[index].key == key) {
                return &table[index].value;
            }
        }
        
        return nullptr;
    }
    
    // 删除键值对
    bool remove(const K& key) {
        for (size_t i = 0; i < capacity; i++) {
            size_t index = hashFunction(key, i);
            
            if (!table[index].isOccupied) {
                return false;  // 未找到
            } else if (!table[index].isDeleted && table[index].key == key) {
                table[index].isDeleted = true;
                size--;
                return true;
            }
        }
        
        return false;
    }
    
    size_t getSize() const {
        return size;
    }
    
    bool isEmpty() const {
        return size == 0;
    }
};
```

### 字符串哈希函数实现

```cpp
class StringHashTable {
private:
    static constexpr size_t BASE = 31;
    static constexpr size_t MOD = 1000000007;
    
    // 字符串哈希函数
    size_t hashString(const std::string& str) const {
        size_t hash = 0;
        size_t power = 1;
        
        for (char c : str) {
            hash = (hash + (c - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;
        }
        
        return hash;
    }
    
    std::vector<std::list<std::pair<std::string, int>>> table;
    size_t capacity;
    
public:
    StringHashTable(size_t initialCapacity = 100) : capacity(initialCapacity) {
        table.resize(capacity);
    }
    
    void insert(const std::string& key, int value) {
        size_t index = hashString(key) % capacity;
        
        // 检查是否已存在
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        
        table[index].emplace_back(key, value);
    }
    
    int* find(const std::string& key) {
        size_t index = hashString(key) % capacity;
        
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                return &pair.second;
            }
        }
        
        return nullptr;
    }
};
```

## 使用示例

```cpp
int main() {
    // 基础哈希表使用
    HashTable<std::string, int> hashTable;
    
    // 插入数据
    hashTable.insert("apple", 1);
    hashTable.insert("banana", 2);
    hashTable.insert("cherry", 3);
    
    // 查找数据
    int* value = hashTable.find("apple");
    if (value) {
        std::cout << "apple: " << *value << std::endl;
    }
    
    // 删除数据
    hashTable.remove("banana");
    
    // 开放定址法哈希表
    OpenAddressingHashTable<int, std::string> openHashTable;
    
    openHashTable.insert(1, "one");
    openHashTable.insert(2, "two");
    
    std::string* result = openHashTable.find(1);
    if (result) {
        std::cout << "1: " << *result << std::endl;
    }
    
    return 0;
}
```

## 哈希函数设计

### 好的哈希函数特点
1. **均匀分布**：将关键字均匀分布到哈希表中
2. **计算简单**：计算速度快
3. **冲突少**：减少不同关键字映射到同一位置的概率

### 常用哈希函数
1. **除留余数法**：h(k) = k mod m
2. **乘法哈希**：h(k) = ⌊m(kA mod 1)⌋
3. **全域哈希**：随机选择哈希函数

## 冲突解决方法

### 1. 链地址法（Separate Chaining）
- 使用链表存储冲突的元素
- 优点：简单，删除操作容易
- 缺点：需要额外的指针空间

### 2. 开放定址法（Open Addressing）
- **线性探测**：h(k,i) = (h(k) + i) mod m
- **二次探测**：h(k,i) = (h(k) + i²) mod m
- **双重哈希**：h(k,i) = (h₁(k) + i·h₂(k)) mod m

## 算法特点

### 优点
1. **查找效率高**：平均情况下 O(1) 查找时间
2. **插入删除快**：支持高效的动态操作
3. **空间利用率高**：负载因子可调

### 缺点
1. **最坏情况**：所有元素哈希到同一位置时效率低
2. **无序性**：不保持元素的插入顺序
3. **内存开销**：需要额外的空间存储哈希表

## 考研重点

1. **哈希函数设计**：理解好的哈希函数的特点
2. **冲突解决**：掌握各种冲突解决方法
3. **负载因子**：理解负载因子对性能的影响
4. **复杂度分析**：分析各种情况下的时间复杂度
5. **实现细节**：能够手写简单的哈希表实现 