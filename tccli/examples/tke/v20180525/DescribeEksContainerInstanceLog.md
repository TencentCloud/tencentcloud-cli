**Example 1: 查询容器实例中容器日志**

查询容器实例中容器日志

Input: 

```
tccli tke DescribeEksContainerInstanceLog --cli-unfold-argument  \
    --EksCiId eksci-123456 \
    --Tail 500 \
    --Previous False \
    --ContainerName simple-cputest
```

Output: 
```
{
    "Response": {
        "ContainerName": "simple-cputest",
        "LogContent": "hello world",
        "RequestId": "5f792091-66a7-40fc-8043-4d8b9537faiu"
    }
}
```

