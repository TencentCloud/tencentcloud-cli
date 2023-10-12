**Example 1: 获取资产管理端口列表**



Input: 

```
tccli cwp DescribeAssetPortInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Ports": [
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
                "ProcessName": "abc",
                "ProcessVersion": "abc",
                "ProcessPath": "abc",
                "Pid": "abc",
                "User": "abc",
                "StartTime": "abc",
                "Param": "abc",
                "Teletype": "abc",
                "Port": "abc",
                "GroupName": "abc",
                "Md5": "abc",
                "Ppid": "abc",
                "ParentProcessName": "abc",
                "Proto": "abc",
                "BindIp": "abc",
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

