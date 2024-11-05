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
        "NamespaceDetail": [
            {
                "ImageCnt": 54,
                "Namespace": "os_images",
                "RegistryCnt": 1,
                "RiskImageCnt": 50
            }
        ],
        "NamespaceList": [
            "adadadadmin"
        ],
        "RequestId": "fe6d6a40-fe7e-43d9-818e-e0afd7975663",
        "TotalCount": 33
    }
}
```

