# 二叉树遍历 (Binary Tree Traversal)

## 算法描述

二叉树遍历是指按照某种顺序访问二叉树中的所有节点。根据访问根节点的时机不同，可以分为前序遍历、中序遍历和后序遍历。此外，还有层次遍历，按照树的层级从上到下、从左到右访问节点。

**核心思想**：
- **前序遍历**：根节点 → 左子树 → 右子树
- **中序遍历**：左子树 → 根节点 → 右子树
- **后序遍历**：左子树 → 右子树 → 根节点
- **层次遍历**：按层级从上到下、从左到右访问

## 复杂度分析

| 遍历方式 | 时间复杂度 | 空间复杂度 |
|----------|------------|------------|
| 递归实现 | O(n) | O(h) - h为树的高度 |
| 非递归实现 | O(n) | O(n) |
| 层次遍历 | O(n) | O(w) - w为树的最大宽度 |

## 伪代码

```
// 前序遍历
前序遍历(节点)
    如果 节点 != 空
        访问(节点)
        前序遍历(节点.左子节点)
        前序遍历(节点.右子节点)

// 中序遍历
中序遍历(节点)
    如果 节点 != 空
        中序遍历(节点.左子节点)
        访问(节点)
        中序遍历(节点.右子节点)

// 后序遍历
后序遍历(节点)
    如果 节点 != 空
        后序遍历(节点.左子节点)
        后序遍历(节点.右子节点)
        访问(节点)

// 层次遍历
层次遍历(根节点)
    如果 根节点 == 空
        返回
    队列.入队(根节点)
    当 队列不为空
        节点 = 队列.出队()
        访问(节点)
        如果 节点.左子节点 != 空
            队列.入队(节点.左子节点)
        如果 节点.右子节点 != 空
            队列.入队(节点.右子节点)
```

## C++ 实现

### 二叉树节点定义

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <queue>

// 二叉树节点定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

### 递归实现

```cpp
class BinaryTreeTraversal {
public:
    // 前序遍历 - 递归
    static void preorderRecursive(TreeNode* root, std::vector<int>& result) {
        if (root == nullptr) return;
        
        result.push_back(root->val);  // 访问根节点
        preorderRecursive(root->left, result);   // 遍历左子树
        preorderRecursive(root->right, result);  // 遍历右子树
    }
    
    // 中序遍历 - 递归
    static void inorderRecursive(TreeNode* root, std::vector<int>& result) {
        if (root == nullptr) return;
        
        inorderRecursive(root->left, result);    // 遍历左子树
        result.push_back(root->val);  // 访问根节点
        inorderRecursive(root->right, result);   // 遍历右子树
    }
    
    // 后序遍历 - 递归
    static void postorderRecursive(TreeNode* root, std::vector<int>& result) {
        if (root == nullptr) return;
        
        postorderRecursive(root->left, result);  // 遍历左子树
        postorderRecursive(root->right, result); // 遍历右子树
        result.push_back(root->val);  // 访问根节点
    }
};
```

### 非递归实现（栈）

