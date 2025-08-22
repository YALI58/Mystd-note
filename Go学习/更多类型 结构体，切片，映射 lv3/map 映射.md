## map 映射

`map` 映射将键映射到值。

映射的零值为 `nil` 。`nil` 映射既没有键，也不能添加键。

`make` 函数会返回给定类型的映射，并将其初始化备用。


```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}

```
### 类型解释：`map[string]Vertex`

- **键（key）** 是 `string` 类型（比如 `"Bell Labs"`）
- **值（value）** 是 `Vertex` 类型（就是上面定义的经纬度结构）

👉 所以这个 map 可以用来：

> 把一个名字（字符串） → 对应的地理位置（经纬度）

⚠️ 注意：这里只是**声明了变量 `m`**，但还没有创建实际的 map！  
此时 `m` 是 `nil`（空的），还不能用。