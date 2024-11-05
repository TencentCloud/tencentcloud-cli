**Example 1: 获取资产管理Web框架列表**



Input: 

```
tccli cwp DescribeAssetWebFrameList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WebFrames": [
            {
                "MachineIp": "1.1.1.1",
                "MachineWanIp": "1.1.1.1",
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
                "Lang": "zh_cn",
                "ServiceType": "tcp",
                "MachineName": "test-name",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 0,
                    "NetworkName": "vpc-id",
                    "InstanceID": "ins-id",
                    "HostName": "test-name"
                },
                "Path": "/root"
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

