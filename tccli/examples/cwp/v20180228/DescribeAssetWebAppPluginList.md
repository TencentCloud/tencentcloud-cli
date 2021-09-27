**Example 1: 获取资产管理Web应用插件列表**



Input: 

```
tccli cwp DescribeAssetWebAppPluginList --cli-unfold-argument  \
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
        "Total": 1,
        "RequestId": "xx",
        "Plugins": [
            {
                "Version": "xx",
                "Link": "xx",
                "Name": "xx",
                "Desc": "xx"
            }
        ]
    }
}
```

