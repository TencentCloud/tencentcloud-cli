**Example 1: 查询用户仓库的项目空间列表**



Input: 

```
tccli tcss DescribeImageRegistryNamespaceList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TotalCount": 2,
        "NamespaceList": [
            "online",
            "test"
        ]
    }
}
```

