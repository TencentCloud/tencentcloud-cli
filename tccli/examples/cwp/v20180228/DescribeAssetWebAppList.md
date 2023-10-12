**Example 1: 获取资产管理Web应用列表**



Input: 

```
tccli cwp DescribeAssetWebAppList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WebApps": [
            {
                "MachineIp": "abc",
                "MachineWanIp": "abc",
                "Quuid": "abc",
                "Uuid": "abc",
                "OsInfo": "abc",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "abc",
                        "TagId": 1
                    }
                ],
                "Name": "abc",
                "Version": "abc",
                "RootPath": "abc",
                "ServiceType": "abc",
                "Domain": "abc",
                "VirtualPath": "abc",
                "PluginCount": 1,
                "Id": "abc",
                "Desc": "abc",
                "MachineName": "abc",
                "UpdateTime": "abc",
                "FirstTime": "abc",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "abc",
                    "PrivateIP": "abc",
                    "NetworkType": 0,
                    "NetworkName": "abc",
                    "InstanceID": "abc",
                    "HostName": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

