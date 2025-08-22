参天大树充满生命力，根深叶茂，分枝扶疏。

它为我们展现了数据分治的生动形态。

7.1 二叉树
二叉树（binary tree）是一种非线性数据结构，代表“祖先”与“后代”之间的派生关系，体现了“一分为二”的分治逻辑。与链表类似，二叉树的基本单元是节点，每个节点包含值、左子节点引用和右子节点引用。

```cpp
二叉树节点结构体
struct TreeNode{
 int val;   // 节点值
 TreeNode *left; // 左子节点指针
 TreeNode *right; // 右子节点指针
 TreeNode(int x) : val(x),left(nullptr),right(nullptr) {}
 }
```

每个节点都有两个引用（指针），分别指向左子节点（left-child node）和右子节点（right-child node），该节点被称为这两个子节点的父节点（parent node）。当给定一个二叉树的节点时，我们将该节点的左子节点及其以下节点形成的树称为该节点的左子树（left subtree），同理可得右子树（right subtree）。

**在二叉树中，除叶节点外，其他所有节点都包含子节点和非空子树**。如图 7-1 所示，如果将“节点 2”视为父节点，则其左子节点和右子节点分别是“节点 4”和“节点 5”，左子树是“节点 4 及其以下节点形成的树”，右子树是“节点 5 及其以下节点形成的树”。[![父节点、子节点、子树](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_definition.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_definition.png)

图 7-1   父节点、子节点、子树

7.1.1二叉树常见术语
二叉树的常用术语如图 7-2 所示。
- 根节点（root node）：位于二叉树顶层的节点，没有父节点。
- 叶节点（leaf node）：没有子节点的节点，其两个指针均指向 `None` 。
- 边（edge）：连接两个节点的线段，即节点引用（指针）。
- 节点所在的层（level）：从顶至底递增，根节点所在层为 1 。
- 节点的度（degree）：节点的子节点的数量。在二叉树中，度的取值范围是 0、1、2 。
- 二叉树的高度（height）：从根节点到最远叶节点所经过的边的数量。
- 节点的深度（depth）：从根节点到该节点所经过的边的数量。
- 节点的高度（height）：从距离该节点最远的叶节点到该节点所经过的边的数量。
[![二叉树的常用术语](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_terminology.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_terminology.png)

图 7-2   二叉树的常用术语
>Tip

请注意，我们通常将“高度”和“深度”定义为“经过的边的数量”，但有些题目或教材可能会将其定义为“经过的节点的数量”。在这种情况下，高度和深度都需要加 1 。

7.1.2 二叉树基本操作
1.初始化二叉树

与链表类似，首先初始化节点，然后构建引用（指针）。
```cpp
// 初始化二叉树
// 初始化节点
TreeNode *n1 = new TreeNode(1);
TreeNode *n2 = new TreeNode(2);
TreeNode *n3 = new TreeNode(3);
TreeNode *n4 = new TreeNode(4);
TreeNode *n5 = new TreeNode(5);
// 构建节点之间的引用（指针）
n1->left = n2;
n1->right = n3;
n2->left = n4;
n2->rigth = n5;
```

2.插入与删除节点
与链表类似，在二叉树中插入与删除节点可以通过修改指针来实现。图 7-3 给出了一个示例。

[![在二叉树中插入与删除节点](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_add_remove.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_add_remove.png)图 7-3   在二叉树中插入与删除节点

```cpp
// 插入与删除节点
TreeNode* P = new TreeNode(0);
// 在n1 -> n2 中间插入节点 P
n1->left =P;
P->left = n2;
// 删除节点 P
n1->left =n2;
// 释放内存
delete P;
```

>Tip

需要注意的是，插入节点可能会改变二叉树的原有逻辑结构，而删除节点通常意味着删除该节点及其所有子树。因此，在二叉树中，插入与删除通常是由一套操作配合完成的，以实现有实际意义的操作。

7.1.3 常见二叉树类型
1.完美二叉树
如图 7-4 所示，完美二叉树（perfect binary tree）所有层的节点都被完全填满。在完美二叉树中，叶节点的度为 0 ，其余所有节点的度都为 2 ；若树的高度为 h ，则节点总数为 2的h+1次方−1 ，呈现标准的指数级关系，反映了自然界中常见的细胞分裂现象。
>Tip

请注意，在中文社区中，完美二叉树常被称为满二叉树。

[![完美二叉树](https://www.hello-algo.com/chapter_tree/binary_tree.assets/perfect_binary_tree.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/perfect_binary_tree.png)

图 7-4   完美二叉树

2.完美二叉树
如图 7-5 所示，完全二叉树（complete binary tree）仅允许最底层的节点不完全填满，且最底层的节点必须从左至右依次连续填充。请注意，完美二叉树也是一棵完全二叉树。

[![完全二叉树](https://www.hello-algo.com/chapter_tree/binary_tree.assets/complete_binary_tree.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/complete_binary_tree.png)

图 7-5   完全二叉树

3.完满二叉树

如图 7-6 所示，完满二叉树（full binary tree）除了叶节点之外，其余所有节点都有两个子节点。

[![完满二叉树](https://www.hello-algo.com/chapter_tree/binary_tree.assets/full_binary_tree.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/full_binary_tree.png)

图 7-6   完满二叉树

4.平衡二叉树
如图 7-7 所示，平衡二叉树（balanced binary tree）中任意节点的左子树和右子树的高度之差的绝对值不超过 1 。
[![平衡二叉树](https://www.hello-algo.com/chapter_tree/binary_tree.assets/balanced_binary_tree.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/balanced_binary_tree.png)

图 7-7   平衡二叉树

7.1.4 二叉树的退化
图 7-8 展示了二叉树的理想结构与退化结构。当二叉树的每层节点都被填满时，达到“完美二叉树”；而当所有节点都偏向一侧时，二叉树退化为“链表”。

- 完美二叉树是理想情况，可以充分发挥二叉树“分治”的优势。
- 链表则是另一个极端，各项操作都变为线性操作，时间复杂度退化至 O(n) 。
[![二叉树的最佳结构与最差结构](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_best_worst_cases.png)](https://www.hello-algo.com/chapter_tree/binary_tree.assets/binary_tree_best_worst_cases.png)

图 7-8   二叉树的最佳结构与最差结构
如表 7-1 所示，在最佳结构和最差结构下，二叉树的叶节点数量、节点总数、高度等达到极大值或极小值。

表 7-1   二叉树的最佳结构与最差结构

||完美二叉树|链表|
|---|---|---|
|第 i 层的节点数量|2i−1|1|
|高度为 h 的树的叶节点数量|2h|1|
|高度为 h 的树的节点总数|2h+1−1|h+1|
|节点总数为 n 的树的高度|log2⁡(n+1)−1|n−1|

7.2 二叉树遍历
从物理结构的角度来看，树是一种基于链表的数据结构，因此其遍历方式是通过指针逐个访问节点。然而，树是一种非线性数据结构，这使得遍历树比遍历链表更加复杂，需要借助搜索算法来实现。

二叉树常见的遍历方式包括层序遍历、前序遍历、中序遍历和后序遍历等。

7.2.1 层序遍历
如图 7-9 所示，层序遍历（level-order traversal）从顶部到底部逐层遍历二叉树，并在每一层按照从左到右的顺序访问节点。

层序遍历本质上属于广度优先遍历（breadth-first traversal），也称广度优先搜索（breadth-first search, BFS），它体现了一种“一圈一圈向外扩展”的逐层遍历方式。

[![二叉树的层序遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal.assets/binary_tree_bfs.png)](https://www.hello-algo.com/chapter_tree/binary_tree_traversal.assets/binary_tree_bfs.png)

图 7-9   二叉树的层序遍历

1.代码实现
广度优先遍历通常借助“队列”来实现。队列遵循“先进先出”的规则，而广度优先遍历则遵循“逐层推进”的规则，两者背后的思想是一致的。实现代码如下：
```cpp
vector<int> levelOrder(TreeNode *root){
// 初始化队列，加入根节点
queue<TreeNode *> queue;
queue.push(root);
// 初始化一个列表，用于保存遍历序列
vector<int> vec;
while(!queue.empty()){
TreeNode *node = queue.front();
queue.pop();  队列出队
vec.push_back(node->val); // 保存节点值
if(node->left !=nullptr)
queue.push(node->left); 左子节点入队
if(node->right != nullptr)
queue.push(node->right);
}
return vec;
}
```

2.复杂度分析
- **时间复杂度为 O(n)** ：所有节点被访问一次，使用 O(n) 时间，其中 n 为节点数量。
- **空间复杂度为 O(n)** ：在最差情况下，即满二叉树时，遍历到最底层之前，队列中最多同时存在 (n+1)/2 个节点，占用 O(n) 空间。

7.2.2 前序、中序、后序遍历
相应地，前序、中序和后序遍历都属于深度优先遍历（depth-first traversal），也称深度优先搜索（depth-first search, DFS），它体现了一种“先走到尽头，再回溯继续”的遍历方式。

图 7-10 展示了对二叉树进行深度优先遍历的工作原理。**深度优先遍历就像是绕着整棵二叉树的外围“走”一圈**，在每个节点都会遇到三个位置，分别对应前序遍历、中序遍历和后序遍历。
[![二叉搜索树的前序、中序、后序遍历](https://www.hello-algo.com/chapter_tree/binary_tree_traversal.assets/binary_tree_dfs.png)](https://www.hello-algo.com/chapter_tree/binary_tree_traversal.assets/binary_tree_dfs.png)

图 7-10   二叉搜索树的前序、中序、后序遍历

1.代码实现

深度优先搜索通常基于递归实现：
```cpp
// 前序遍历
void preOrder(TreeNode* root){
if(root == nullptr)
return;
// 访问优先级：根节点->左子树->右子树
vec，push_back(root->val);
preOrder(root->left);
preOrder(root->right);
}
// 中序遍历
void inOrder(TreeNode* root){
 if(root == nullptr)
 return;
 // 访问优先级: 左子树->根节点->右子树
 inOrder(root->left);
 vec.push_back(root->val);
 inOrder(root->right);
}

// 后序遍历
void postOrder(TreeNode* root){
if(root == nullptr)
return;
postOrder(root->left);
postOrder(root->right);
vec.push_back(root->val);
}
```

>Tip

深度优先搜索也可以基于迭代实现，有兴趣的读者可以自行研究。

图 7-11 展示了前序遍历二叉树的递归过程，其可分为“递”和“归”两个逆向的部分。

1. “递”表示开启新方法，程序在此过程中访问下一个节点。
2. “归”表示函数返回，代表当前节点已经访问完毕。

2 复杂度分析

- **时间复杂度为 O(n)** ：所有节点被访问一次，使用 O(n) 时间。
- **空间复杂度为 O(n)** ：在最差情况下，即树退化为链表时，递归深度达到 n ，系统占用 O(n) 栈帧空间。



7.3 二叉树数组表示
在链表表示下，二叉树的存储单元为节点 `TreeNode` ，节点之间通过指针相连接。上一节介绍了链表表示下的二叉树的各项基本操作。

那么，我们能否用数组来表示二叉树呢？答案是肯定的。

7.3.1 表示完美二叉树

先分析一个简单案例。给定一棵完美二叉树，我们将所有节点按照层序遍历的顺序存储在一个数组中，则每个节点都对应唯一的数组索引。

根据层序遍历的特性，我们可以推导出父节点索引与子节点索引之间的“映射公式”：**若某节点的索引为 i ，则该节点的左子节点索引为 2i+1 ，右子节点索引为 2i+2** 。图 7-12 展示了各个节点索引之间的映射关系。

[![完美二叉树的数组表示](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_binary_tree.png)](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_binary_tree.png)

图 7-12   完美二叉树的数组表示

**映射公式的角色相当于链表中的节点引用（指针）**。给定数组中的任意一个节点，我们都可以通过映射公式来访问它的左（右）子节点。

7.3.2 表示任意二叉树
完美二叉树是一个特例，在二叉树的中间层通常存在许多 `None` 。由于层序遍历序列并不包含这些 `None` ，因此我们无法仅凭该序列来推测 `None` 的数量和分布位置。**这意味着存在多种二叉树结构都符合该层序遍历序列**。

如图 7-13 所示，给定一棵非完美二叉树，上述数组表示方法已经失效。

[![层序遍历序列对应多种二叉树可能性](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_without_empty.png)](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_without_empty.png)

图 7-13   层序遍历序列对应多种二叉树可能性

为了解决此问题，**我们可以考虑在层序遍历序列中显式地写出所有 `None`** 。如图 7-14 所示，这样处理后，层序遍历序列就可以唯一表示二叉树了。示例代码如下：
```cpp
/* 二叉树的数组表示 */
// 使用 int 最大值 INT_MAX 标记空位
vector<int> tree = {1, 2, 3, 4, INT_MAX, 6, 7, 8, 9, INT_MAX, INT_MAX, 12, INT_MAX, INT_MAX, 15};
```
[![任意类型二叉树的数组表示](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_with_empty.png)](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_with_empty.png)

图 7-14   任意类型二叉树的数组表示

值得说明的是，**完全二叉树非常适合使用数组来表示**。回顾完全二叉树的定义，`None` 只出现在最底层且靠右的位置，**因此所有 `None` 一定出现在层序遍历序列的末尾**。

这意味着使用数组表示完全二叉树时，可以省略存储所有 `None` ，非常方便。图 7-15 给出了一个例子。
[![完全二叉树的数组表示](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_complete_binary_tree.png)](https://www.hello-algo.com/chapter_tree/array_representation_of_tree.assets/array_representation_complete_binary_tree.png)

图 7-15   完全二叉树的数组表示

以下代码实现了一棵基于数组表示的二叉树，包括以下几种操作。

- 给定某节点，获取它的值、左（右）子节点、父节点。
- 获取前序遍历、中序遍历、后序遍历、层序遍历序列。
```cpp
/* 数组表示下的二叉树类 */
class ArrayBinaryTree {
  public:
    /* 构造方法 */
    ArrayBinaryTree(vector<int> arr) {
        tree = arr;
    }

    /* 列表容量 */
    int size() {
        return tree.size();
    }

    /* 获取索引为 i 节点的值 */
    int val(int i) {
        // 若索引越界，则返回 INT_MAX ，代表空位
        if (i < 0 || i >= size())
            return INT_MAX;
        return tree[i];
    }

    /* 获取索引为 i 节点的左子节点的索引 */
    int left(int i) {
        return 2 * i + 1;
    }

    /* 获取索引为 i 节点的右子节点的索引 */
    int right(int i) {
        return 2 * i + 2;
    }

    /* 获取索引为 i 节点的父节点的索引 */
    int parent(int i) {
        return (i - 1) / 2;
    }

    /* 层序遍历 */
    vector<int> levelOrder() {
        vector<int> res;
        // 直接遍历数组
        for (int i = 0; i < size(); i++) {
            if (val(i) != INT_MAX)
                res.push_back(val(i));
        }
        return res;
    }

    /* 前序遍历 */
    vector<int> preOrder() {
        vector<int> res;
        dfs(0, "pre", res);
        return res;
    }

    /* 中序遍历 */
    vector<int> inOrder() {
        vector<int> res;
        dfs(0, "in", res);
        return res;
    }

    /* 后序遍历 */
    vector<int> postOrder() {
        vector<int> res;
        dfs(0, "post", res);
        return res;
    }

  private:
    vector<int> tree;

    /* 深度优先遍历 */
    void dfs(int i, string order, vector<int> &res) {
        // 若为空位，则返回
        if (val(i) == INT_MAX)
            return;
        // 前序遍历
        if (order == "pre")
            res.push_back(val(i));
        dfs(left(i), order, res);
        // 中序遍历
        if (order == "in")
            res.push_back(val(i));
        dfs(right(i), order, res);
        // 后序遍历
        if (order == "post")
            res.push_back(val(i));
    }
};
```

7.3.3 优点与局限性
二叉树的数组表示主要有以下优点。

- 数组存储在连续的内存空间中，对缓存友好，访问与遍历速度较快。
- 不需要存储指针，比较节省空间。
- 允许随机访问节点。

然而，数组表示也存在一些局限性。

- 数组存储需要连续内存空间，因此不适合存储数据量过大的树。
- 增删节点需要通过数组插入与删除操作实现，效率较低。
- 当二叉树中存在大量 `None` 时，数组中包含的节点数据比重较低，空间利用率较低。

7.4 二叉搜索树
如图 7-16 所示，二叉搜索树（binary search tree）满足以下条件。

1. 对于根节点，左子树中所有节点的值 < 根节点的值 < 右子树中所有节点的值。
2. 任意节点的左、右子树也是二叉搜索树，即同样满足条件 `1.` 。
[![二叉搜索树](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/binary_search_tree.png)](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/binary_search_tree.png)

图 7-16   二叉搜索树

7.4.1 二叉搜索树的操作
我们将二叉搜索树封装为一个类 `BinarySearchTree` ，并声明一个成员变量 `root` ，指向树的根节点。

1.查找节点
给定目标节点值 `num` ，可以根据二叉搜索树的性质来查找。如图 7-17 所示，我们声明一个节点 `cur` ，从二叉树的根节点 `root` 出发，循环比较节点值 `cur.val` 和 `num` 之间的大小关系。

- 若 `cur.val < num` ，说明目标节点在 `cur` 的右子树中，因此执行 `cur = cur.right` 。
- 若 `cur.val > num` ，说明目标节点在 `cur` 的左子树中，因此执行 `cur = cur.left` 。
- 若 `cur.val = num` ，说明找到目标节点，跳出循环并返回该节点。
二叉搜索树的查找操作与二分查找算法的工作原理一致，都是每轮排除一半情况。循环次数最多为二叉树的高度，当二叉树平衡时，使用 O(log⁡n) 时间。示例代码如下：
```cpp
// 查找节点
TreeNode* search(int num){
TreeNode *cur = root;
// 循环查找，越过叶节点后跳出
while(cur!=nullptr){
// 目标节点在cur的右子树中
if(cur->val<num)
cur=cur->right;
// 目标节点在cur的左子树
else if(cur->val>num)
cur=cur->left;
// 找到目标节点，跳出循环
else
break;
}
// 返回目标节点
return cur;
}
```

2.插入节点
给定一个待插入元素 `num` ，为了保持二叉搜索树“左子树 < 根节点 < 右子树”的性质，插入操作流程如图 7-18 所示。

1. **查找插入位置**：与查找操作相似，从根节点出发，根据当前节点值和 `num` 的大小关系循环向下搜索，直到越过叶节点（遍历至 `None` ）时跳出循环。
2. **在该位置插入节点**：初始化节点 `num` ，将该节点置于 `None` 的位置。

[![在二叉搜索树中插入节点](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_insert.png)](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_insert.png)

图 7-18   在二叉搜索树中插入节点

在代码实现中，需要注意以下两点。

- 二叉搜索树不允许存在重复节点，否则将违反其定义。因此，若待插入节点在树中已存在，则不执行插入，直接返回。
- 为了实现插入节点，我们需要借助节点 `pre` 保存上一轮循环的节点。这样在遍历至 `None` 时，我们可以获取到其父节点，从而完成节点插入操作。
```cpp
void insert(int num){
// 若树为空，则初始化根节点
if(root==nullptr){
root = new TreeNode(num);
return;
}
TreeNode* cur = root,*pre = nullptr;
// 循环查找，越过叶节点后跳出
while(cur!=nullptr){
// 找到重复节点，直接返回
if(cur->val==num)
return;
pre = cur;
// 插入位置在cur的右子树中
if(cur->val<num)
cur=cur->right;
//插入位置在cur的左子树中
else
cur=cur->left;
}

// 插入节点
TreeNode* node = new TreeNode(num);
if(pre->val<num)
pre->right=node;
else
pre->left=node;
}
```

3.删除节点
先在二叉树中查找到目标节点，再将其删除。与插入节点类似，我们需要保证在删除操作完成后，二叉搜索树的“左子树 < 根节点 < 右子树”的性质仍然满足。因此，我们根据目标节点的子节点数量，分 0、1 和 2 三种情况，执行对应的删除节点操作。

如图 7-19 所示，当待删除节点的度为 0 时，表示该节点是叶节点，可以直接删除。

[![在二叉搜索树中删除节点（度为 0 ）](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_remove_case1.png)](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_remove_case1.png)

图 7-19   在二叉搜索树中删除节点（度为 0 ）

如图 7-20 所示，当待删除节点的度为 1 时，将待删除节点替换为其子节点即可。

[![在二叉搜索树中删除节点（度为 1 ）](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_remove_case2.png)](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_remove_case2.png)

图 7-20   在二叉搜索树中删除节点（度为 1 ）

当待删除节点的度为 2 时，我们无法直接删除它，而需要使用一个节点替换该节点。由于要保持二叉搜索树“左子树 < 根节点 < 右子树”的性质，**因此这个节点可以是右子树的最小节点或左子树的最大节点**。

假设我们选择右子树的最小节点（中序遍历的下一个节点），则删除操作流程如图 7-21 所示。

1. 找到待删除节点在“中序遍历序列”中的下一个节点，记为 `tmp` 。
2. 用 `tmp` 的值覆盖待删除节点的值，并在树中递归删除节点 `tmp` 。

```cpp
/* 删除节点 */
void remove(int num) {
    // 若树为空，直接提前返回
    if (root == nullptr)
        return;
    TreeNode *cur = root, *pre = nullptr;
    // 循环查找，越过叶节点后跳出
    while (cur != nullptr) {
        // 找到待删除节点，跳出循环
        if (cur->val == num)
            break;
        pre = cur;
        // 待删除节点在 cur 的右子树中
        if (cur->val < num)
            cur = cur->right;
        // 待删除节点在 cur 的左子树中
        else
            cur = cur->left;
    }
    // 若无待删除节点，则直接返回
    if (cur == nullptr)
        return;
    // 子节点数量 = 0 or 1
    if (cur->left == nullptr || cur->right == nullptr) {
        // 当子节点数量 = 0 / 1 时， child = nullptr / 该子节点
        TreeNode *child = cur->left != nullptr ? cur->left : cur->right;
        // 删除节点 cur
        if (cur != root) {
            if (pre->left == cur)
                pre->left = child;
            else
                pre->right = child;
        } else {
            // 若删除节点为根节点，则重新指定根节点
            root = child;
        }
        // 释放内存
        delete cur;
    }
    // 子节点数量 = 2
    else {
        // 获取中序遍历中 cur 的下一个节点
        TreeNode *tmp = cur->right;
        while (tmp->left != nullptr) {
            tmp = tmp->left;
        }
        int tmpVal = tmp->val;
        // 递归删除节点 tmp
        remove(tmp->val);
        // 用 tmp 覆盖 cur
        cur->val = tmpVal;
    }
}
```
4.中序遍历有序
如图 7-22 所示，二叉树的中序遍历遵循“左 → 根 → 右”的遍历顺序，而二叉搜索树满足“左子节点 < 根节点 < 右子节点”的大小关系。

这意味着在二叉搜索树中进行中序遍历时，总是会优先遍历下一个最小节点，从而得出一个重要性质：**二叉搜索树的中序遍历序列是升序的**。

利用中序遍历升序的性质，我们在二叉搜索树中获取有序数据仅需 O(n) 时间，无须进行额外的排序操作，非常高效。

[![二叉搜索树的中序遍历序列](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_inorder_traversal.png)](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_inorder_traversal.png)

图 7-22   二叉搜索树的中序遍历序列

7.4.2 二叉搜索树的效率
给定一组数据，我们考虑使用数组或二叉搜索树存储。观察表 7-2 ，二叉搜索树的各项操作的时间复杂度都是对数阶，具有稳定且高效的性能。只有在高频添加、低频查找删除数据的场景下，数组比二叉搜索树的效率更高。

表 7-2   数组与搜索树的效率对比

||无序数组|二叉搜索树|
|---|---|---|
|查找元素|O(n)|O(log⁡n)|
|插入元素|O(1)|O(log⁡n)|
|删除元素|O(n)|O(log⁡n)|

在理想情况下，二叉搜索树是“平衡”的，这样就可以在 log⁡n 轮循环内查找任意节点。

然而，如果我们在二叉搜索树中不断地插入和删除节点，可能导致二叉树退化为图 7-23 所示的链表，这时各种操作的时间复杂度也会退化为 O(n) 。

[![二叉搜索树退化](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_degradation.png)](https://www.hello-algo.com/chapter_tree/binary_search_tree.assets/bst_degradation.png)

图 7-23   二叉搜索树退化

7.4.3 二叉搜索树常见应用
- 用作系统中的多级索引，实现高效的查找、插入、删除操作。
- 作为某些搜索算法的底层数据结构。
- 用于存储数据流，以保持其有序状态。
# 7.6   小结

### 1.   重点回顾[¶](https://www.hello-algo.com/chapter_tree/summary/#1 "Permanent link")

- 二叉树是一种非线性数据结构，体现“一分为二”的分治逻辑。每个二叉树节点包含一个值以及两个指针，分别指向其左子节点和右子节点。
- 对于二叉树中的某个节点，其左（右）子节点及其以下形成的树被称为该节点的左（右）子树。
- 二叉树的相关术语包括根节点、叶节点、层、度、边、高度和深度等。
- 二叉树的初始化、节点插入和节点删除操作与链表操作方法类似。
- 常见的二叉树类型有完美二叉树、完全二叉树、完满二叉树和平衡二叉树。完美二叉树是最理想的状态，而链表是退化后的最差状态。
- 二叉树可以用数组表示，方法是将节点值和空位按层序遍历顺序排列，并根据父节点与子节点之间的索引映射关系来实现指针。
- 二叉树的层序遍历是一种广度优先搜索方法，它体现了“一圈一圈向外扩展”的逐层遍历方式，通常通过队列来实现。
- 前序、中序、后序遍历皆属于深度优先搜索，它们体现了“先走到尽头，再回溯继续”的遍历方式，通常使用递归来实现。
- 二叉搜索树是一种高效的元素查找数据结构，其查找、插入和删除操作的时间复杂度均为 O(log⁡n) 。当二叉搜索树退化为链表时，各项时间复杂度会劣化至 O(n) 。
- AVL 树，也称平衡二叉搜索树，它通过旋转操作确保在不断插入和删除节点后树仍然保持平衡。
- AVL 树的旋转操作包括右旋、左旋、先右旋再左旋、先左旋再右旋。在插入或删除节点后，AVL 树会从底向顶执行旋转操作，使树重新恢复平衡。

### 2.   Q & A[¶](https://www.hello-algo.com/chapter_tree/summary/#2-q-a "Permanent link")

**Q**：对于只有一个节点的二叉树，树的高度和根节点的深度都是 0 吗？

是的，因为高度和深度通常定义为“经过的边的数量”。

**Q**：二叉树中的插入与删除一般由一套操作配合完成，这里的“一套操作”指什么呢？可以理解为资源的子节点的资源释放吗？

拿二叉搜索树来举例，删除节点操作要分三种情况处理，其中每种情况都需要进行多个步骤的节点操作。

**Q**：为什么 DFS 遍历二叉树有前、中、后三种顺序，分别有什么用呢？

与顺序和逆序遍历数组类似，前序、中序、后序遍历是三种二叉树遍历方法，我们可以使用它们得到一个特定顺序的遍历结果。例如在二叉搜索树中，由于节点大小满足 `左子节点值 < 根节点值 < 右子节点值` ，因此我们只要按照“左 → 根 → 右”的优先级遍历树，就可以获得有序的节点序列。

**Q**：右旋操作是处理失衡节点 `node`、`child`、`grand_child` 之间的关系，那 `node` 的父节点和 `node` 原来的连接不需要维护吗？右旋操作后岂不是断掉了？

我们需要从递归的视角来看这个问题。右旋操作 `right_rotate(root)` 传入的是子树的根节点，最终 `return child` 返回旋转之后的子树的根节点。子树的根节点和其父节点的连接是在该函数返回后完成的，不属于右旋操作的维护范围。

**Q**：在 C++ 中，函数被划分到 `private` 和 `public` 中，这方面有什么考量吗？为什么要将 `height()` 函数和 `updateHeight()` 函数分别放在 `public` 和 `private` 中呢？

主要看方法的使用范围，如果方法只在类内部使用，那么就设计为 `private` 。例如，用户单独调用 `updateHeight()` 是没有意义的，它只是插入、删除操作中的一步。而 `height()` 是访问节点高度，类似于 `vector.size()` ，因此设置成 `public` 以便使用。

**Q**：如何从一组输入数据构建一棵二叉搜索树？根节点的选择是不是很重要？

是的，构建树的方法已在二叉搜索树代码中的 `build_tree()` 方法中给出。至于根节点的选择，我们通常会将输入数据排序，然后将中点元素作为根节点，再递归地构建左右子树。这样做可以最大程度保证树的平衡性。

**Q**：在 Java 中，字符串对比是否一定要用 `equals()` 方法？

在 Java 中，对于基本数据类型，`==` 用于对比两个变量的值是否相等。对于引用类型，两种符号的工作原理是不同的。

- `==` ：用来比较两个变量是否指向同一个对象，即它们在内存中的位置是否相同。
- `equals()`：用来对比两个对象的值是否相等。

因此，如果要对比值，我们应该使用 `equals()` 。然而，通过 `String a = "hi"; String b = "hi";` 初始化的字符串都存储在字符串常量池中，它们指向同一个对象，因此也可以用 `a == b` 来比较两个字符串的内容。

**Q**：广度优先遍历到最底层之前，队列中的节点数量是 2h 吗？

是的，例如高度 h=2 的满二叉树，其节点总数 n=7 ，则底层节点数量 4=2h=(n+1)/2 。