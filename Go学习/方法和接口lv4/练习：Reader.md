## 练习：Reader

实现一个 `Reader` 类型，它产生一个 ASCII 字符 `'A'` 的无限流。
```go
package main

import "golang.org/x/tour/reader"

type MyReader struct{}

// TODO: 为 MyReader 添加一个 Read([]byte) (int, error) 方法。
func (mr MyReader) Read(p [] byte)(int,error){
	for i:=range p{
	p[i]='A'
	}
	return len(p),nil
}

func main() {
	reader.Validate(MyReader{})
}

```

