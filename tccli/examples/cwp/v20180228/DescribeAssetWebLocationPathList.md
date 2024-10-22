**Example 1: 获取Web站点虚拟目录列表**



Input: 

```
tccli cwp DescribeAssetWebLocationPathList --cli-unfold-argument  \
    --Quuid 6cf3c132-68ed-11ea-b08d-98be94213712 \
    --Uuid 6cf3c132-68ed-11ea-b08d-98be94213712 \
    --Id 1000 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Paths": [
            {
                "VirtualPath": "/a/b",
                "RealPath": "/a/b",
                "User": "user1",
                "Group": "group1",
                "Permission": "066"
            }
        ],
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

