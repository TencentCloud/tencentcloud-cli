**Example 1: 获取资源监控列表**

获取资源监控列表

Input: 

```
tccli cwp DescribeAssetMachineList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Machines": [
            {
                "Quuid": "abc",
                "Uuid": "abc",
                "MachineIp": "abc",
                "MachineName": "abc",
                "OsInfo": "abc",
                "Cpu": "abc",
                "MemSize": 1,
                "MemLoad": "abc",
                "DiskSize": 1,
                "DiskLoad": "abc",
                "PartitionCount": 1,
                "MachineWanIp": "abc",
                "ProjectId": 1,
                "CpuSize": 1,
                "CpuLoad": "abc",
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "abc",
                        "TagId": 1
                    }
                ],
                "UpdateTime": "abc",
                "IsNew": 0,
                "FirstTime": "abc",
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

