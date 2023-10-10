**Example 1: 获取Web站点虚拟目录列表**



Input: 

```
tccli cwp DescribeAssetWebLocationPathList --cli-unfold-argument  \
    --Offset 1 \
    --Id xx \
    --Limit 1 \
    --Uuid xx \
    --Quuid xx
```

Output: 
```
{
    "Response": {
        "Paths": [
            {
                "Permission": "xx",
                "Group": "xx",
                "User": "xx",
                "RealPath": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

