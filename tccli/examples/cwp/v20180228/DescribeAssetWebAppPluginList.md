**Example 1: 获取资产管理Web应用插件列表**



Input: 

```
tccli cwp DescribeAssetWebAppPluginList --cli-unfold-argument  \
    --Offset 1 \
    --Id 1001 \
    --Limit 1 \
    --Uuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Quuid 24c9be55-c743-4a75-a5c7-2a2912341234
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82",
        "Plugins": [
            {
                "Version": "0.1.1",
                "Link": "/bin",
                "Name": "test-name",
                "Desc": "test app"
            }
        ]
    }
}
```

