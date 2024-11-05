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
                "MachineIp": "10.0.0.11",
                "MachineWanIp": "110.84.0.11",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "OsInfo": "CentOs Bit64",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "Name": "test-name",
                "Version": "0.1.1",
                "RootPath": "/root",
                "ServiceType": "Nginx",
                "Domain": "www.test.com",
                "VirtualPath": "/root",
                "PluginCount": 1,
                "Id": "10001",
                "Desc": "test domain",
                "MachineName": "test-name",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "110.84.0.11",
                    "PrivateIP": "10.0.0.11",
                    "NetworkType": 0,
                    "NetworkName": "vpc-12341234",
                    "InstanceID": "ins-aj28fjz",
                    "HostName": "test-name"
                }
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

