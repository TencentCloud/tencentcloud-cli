**Example 1: 获取资产管理Web应用列表**



Input: 

```
tccli cwp DescribeAssetWebAppList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "WebApps": [
            {
                "OsInfo": "xx",
                "Domain": "xx",
                "Id": "xx",
                "MachineWanIp": "xx",
                "Uuid": "xx",
                "ProjectId": 1,
                "RootPath": "xx",
                "PluginCount": 1,
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "Version": "xx",
                "Quuid": "xx",
                "Desc": "xx",
                "VirtualPath": "xx",
                "ServiceType": "xx",
                "MachineIp": "xx",
                "Name": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

