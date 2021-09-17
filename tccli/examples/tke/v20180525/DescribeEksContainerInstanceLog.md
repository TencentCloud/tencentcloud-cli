**Example 1: 查询容器实例中容器日志**



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
        "RequestId": "xx"
    }
}
```

