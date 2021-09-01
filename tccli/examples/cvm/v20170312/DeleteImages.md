**Example 1: 删除一个镜像**

删除一个镜像img-34vaef8fe， 当这个镜像处于使用中或者镜像Id不存在时不采取操作并返回错误码。

Input: 

```
tccli cvm DeleteImages --cli-unfold-argument  \
    --ImageIds img-34vaef8fe
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