```cpp
class NonRecursiveTraversal {
public:
    // 前序遍历 - 非递归
    static std::vector<int> preorderIterative(TreeNode* root) {
        std::vector<int> result;
        if (root == nullptr) return result;
        
        std::stack<TreeNode*> stack;
        stack.push(root);
        
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            
            result.push_back(node->val);
            
            // 先压入右子节点，再压入左子节点
            // 这样出栈时就是左子节点先出栈
            if (node->right) {
                stack.push(node->right);
            }
            if (node->left) {
                stack.push(node->left);
            }
        }
        
        return result;
    }
    
    // 中序遍历 - 非递归
    static std::vector<int> inorderIterative(TreeNode* root) {
        std::vector<int> result;
        std::stack<TreeNode*> stack;
        TreeNode* current = root;
        
        while (current != nullptr || !stack.empty()) {
            // 一直向左走到底
            while (current != nullptr) {
                stack.push(current);
                current = current->left;
            }
            
            // 弹出栈顶元素并访问
            current = stack.top();
            stack.pop();
            result.push_back(current->val);
            
            // 转向右子树
            current = current->right;
        }
        
        return result;
    }
    
    // 后序遍历 - 非递归（使用两个栈）
    static std::vector<int> postorderIterative(TreeNode* root) {
        std::vector<int> result;
        if (root == nullptr) return result;
        
        std::stack<TreeNode*> stack1, stack2;
        stack1.push(root);
        
        // 第一个栈：根->右->左的顺序
        while (!stack1.empty()) {
            TreeNode* node = stack1.top();
            stack1.pop();
            stack2.push(node);
            
            if (node->left) {
                stack1.push(node->left);
            }
            if (node->right) {
                stack1.push(node->right);
            }
        }
        
        // 第二个栈：弹出顺序就是左->右->根
        while (!stack2.empty()) {
            result.push_back(stack2.top()->val);
            stack2.pop();
        }
        
        return result;
    }
    
    // 后序遍历 - 非递归（使用一个栈）
    static std::vector<int> postorderIterativeOneStack(TreeNode* root) {
        std::vector<int> result;
        if (root == nullptr) return result;
        
        std::stack<TreeNode*> stack;
        TreeNode* current = root;
        TreeNode* lastVisited = nullptr;
        
        while (current != nullptr || !stack.empty()) {
            // 一直向左走到底
            while (current != nullptr) {
                stack.push(current);
                current = current->left;
            }
            
            TreeNode* top = stack.top();
            
            // 如果右子树为空或已经访问过右子树
            if (top->right == nullptr || top->right == lastVisited) {
                result.push_back(top->val);
                lastVisited = top;
                stack.pop();
            } else {
                // 转向右子树
                current = top->right;
            }
        }
        
        return result;
    }
};
```

### 层次遍历

```cpp
class LevelOrderTraversal {
public:
    // 层次遍历 - 基础版本
    static std::vector<int> levelOrder(TreeNode* root) {
        std::vector<int> result;
        if (root == nullptr) return result;
        
        std::queue<TreeNode*> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();
            
            result.push_back(node->val);
            
            if (node->left) {
                queue.push(node->left);
            }
            if (node->right) {
                queue.push(node->right);
            }
        }
        
        return result;
    }
    
    // 层次遍历 - 按层返回
    static std::vector<std::vector<int>> levelOrderByLevel(TreeNode* root) {
        std::vector<std::vector<int>> result;
        if (root == nullptr) return result;
        
        std::queue<TreeNode*> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int levelSize = queue.size();
            std::vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.pop();
                
                level.push_back(node->val);
                
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
            
            result.push_back(level);
        }
        
        return result;
    }
    
    // 之字形层次遍历
    static std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
        std::vector<std::vector<int>> result;
        if (root == nullptr) return result;
        
        std::queue<TreeNode*> queue;
        queue.push(root);
        bool leftToRight = true;
        
        while (!queue.empty()) {
            int levelSize = queue.size();
            std::vector<int> level(levelSize);
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.pop();
                
                int index = leftToRight ? i : levelSize - 1 - i;
                level[index] = node->val;
                
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
            
            result.push_back(level);
            leftToRight = !leftToRight;
        }
        
        return result;
    }
};
```

### 莫里斯遍历（Morris Traversal）

