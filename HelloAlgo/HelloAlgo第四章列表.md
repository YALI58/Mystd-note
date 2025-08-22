4.3列表
列表（list）是一个抽象的数据结构概念，它表示元素的有序集合，支持元素访问、修改、添加、删除和遍历等操作，无须使用者考虑容量限制的问题。列表可以基于链表或数组实现。

- 链表天然可以看作一个列表，其支持元素增删查改操作，并且可以灵活动态扩容。
- 数组也支持元素增删查改，但由于其长度不可变，因此只能看作一个具有长度限制的列表。

当使用数组实现列表时，**长度不可变的性质会导致列表的实用性降低**。这是因为我们通常无法事先确定需要存储多少数据，从而难以选择合适的列表长度。若长度过小，则很可能无法满足使用需求；若长度过大，则会造成内存空间浪费。

为解决此问题，我们可以使用动态数组（dynamic array）来实现列表。它继承了数组的各项优点，并且可以在程序运行过程中进行动态扩容。

实际上，**许多编程语言中的标准库提供的列表是基于动态数组实现的**，例如 Python 中的 `list` 、Java 中的 `ArrayList` 、C++ 中的 `vector` 和 C# 中的 `List` 等。在接下来的讨论中，我们将把“列表”和“动态数组”视为等同的概念。

4.3.1 列表常用操作
1.初始化列表
我们通常使用“无初始值”和“有初始值”这两种初始化方法：
```cpp
// 无初始值
vector<int> nums;
// 有初始值
vector<int>nums={1,2,3};
```
2.访问元素
列表本质上是数组，因此可以在O(1)时间内访问和更新元素，效率很高。
```cpp
int num = nums[1];
// 更新元素
nums[1] = 0;
```
3.插入与删除元素
相较于数组，列表可以自由地添加与删除元素。在列表尾部添加元素的时间复杂度为O(1),但插入和删除元素的效率仍与数组相同，时间复杂度为O(n)。
```cpp
nums.clear();
// 在尾部添加元素
nums.push_back(1);
nums.push_back(2);
nums.push_back(3);
nums.push_back(4);
nums.push_back(5);
// 在中间插入元素
nums.insert(nums.begin()+3,6); // 在索引3处插入6
// 删除元素
nums.erase(nums.begin()+3);
```

4.遍历链表
与数组一样，列表可以根据索引遍历，也可以直接遍历各元素。
```cpp
// 通过索引遍历列表
int count = 0;
for(int i = 0;i<nums.size();i++){
   count+=nums[i];
}
count = 0;
for(int num :nums){
count+=num;
}
```

5.拼接列表
给定一个新列表nums1,我们可以将其拼接到原列表的尾部。
```cpp
// 拼接来个列表
vector<int> nums1= {6,7,8,9};
// 将列表nums1 拼接到nums之后
nums.insert(nums.end(),nums1.begin()，nums1.end());
```
6.排序列表
完成列表排序后，我们便可以使用在数组类算法题中经常考查的“二分查找”和“双指针”算法。
```cpp
sort(nums.begin(),nums.end());
```
4,.3.2 列表实现
许多编程语言内置了列表，例如 Java、C++、Python 等。它们的实现比较复杂，各个参数的设定也非常考究，例如初始容量、扩容倍数等。感兴趣的读者可以查阅源码进行学习。

为了加深对列表工作原理的理解，我们尝试实现一个简易版列表，包括以下三个重点设计。

- **初始容量**：选取一个合理的数组初始容量。在本示例中，我们选择 10 作为初始容量。
- **数量记录**：声明一个变量 `size` ，用于记录列表当前元素数量，并随着元素插入和删除实时更新。根据此变量，我们可以定位列表尾部，以及判断是否需要扩容。
- **扩容机制**：若插入元素时列表容量已满，则需要进行扩容。先根据扩容倍数创建一个更大的数组，再将当前数组的所有元素依次移动至新数组。在本示例中，我们规定每次将数组扩容至之前的 2 倍。
```cpp
class MyList{
private:
int *arr;
int arrCapacity=10;
int arrSize=0;        // 列表长度（当前元素数量）
int extendRatio = 2;
public:
MyList(){
arr = new int[arrCapacity];
}
~MyList(){
delete[] arr;
}
int size(){
return arrSize;
}
int capacity(){
return arrCapacity;
}
int get(int index){
// 索引如果越界，则抛出异常
if(index<0||index>=size())
throw out_of_range("索引越界")
return arr[index];
}

void set(int index,int num){
if(index<0||index>=size())
throw out_of_range("索引越界")；
arr[index]= num;
}

void add(int nnum){
if(size()==capacity())
	extendCapacity();
arr[size()]=num;
arrSize++;
}

void insert(int index,int num){
if(index<0||index>=size())
throw out_of_range("索引越界");
if(size()==capacity())
extendCapacity();
for(int j = size()-1;j>=index;j--){
arr[j+1]=arr[j];
}
arr[index]=num;
arrSize++;
}

int remove(int index){
if(index<0||index>=size())
throw out_of_range("索引越界");
int num=arr[index];
for(int j =index;j<size()-1;j++){
arr[j]=arr[j+1]
}
arrSize--;
return num;
}

void extendCapacity(){
int newCapacity=capacity()*extendRatio;
int *tmp = arr;
arr = new int[newCapacity];
for(int i=0;i<size();i++){
arr[i]=tmp[i];
}
delete[] tmp;
arrCapacity = newCapacity;
}

vector<int> toVector(){
vector<int> vec(size());
for(int i=0;i<size();i++){
vec[i]=arr[i];
}
return vec;
}
}
```
