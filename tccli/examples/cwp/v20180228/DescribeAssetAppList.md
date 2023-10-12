**Example 1: 查询应用列表**



Input: 

```
tccli cwp DescribeAssetAppList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Apps": [
            {
                "MachineIp": "abc",
                "MachineName": "abc",
                "MachineWanIp": "abc",
                "Uuid": "abc",
                "Quuid": "abc",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "abc",
                        "TagId": 1
                    }
                ],
                "Name": "abc",
                "Type": 1,
                "BinPath": "abc",
                "OsInfo": "abc",
                "ProcessCount": 1,
                "Desc": "abc",
                "Version": "abc",
                "ConfigPath": "abc",
                "FirstTime": "abc",
                "UpdateTime": "abc",
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
        "Total": 1,
        "RequestId": "abc"
    }
}
```