```cpp
class MorrisTraversal {
public:
    // 中序遍历 - 莫里斯遍历（O(1)空间复杂度）
    static std::vector<int> inorderMorris(TreeNode* root) {
        std::vector<int> result;
        TreeNode* current = root;
        
        while (current != nullptr) {
            if (current->left == nullptr) {
                // 没有左子树，访问当前节点
                result.push_back(current->val);
                current = current->right;
            } else {
                // 找到当前节点的前驱节点
                TreeNode* predecessor = current->left;
                while (predecessor->right != nullptr && predecessor->right != current) {
                    predecessor = predecessor->right;
                }
                
                if (predecessor->right == nullptr) {
                    // 第一次访问，建立线索
                    predecessor->right = current;
                    current = current->left;
                } else {
                    // 第二次访问，恢复结构并访问当前节点
                    predecessor->right = nullptr;
                    result.push_back(current->val);
                    current = current->right;
                }
            }
        }
        
        return result;
    }
    
    // 前序遍历 - 莫里斯遍历
    static std::vector<int> preorderMorris(TreeNode* root) {
        std::vector<int> result;
        TreeNode* current = root;
        
        while (current != nullptr) {
            if (current->left == nullptr) {
                result.push_back(current->val);
                current = current->right;
            } else {
                TreeNode* predecessor = current->left;
                while (predecessor->right != nullptr && predecessor->right != current) {
                    predecessor = predecessor->right;
                }
                
                if (predecessor->right == nullptr) {
                    result.push_back(current->val);
                    predecessor->right = current;
                    current = current->left;
                } else {
                    predecessor->right = nullptr;
                    current = current->right;
                }
            }
        }
        
        return result;
    }
};
```

## 使用示例

```cpp
// 创建测试二叉树
TreeNode* createTestTree() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);
    return root;
}

int main() {
    TreeNode* root = createTestTree();
    
    // 递归遍历
    std::vector<int> preorder, inorder, postorder;
    BinaryTreeTraversal::preorderRecursive(root, preorder);
    BinaryTreeTraversal::inorderRecursive(root, inorder);
    BinaryTreeTraversal::postorderRecursive(root, postorder);
    
    std::cout << "递归前序遍历: ";
    for (int val : preorder) std::cout << val << " ";
    std::cout << std::endl;
    
    std::cout << "递归中序遍历: ";
    for (int val : inorder) std::cout << val << " ";
    std::cout << std::endl;
    
    std::cout << "递归后序遍历: ";
    for (int val : postorder) std::cout << val << " ";
    std::cout << std::endl;
    
    // 非递归遍历
    auto preorderIter = NonRecursiveTraversal::preorderIterative(root);
    auto inorderIter = NonRecursiveTraversal::inorderIterative(root);
    auto postorderIter = NonRecursiveTraversal::postorderIterative(root);
    
    std::cout << "非递归前序遍历: ";
    for (int val : preorderIter) std::cout << val << " ";
    std::cout << std::endl;
    
    // 层次遍历
    auto levelOrder = LevelOrderTraversal::levelOrder(root);
    std::cout << "层次遍历: ";
    for (int val : levelOrder) std::cout << val << " ";
    std::cout << std::endl;
    
    return 0;
}
```

## 遍历特点

### 前序遍历
- **访问顺序**：根 → 左 → 右
- **应用场景**：复制二叉树、前缀表达式
- **特点**：第一个访问的总是根节点

### 中序遍历
- **访问顺序**：左 → 根 → 右
- **应用场景**：二叉搜索树的有序输出
- **特点**：对于二叉搜索树，中序遍历得到有序序列

### 后序遍历
- **访问顺序**：左 → 右 → 根
- **应用场景**：删除二叉树、后缀表达式
- **特点**：最后一个访问的总是根节点

### 层次遍历
- **访问顺序**：按层级从上到下、从左到右
- **应用场景**：打印二叉树、计算树的高度
- **特点**：使用队列实现

## 考研重点

1. **递归实现**：掌握三种遍历的递归实现
2. **非递归实现**：重点掌握中序遍历的非递归实现
3. **层次遍历**：使用队列实现，常考按层返回
4. **莫里斯遍历**：O(1)空间复杂度的遍历方法
5. **应用场景**：理解不同遍历方式的应用场景
6. **复杂度分析**：掌握各种实现的时间空间复杂度 