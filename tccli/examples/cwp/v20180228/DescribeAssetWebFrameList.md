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
                "Lang": "abc",
                "ServiceType": "abc",
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
                },
                "Path": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

