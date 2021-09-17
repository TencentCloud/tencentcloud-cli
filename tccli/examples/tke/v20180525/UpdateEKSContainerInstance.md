**Example 1: 更新容器实例**



Input: 

```
tccli tke UpdateEKSContainerInstance --cli-unfold-argument  \
    --Name helloworld \
    --RestartPolicy Always \
    --EksCiId eksci-123456
```

Output: 
```
{
    "Response": {
        "RequestId": "51d9ea5a-6e9e-4384-88da-84229e133246",
        "EksCiId": "eksci-rkkrzy4o"
    }
}
```

