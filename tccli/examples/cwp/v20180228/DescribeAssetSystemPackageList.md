**Example 1: 获取资产管理系统安装包列表**



Input: 

```
tccli cwp DescribeAssetSystemPackageList --cli-unfold-argument  \
    --Uuid xx \
    --Limit 1 \
    --Quuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Packages": [
            {
                "Name": "xx",
                "Version": "xx",
                "Type": 1,
                "InstallTime": "xx",
                "Desc": "xx"
            }
        ],
        "RequestId": "xx",
        "Total": 1
    }
}
```

